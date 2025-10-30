---
name: web-crawler-ocr
description: 웹페이지 크롤링 + 이미지 OCR 자동 분석. "이 URL 분석해줘", "크롤링해줘", "웹사이트 분석", "사이트 크롤링", "경쟁사 분석", "페이지 추출", "analyze this URL", "crawl website", "competitor analysis", "extract webpage" 등을 언급하거나 https:// 또는 http:// URL을 제공하면 자동 실행. Claude의 5MB 이미지 제한을 Gemini OCR(20MB)로 우회.
allowed-tools: Bash, Read, Write
---

# Web Crawler + Gemini OCR Integration Skill

웹페이지의 텍스트와 이미지를 완전하게 추출하여 마크다운 파일로 저장합니다.

## ⚠️ 사전 준비

**첫 사용 시 설정 필요:**

1. **Python 가상환경 및 패키지 설치** (자동화: `/setup-web-crawler` 사용)
2. **API 키 설정** (수동 필요):
   ```bash
   export GEMINI_API_KEY="your_gemini_api_key_here"
   export FIRECRAWL_API_KEY="your_firecrawl_api_key_here"
   ```

자세한 설정은 [SETUP_GUIDE.md](./SETUP_GUIDE.md)를 참고하세요.

## 🎯 사용 시나리오 및 실행 방법

### 1. 경쟁사 웹사이트 분석

**Trigger 키워드:**
- "이 경쟁사 사이트 분석해줘: https://competitor-cafe.com"
- "크롤링해줘: https://example.com"

**실행 과정:**
1. URL 식별
2. 적절한 저장 경로 결정 (예: `50-resources/competitor-analysis/`)
3. 스크립트 실행:
   ```bash
   cd skills/web-crawler-ocr/scripts && \
   source venv/bin/activate && \
   python3 web-crawler.py "https://competitor-cafe.com" "../../50-resources/competitor-analysis/competitor-cafe-20251031.md"
   ```
4. 결과 파일 읽기 및 인사이트 제공

**출력 위치:**
- 경쟁사 분석: `50-resources/competitor-analysis/`
- 교육 자료: `10-projects/12-education/{project}/`
- 일반 리서치: `50-resources/web-research/`

### 2. 여러 URL 일괄 처리

**Trigger 키워드:**
- "이 3개 사이트 분석해줘: https://a.com, https://b.com, https://c.com"

**실행:**
각 URL을 순차적으로 처리하고 비교 분석 제공

### 3. 대용량 이미지 OCR

**Trigger 키워드:**
- "이 페이지 이미지들 OCR 해줘"
- "큰 이미지 있는데 분석해줘"

**장점:**
- Claude의 5MB 이미지 제한 우회
- Gemini OCR로 20MB 이미지 처리
- 웹페이지 내 모든 이미지 자동 추출 및 분석

## 🔧 스크립트 실행 예시

### 기본 사용

```bash
cd skills/web-crawler-ocr/scripts
source venv/bin/activate
python3 web-crawler.py "https://example.com"
```

### 출력 파일 지정

```bash
python3 web-crawler.py "https://competitor.com" "../../50-resources/competitor-analysis/result.md"
```

### 환경변수 확인

```bash
echo $GEMINI_API_KEY
echo $FIRECRAWL_API_KEY
```

## 📋 출력 형식

생성되는 마크다운 파일 구조:

```markdown
# 페이지 제목

> 출처: https://example.com
> 크롤링: 2025-10-31 15:30:00
> 도구: Firecrawl + Gemini OCR

---

## 📄 텍스트 내용

[Firecrawl로 추출한 깨끗한 텍스트]

---

## 🖼️ 이미지 분석 (Gemini OCR)

### 이미지 1
- **URL**: https://example.com/image1.jpg
- **Alt 텍스트**: Product photo

**분석 결과:**

[Gemini가 추출한 이미지 텍스트 및 설명]
```

## 🔍 작동 원리

1. **Firecrawl**: 웹페이지의 깨끗한 텍스트 추출 (광고/잡음 제거)
2. **이미지 다운로드**: HTML에서 이미지 URL 추출 및 다운로드
3. **Gemini OCR**: 각 이미지에서 텍스트 추출 및 내용 분석
4. **마크다운 생성**: 텍스트 + 이미지 분석을 하나의 마크다운으로 통합

## ⚠️ 제한사항

- **Gemini Free Tier**: 분당 15개 요청
- **Firecrawl Free Tier**: 500 크레딧
- **이미지 제한**: 페이지당 최대 10개 이미지 처리
- **파일 크기**: 이미지당 최대 20MB

## 🛠 트러블슈팅

### API 키 오류

```bash
# 환경변수 확인
echo $GEMINI_API_KEY
echo $FIRECRAWL_API_KEY

# 환경변수 설정
export GEMINI_API_KEY="your_key_here"
export FIRECRAWL_API_KEY="your_key_here"
```

### Python 패키지 오류

```bash
cd skills/web-crawler-ocr/scripts
source venv/bin/activate
pip install -r requirements.txt
```

### 스크립트를 찾을 수 없음

```bash
ls -la skills/web-crawler-ocr/scripts/web-crawler.py
```

## 📚 관련 문서

- **설정 가이드**: [SETUP_GUIDE.md](./SETUP_GUIDE.md)
- **빠른 시작**: [README.md](./README.md)
- **자동화 커맨드**: `/setup-web-crawler`

## 🎓 PKM 통합

이 skill은 다음 워크플로우에서 유용합니다:

1. **경쟁사 분석**: 경쟁사 웹사이트 → 마크다운 → 인사이트 추출
2. **교육 자료 수집**: 참고 사이트 → 정리된 문서 → 강의 자료화
3. **리서치 자동화**: 여러 URL → 일괄 크롤링 → 비교 분석

## 🔗 영감

이 skill은 Noah Brier의 [Claudesidian](https://github.com/heyitsnoah/claudesidian) 프로젝트에서 영감을 받았습니다:
- Firecrawl for web research
- Gemini for large image/PDF analysis
- Unix philosophy: simple composable tools
