#!/usr/bin/env python3
"""
범용 웹 크롤러 + Gemini OCR 통합 시스템

Firecrawl로 텍스트 추출 → 이미지 다운로드 → Gemini OCR → 완전한 마크다운 생성

사용법:
  python web-crawler.py <URL> [출력_파일명]

예시:
  python web-crawler.py https://example.com/article
  python web-crawler.py https://competitor-cafe.com analysis.md
"""

import os
import sys
import json
import requests
import base64
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import google.generativeai as genai

# 환경변수 로드
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

# 색상 출력
class Colors:
    BLUE = '\033[0;34m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    RED = '\033[0;31m'
    NC = '\033[0m'

def print_color(text, color):
    """색상 출력"""
    print(f"{color}{text}{Colors.NC}")

def check_api_keys():
    """API 키 확인"""
    missing = []

    if not GEMINI_API_KEY:
        missing.append("GEMINI_API_KEY")

    if not FIRECRAWL_API_KEY:
        missing.append("FIRECRAWL_API_KEY")

    if missing:
        print_color(f"❌ 다음 API 키가 설정되지 않았습니다: {', '.join(missing)}", Colors.RED)
        print("\n설정 방법:")
        print("1. .env 파일 생성 또는 환경변수 설정:")
        print("   GEMINI_API_KEY='your_key_here'")
        print("   FIRECRAWL_API_KEY='your_key_here'")
        print("\n2. API 키 발급:")
        print("   - Gemini: https://aistudio.google.com/apikey")
        print("   - Firecrawl: https://firecrawl.dev")
        sys.exit(1)

def crawl_with_firecrawl(url):
    """Firecrawl로 웹페이지 크롤링"""
    print_color(f"🔍 Firecrawl로 텍스트 추출 중: {url}", Colors.BLUE)

    try:
        from firecrawl import FirecrawlApp

        app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)
        result = app.scrape_url(url, params={
            'formats': ['markdown', 'html'],
            'onlyMainContent': True
        })

        if result.get('success'):
            markdown = result.get('markdown', '')
            html = result.get('html', '')
            metadata = result.get('metadata', {})

            print_color(f"✅ 텍스트 추출 완료 ({len(markdown)} 글자)", Colors.GREEN)
            return {
                'markdown': markdown,
                'html': html,
                'metadata': metadata
            }
        else:
            print_color("⚠️ Firecrawl 실패, BeautifulSoup으로 대체", Colors.YELLOW)
            return crawl_with_beautifulsoup(url)

    except ImportError:
        print_color("⚠️ firecrawl-py 미설치, BeautifulSoup으로 대체", Colors.YELLOW)
        return crawl_with_beautifulsoup(url)
    except Exception as e:
        print_color(f"⚠️ Firecrawl 오류: {e}, BeautifulSoup으로 대체", Colors.YELLOW)
        return crawl_with_beautifulsoup(url)

def crawl_with_beautifulsoup(url):
    """BeautifulSoup으로 대체 크롤링"""
    print_color("🔄 BeautifulSoup으로 크롤링 중...", Colors.BLUE)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    # 본문 추출
    article = soup.find('article') or soup.find('main') or soup.body
    text = article.get_text(separator='\n', strip=True) if article else soup.get_text(separator='\n', strip=True)

    # 메타데이터 추출
    title = soup.find('title')
    title_text = title.text if title else urlparse(url).netloc

    return {
        'markdown': text,
        'html': str(soup),
        'metadata': {
            'title': title_text,
            'sourceURL': url
        }
    }

def extract_images_from_html(html, base_url):
    """HTML에서 이미지 URL 추출"""
    soup = BeautifulSoup(html, 'html.parser')
    images = []

    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src')
        if src:
            # 상대 경로를 절대 경로로 변환
            full_url = urljoin(base_url, src)

            # alt 텍스트
            alt = img.get('alt', '')

            images.append({
                'url': full_url,
                'alt': alt
            })

    print_color(f"🖼️ 이미지 {len(images)}개 발견", Colors.GREEN)
    return images

