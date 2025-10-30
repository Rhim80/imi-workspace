# Web Crawler + OCR Skill

> 웹페이지를 크롤링하고 이미지 OCR까지 자동으로 처리하는 All-in-One 솔루션

## 🎯 주요 기능

- ✅ **깨끗한 텍스트 추출**: Firecrawl로 광고/잡음 제거
- ✅ **대용량 이미지 OCR**: Gemini로 20MB 이미지 처리 (Claude 5MB 제한 우회)
- ✅ **완전한 마크다운 생성**: 텍스트 + 이미지 분석을 하나의 파일로
- ✅ **자동 실행**: URL만 제공하면 Claude Code가 자동으로 처리

## ⚡ 빠른 시작

### 1. 설정 (10분 소요)

**자동 설정 (권장):**
```
Claude Code에서 실행:
> /setup-web-crawler
```

**수동 설정:**
전체 설정 가이드는 [SETUP_GUIDE.md](./SETUP_GUIDE.md)를 참고하세요.

**요약:**
1. Python 가상환경 생성 및 패키지 설치
2. Gemini API Key 발급 (무료)
3. Firecrawl API Key 발급 (무료 티어)
4. 환경변수 설정

### 2. 대화로 사용하기

**예시 1: 경쟁사 분석**
```
You: 이 경쟁사 사이트 분석해줘: https://competitor-cafe.com

Claude: (자동으로 크롤링 + OCR 실행)
✅ 크롤링 완료! 3,200자 텍스트 + 7개 이미지 분석 완료

주요 인사이트:
1. 브랜드 포지셔닝: 프리미엄 스페셜티
2. 메뉴 구성: 시그니처 음료 5종 강조
3. 차별점: 로스팅 공간 가시화
```

**예시 2: 여러 URL 일괄 처리**
```
You: 이 3개 사이트 비교 분석해줘:
- https://cafe-a.com
- https://cafe-b.com
- https://cafe-c.com

Claude: (순차적으로 크롤링)
✅ 3개 사이트 분석 완료

비교 분석:
| 항목 | Cafe A | Cafe B | Cafe C |
|------|--------|--------|--------|
| 포지셔닝 | ... | ... | ... |
| 주력 상품 | ... | ... | ... |
```

**예시 3: 교육 자료 수집**
```
You: 이 HFK AI 페이지 내용 정리해서 강의 자료로 저장해줘
https://hfk.me/ai-team

Claude: ✅ 교육 자료 저장 완료
위치: 10-projects/12-education/12.06-hfk-winter-ai/hfk-ai-team-reference.md
```

## 📋 사용 시나리오

### 시나리오 1: 경쟁사 웹사이트 분석

**Input:**
```
"https://competitor.com 크롤링해서 분석해줘"
```

**Claude의 작업:**
1. URL 식별
2. `50-resources/competitor-analysis/` 경로에 저장
3. 크롤링 실행
4. 결과 분석 및 인사이트 제공

**Output:**
- 마크다운 파일 생성
- 텍스트 내용 요약
- 이미지 분석 결과
- 핵심 인사이트 정리

### 시나리오 2: 대용량 이미지가 있는 페이지

**Problem:**
- Claude는 5MB 이상 이미지 처리 불가
- 웹페이지에 고해상도 이미지 많음

**Solution:**
```
"이 페이지 이미지들 OCR 해줘: https://example.com/portfolio"
```

- Gemini OCR로 20MB 이미지 처리
- 모든 이미지 자동 다운로드 및 분석
- 텍스트 추출 + 내용 설명

### 시나리오 3: 리서치 자동화

**Input:**
```
"주요 AI 뉴스 사이트 3곳 크롤링해줘"
```

**Claude의 작업:**
1. 여러 URL 순차 처리
2. `50-resources/web-research/` 저장
3. 비교 분석 리포트 생성

## 🔧 기술 스택

- **Firecrawl**: 웹페이지 깨끗한 텍스트 추출
- **Gemini 2.5 Flash**: 이미지 OCR 및 분석
- **BeautifulSoup**: Firecrawl 실패 시 대체
- **Python**: 통합 스크립트

## 📂 출력 위치

Claude는 컨텍스트에 따라 적절한 위치에 저장합니다:

| 용도 | 경로 |
|------|------|
| 경쟁사 분석 | `50-resources/competitor-analysis/` |
| 교육 자료 | `10-projects/12-education/{project}/` |
| 일반 리서치 | `50-resources/web-research/` |

파일명 형식: `domain_YYYYMMDD_HHMMSS.md`

## 🎓 교육 활용

### 학생들에게 설명할 때

1. **설정은 간단해요** (10분)
   - `/setup-web-crawler` 한 번만 실행
   - API 키 2개만 발급받으면 끝

2. **사용은 더 간단해요** (대화만 하면 됨)
   - URL만 말하면 자동 실행
   - "크롤링해줘", "분석해줘" 같은 자연스러운 표현

3. **결과는 마크다운** (PKM 즉시 활용)
   - 텍스트 + 이미지 분석이 하나의 파일로
   - Obsidian에서 바로 보기 가능

## ⚠️ 제한사항

### 무료 티어 제한

**Gemini:**
- 분당 15개 요청
- 일일 1,500개 요청
- → 교육용으로 충분

**Firecrawl:**
- 500 크레딧
- 크롤링 1회 = 1 크레딧
- → 500개 페이지 크롤링 가능

### 기술적 제한

- 페이지당 최대 10개 이미지 처리
- 이미지당 최대 20MB
- JavaScript 렌더링 필요한 페이지는 제한적

## 🛠 트러블슈팅

### API 키 오류

**증상:**
```
❌ 다음 API 키가 설정되지 않았습니다: GEMINI_API_KEY
```

**해결:**
```bash
export GEMINI_API_KEY="your_key_here"
export FIRECRAWL_API_KEY="your_key_here"
```

### Python 패키지 오류

**증상:**
```
ModuleNotFoundError: No module named 'requests'
```

**해결:**
```bash
cd skills/web-crawler-ocr/scripts
source venv/bin/activate
pip install -r requirements.txt
```

### 크롤링 속도 제한

**증상:**
```
Gemini 분석 실패: 429 Resource exhausted
```

**해결:**
- 1분 대기 후 재시도
- 이미지가 많은 페이지는 여러 번에 나누어 처리

## 📚 상세 문서

- **[SETUP_GUIDE.md](./SETUP_GUIDE.md)**: 단계별 설정 가이드
- **[SKILL.md](./SKILL.md)**: Claude Code 통합 상세
- **자동화 커맨드**: `/setup-web-crawler`

## 🔗 영감

이 skill은 [Claudesidian](https://github.com/heyitsnoah/claudesidian) (Noah Brier)에서 영감을 받았습니다.

- **철학**: Unix philosophy - Simple, Composable Tools
- **도구**: Firecrawl (웹 리서치) + Gemini (대용량 분석)
- **목표**: 비개발자도 쉽게 사용 가능한 자동화

## 🤝 기여

이 skill을 개선하고 싶으시다면:

1. 스크립트 위치: `skills/web-crawler-ocr/scripts/web-crawler.py`
2. 이슈 제보: GitHub Issues
3. 개선 제안: Pull Requests 환영

---

**버전**: 1.0.0
**최종 업데이트**: 2025-10-31
**유지보수**: IMI WORK (이림)
