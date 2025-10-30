# Web Crawler + OCR Setup Guide

> 웹페이지 크롤링 + 이미지 OCR 통합 시스템 설정 가이드

**예상 소요 시간**: 10분

## 📋 준비물

1. Python 3.8 이상
2. Gemini API Key (무료)
3. Firecrawl API Key (무료 티어 가능)

---

## Step 1: Python 및 pip 확인

### 1-1. Python 버전 확인

```bash
python3 --version
```

**예상 출력:**
```
Python 3.11.x 또는 3.12.x
```

### 1-2. pip 확인

```bash
python3 -m pip --version
```

**pip가 없다면:**

```bash
# macOS (Homebrew)
brew install python

# Linux/WSL
sudo apt update
sudo apt install python3-pip

# Windows
# Python 설치 시 "Add Python to PATH" 체크
```

---

## Step 2: Python 가상환경 생성 및 패키지 설치

### 2-1. 가상환경 생성

**imi-workspace 루트에서 실행:**

```bash
cd skills/web-crawler-ocr/scripts
python3 -m venv venv
```

**확인:**
```bash
ls -la venv/
```

예상 출력: `bin/`, `lib/`, `pyvenv.cfg` 등

### 2-2. 가상환경 활성화

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

**활성화 확인:**
프롬프트 앞에 `(venv)` 표시가 나타나야 함

### 2-3. 패키지 설치

```bash
pip install -r requirements.txt
```

**예상 출력:**
```
Successfully installed requests-2.31.0 beautifulsoup4-4.12.0 firecrawl-py-0.0.14 google-generativeai-0.3.0 python-dotenv-1.0.0 markdownify-0.11.6
```

### 2-4. 설치 확인

```bash
pip list
```

**필수 패키지 확인:**
- `requests`
- `beautifulsoup4`
- `firecrawl-py`
- `google-generativeai`
- `python-dotenv`
- `markdownify`

---

## Step 3: API 키 발급

### 3-1. Gemini API Key 발급

1. **Google AI Studio 접속**: https://aistudio.google.com/apikey
2. **"Create API Key" 버튼 클릭**
3. **프로젝트 선택 또는 생성**
4. **API 키 복사** (예: `AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX`)

**무료 티어:**
- 분당 15개 요청
- 일일 1,500개 요청
- 교육용으로 충분한 용량

### 3-2. Firecrawl API Key 발급

1. **Firecrawl 접속**: https://firecrawl.dev
2. **Sign Up** (GitHub 계정으로 가능)
3. **Dashboard → API Keys**
4. **API 키 복사** (예: `fc-XXXXXXXXXXXXXXXXXXXXXXXX`)

**무료 티어:**
- 500 크레딧
- 크롤링 1회 = 1 크레딧
- 테스트 및 소규모 사용에 적합

---

## Step 4: 환경변수 설정

### 방법 A: .env 파일 생성 (권장)

**imi-workspace/skills/web-crawler-ocr/scripts/.env 파일 생성:**

```bash
cd skills/web-crawler-ocr/scripts
cat > .env <<'EOF'
GEMINI_API_KEY=your_gemini_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
EOF
```

**실제 키로 수정:**

```bash
# nano 또는 vim으로 편집
nano .env
```

**.env 파일 예시:**
```
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX
FIRECRAWL_API_KEY=fc-XXXXXXXXXXXXXXXXXXXXXXXX
```

**저장 후 확인:**
```bash
cat .env
```

### 방법 B: Shell 환경변수 설정 (세션 한정)

**현재 세션에만 적용:**

```bash
export GEMINI_API_KEY="your_gemini_api_key_here"
export FIRECRAWL_API_KEY="your_firecrawl_api_key_here"
```

**확인:**
```bash
echo $GEMINI_API_KEY
echo $FIRECRAWL_API_KEY
```

### 방법 C: Shell RC 파일 추가 (영구 설정)

**zsh 사용자 (~/.zshrc):**