def download_image(url, output_dir):
    """이미지 다운로드"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # 파일명 생성
        filename = Path(urlparse(url).path).name or 'image.jpg'
        filepath = output_dir / filename

        with open(filepath, 'wb') as f:
            f.write(response.content)

        return filepath
    except Exception as e:
        print_color(f"⚠️ 이미지 다운로드 실패: {url} ({e})", Colors.YELLOW)
        return None

def analyze_image_with_gemini(image_path):
    """Gemini로 이미지 OCR 및 분석"""
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash')

        # 이미지 로드
        with open(image_path, 'rb') as f:
            image_data = f.read()

        # Gemini에 분석 요청
        response = model.generate_content([
            "이 이미지의 모든 텍스트를 추출하고, 주요 내용을 설명해주세요. 한글로 답변해주세요.",
            {'mime_type': 'image/jpeg', 'data': image_data}
        ])

        return response.text
    except Exception as e:
        print_color(f"⚠️ Gemini 분석 실패: {e}", Colors.YELLOW)
        return None

def process_url(url, output_file=None):
    """URL 전체 처리 워크플로우"""

    print_color(f"\n{'='*80}", Colors.BLUE)
    print_color(f"🚀 웹 크롤링 + OCR 시작", Colors.BLUE)
    print_color(f"{'='*80}\n", Colors.BLUE)

    # 1. Firecrawl로 텍스트 크롤링
    crawl_result = crawl_with_firecrawl(url)
    markdown_text = crawl_result['markdown']
    html = crawl_result['html']
    metadata = crawl_result['metadata']

    # 2. 이미지 추출
    images = extract_images_from_html(html, url)

    # 3. 이미지 다운로드 및 OCR
    temp_dir = Path('/tmp/web-crawler-images')
    temp_dir.mkdir(exist_ok=True)

    image_analyses = []

    if images:
        print_color(f"\n🤖 Gemini OCR 처리 중 ({len(images)}개 이미지)...", Colors.BLUE)

        for i, img in enumerate(images[:10], 1):  # 최대 10개까지
            print(f"  [{i}/{min(len(images), 10)}] {img['url']}")

            # 다운로드
            filepath = download_image(img['url'], temp_dir)
            if not filepath:
                continue

            # Gemini OCR
            analysis = analyze_image_with_gemini(filepath)
            if analysis:
                image_analyses.append({
                    'url': img['url'],
                    'alt': img['alt'],
                    'analysis': analysis
                })

    # 4. 최종 마크다운 생성
    final_markdown = generate_final_markdown(
        url=url,
        metadata=metadata,
        text=markdown_text,
        image_analyses=image_analyses
    )

    # 5. 파일 저장
    if not output_file:
        # URL에서 파일명 생성
        domain = urlparse(url).netloc.replace('www.', '')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"{domain}_{timestamp}.md"

    output_path = Path(output_file)
    output_path.write_text(final_markdown, encoding='utf-8')

    print_color(f"\n{'='*80}", Colors.GREEN)
    print_color(f"✅ 완료: {output_path.absolute()}", Colors.GREEN)
    print_color(f"{'='*80}\n", Colors.GREEN)

    return output_path

def generate_final_markdown(url, metadata, text, image_analyses):
    """최종 마크다운 생성"""

    title = metadata.get('title', 'Untitled')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    md = f"""# {title}

> 출처: {url}
> 크롤링: {timestamp}
> 도구: Firecrawl + Gemini OCR

---

## 📄 텍스트 내용

{text}

"""

    if image_analyses:
        md += "\n---\n\n## 🖼️ 이미지 분석 (Gemini OCR)\n\n"

        for i, img in enumerate(image_analyses, 1):
            md += f"### 이미지 {i}\n\n"
            md += f"- **URL**: {img['url']}\n"
            if img['alt']:
                md += f"- **Alt 텍스트**: {img['alt']}\n"
            md += f"\n**분석 결과:**\n\n{img['analysis']}\n\n---\n\n"

    return md

def main():
    """메인 실행"""

    # API 키 확인
    check_api_keys()

    # 인자 확인
    if len(sys.argv) < 2:
        print("사용법: python web-crawler.py <URL> [출력_파일명]")
        print("\n예시:")
        print("  python web-crawler.py https://example.com/article")
        print("  python web-crawler.py https://competitor.com analysis.md")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    # 처리 실행
    result = process_url(url, output_file)

    print(f"📂 결과 파일: {result}")
    print("\n💡 Claude Code에서 활용:")
    print(f"   > {result} 읽고 핵심 인사이트 정리해줘")

if __name__ == "__main__":
    main()