```bash
echo 'export GEMINI_API_KEY="your_gemini_api_key_here"' >> ~/.zshrc
echo 'export FIRECRAWL_API_KEY="your_firecrawl_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

**bash 사용자 (~/.bashrc):**

```bash
echo 'export GEMINI_API_KEY="your_gemini_api_key_here"' >> ~/.bashrc
echo 'export FIRECRAWL_API_KEY="your_firecrawl_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

---

## Step 5: 테스트

### 5-1. 스크립트 실행 테스트

```bash
cd skills/web-crawler-ocr/scripts
source venv/bin/activate
python3 web-crawler.py https://example.com
```

**예상 출력:**
```
================================================================================
🚀 웹 크롤링 + OCR 시작
================================================================================

🔍 Firecrawl로 텍스트 추출 중: https://example.com
✅ 텍스트 추출 완료 (2543 글자)
🖼️ 이미지 1개 발견

🤖 Gemini OCR 처리 중 (1개 이미지)...
  [1/1] https://example.com/image.jpg

================================================================================
✅ 완료: /Users/rhim/Projects/imi-workspace/example.com_20251031_153045.md
================================================================================
```

### 5-2. 결과 파일 확인

```bash
ls -lh example.com_*.md
```

**파일 내용 확인:**
```bash
head -20 example.com_*.md
```

---

## 🛠 트러블슈팅

### 1. `ModuleNotFoundError: No module named 'requests'`

**원인**: 가상환경이 활성화되지 않았거나 패키지 미설치

**해결:**
```bash
cd skills/web-crawler-ocr/scripts
source venv/bin/activate
pip install -r requirements.txt
```

### 2. `❌ 다음 API 키가 설정되지 않았습니다: GEMINI_API_KEY`

**원인**: 환경변수가 설정되지 않음

**해결:**
```bash
# .env 파일 확인
cat skills/web-crawler-ocr/scripts/.env

# 환경변수 수동 설정
export GEMINI_API_KEY="your_key_here"
export FIRECRAWL_API_KEY="your_key_here"
```

### 3. `Firecrawl 실패, BeautifulSoup으로 대체`

**원인**: Firecrawl API 키 문제 또는 크레딧 소진

**해결:**
- Firecrawl 대시보드에서 크레딧 확인
- API 키 재확인
- BeautifulSoup으로 대체되어도 기본 크롤링은 작동함

### 4. `Gemini 분석 실패: 429 Resource exhausted`

**원인**: Gemini API 무료 티어 속도 제한 (분당 15개)

**해결:**
- 1분 대기 후 재시도
- 이미지가 많은 페이지는 여러 번에 나누어 처리

### 5. 가상환경 활성화 오류

**macOS/Linux에서 `command not found: activate`:**

```bash
# 올바른 명령어
source venv/bin/activate

# 또는
. venv/bin/activate
```

**Windows에서 실행 정책 오류:**

```powershell
# PowerShell 실행 정책 변경
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 가상환경 활성화
venv\Scripts\activate
```

---

## 📚 다음 단계

설정이 완료되었다면:

1. **README.md 읽기**: 사용 예시 확인
2. **SKILL.md 읽기**: Claude Code 통합 방법
3. **실습**: 실제 웹사이트 크롤링 시도

**추천 실습 URL:**
- https://example.com (테스트)
- https://news.ycombinator.com (텍스트 많음)
- https://unsplash.com (이미지 많음)

---

## 🔒 보안 주의사항

1. **.env 파일을 Git에 커밋하지 마세요**
   - `.gitignore`에 `.env` 포함 확인
   - API 키는 절대 공개 저장소에 업로드 금지

2. **API 키 공유 금지**
   - 스크린샷, 문서, 채팅에 API 키 노출 주의

3. **무료 티어 모니터링**
   - Gemini: https://aistudio.google.com/apikey
   - Firecrawl: https://firecrawl.dev/dashboard

---

## 📞 도움이 필요하시면

- **문서**: [README.md](./README.md), [SKILL.md](./SKILL.md)
- **자동화 커맨드**: `/setup-web-crawler` (Claude Code에서 실행)
- **스크립트 위치**: `skills/web-crawler-ocr/scripts/web-crawler.py`
