# Setup Web Crawler + OCR - 대화형 설정 마법사

웹 크롤링 + 이미지 OCR 통합 시스템을 자동으로 설정합니다.

## 🎯 수행 작업

### Phase 1: 자동 설치 (Claude가 실행)
1. ✅ Python 및 pip 확인
2. ✅ 가상환경 생성 (`skills/web-crawler-ocr/scripts/venv`)
3. ✅ Python 패키지 설치 (requests, firecrawl-py, google-generativeai 등)
4. ✅ 설치 확인 테스트

### Phase 2: API 키 설정 (사용자 필요)
1. 🔐 Gemini API Key 발급 안내
2. 🔐 Firecrawl API Key 발급 안내
3. ✅ .env 파일 생성 방법 안내

### Phase 3: 테스트 및 완료
1. 📋 API 키 확인
2. 🧪 테스트 크롤링 (선택 사항)
3. 🎉 완료 메시지
4. 💡 사용 가능한 기능 안내

---

## 실행 단계

### Step 1: 환경 확인

먼저 Python 환경을 확인합니다.

**1-1. Python 버전 확인:**
```bash
python3 --version
```

**1-2. pip 확인:**
```bash
python3 -m pip --version
```

**예상 출력:**
- Python 3.8 이상
- pip 20.0 이상

**문제 발생 시:**
- Python이 없으면 설치 안내 제공
- pip가 없으면 설치 방법 안내

---

### Step 2: 가상환경 생성 및 패키지 설치

**2-1. 작업 디렉토리 이동:**
```bash
cd skills/web-crawler-ocr/scripts
```

**2-2. 가상환경 생성:**
```bash
python3 -m venv venv
```

**2-3. 가상환경 확인:**
```bash
ls -la venv/
```

**예상 출력:**
- `bin/` 폴더 (실행 파일)
- `lib/` 폴더 (패키지)
- `pyvenv.cfg` (설정)

**2-4. 가상환경 활성화 및 패키지 설치:**

**macOS/Linux:**
```bash
source venv/bin/activate && pip install -r requirements.txt
```

**Windows (사용자가 WSL이 아닌 경우):**
```bash
venv\Scripts\activate && pip install -r requirements.txt
```

**예상 소요 시간:** 30초 ~ 2분

**2-5. 설치 확인:**
```bash
pip list | grep -E "(requests|beautifulsoup4|firecrawl|google-generativeai|python-dotenv)"
```

**필수 패키지 확인:**
- `requests`
- `beautifulsoup4`
- `firecrawl-py`
- `google-generativeai`
- `python-dotenv`
- `markdownify`

---

### Step 3: API 키 발급 안내 (사용자 수동 작업)

이 단계는 **사용자가 직접 수행**해야 합니다.

**3-1. Gemini API Key 발급:**

1. **Google AI Studio 접속**: https://aistudio.google.com/apikey
2. **"Create API Key" 버튼 클릭**
3. **프로젝트 선택 또는 생성**
4. **API 키 복사** (예: `AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX`)

**무료 티어:**
- 분당 15개 요청
- 일일 1,500개 요청
- 교육용으로 충분한 용량

**3-2. Firecrawl API Key 발급:**

1. **Firecrawl 접속**: https://firecrawl.dev
2. **Sign Up** (GitHub 계정으로 간편 가입)
3. **Dashboard → API Keys**
4. **API 키 복사** (예: `fc-XXXXXXXXXXXXXXXXXXXXXXXX`)

**무료 티어:**
- 500 크레딧
- 크롤링 1회 = 1 크레딧
- 테스트 및 소규모 사용에 적합

---

### Step 4: .env 파일 생성 (사용자 수동 작업)

**4-1. .env 파일 생성 방법 안내:**

사용자에게 다음을 안내합니다:

```
API 키 발급이 완료되면, 다음 명령어로 .env 파일을 생성하세요:

cd skills/web-crawler-ocr/scripts
cat > .env <<'EOF'
GEMINI_API_KEY=your_gemini_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
EOF

그 다음 에디터로 실제 키를 입력하세요:
nano .env

또는 Claude Code에게 요청:
"skills/web-crawler-ocr/scripts/.env 파일 만들어줘.
GEMINI_API_KEY=AIzaSy...
FIRECRAWL_API_KEY=fc-..."
```

**4-2. .env 파일 예시:**
```
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX
FIRECRAWL_API_KEY=fc-XXXXXXXXXXXXXXXXXXXXXXXX
```

**4-3. 환경변수 확인 (Claude 실행):**

API 키가 설정되었는지 확인:

```bash
cd skills/web-crawler-ocr/scripts
if [ -f .env ]; then
  echo "✅ .env 파일이 존재합니다."
  echo ""
  echo "파일 내용:"
  cat .env | sed 's/\(API_KEY=\).*/\1***HIDDEN***/'
else
  echo "⚠️ .env 파일이 없습니다."
  echo ""
  echo "다음 명령어로 생성하세요:"
  echo "cat > .env <<'EOF'"
  echo "GEMINI_API_KEY=your_gemini_key_here"
  echo "FIRECRAWL_API_KEY=your_firecrawl_key_here"
  echo "EOF"
fi
```

---

### Step 5: 테스트 크롤링 (선택 사항)

**5-1. 사용자에게 테스트 여부 확인:**

```
설정이 완료되었습니다! 테스트 크롤링을 실행하시겠습니까?

테스트 URL: https://example.com
(간단한 페이지로 약 10초 소요)

테스트를 원하시면 "테스트 해줘" 또는 "yes"라고 말씀해주세요.
건너뛰려면 "아니요" 또는 "skip"이라고 말씀해주세요.
```

**5-2. 테스트 실행 (사용자가 원하는 경우):**

```bash
cd skills/web-crawler-ocr/scripts && \
source venv/bin/activate && \
python3 web-crawler.py https://example.com test-output.md
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
  [1/1] https://example.com/iana-logo.svg

================================================================================
✅ 완료: /Users/rhim/Projects/imi-workspace/skills/web-crawler-ocr/scripts/test-output.md
================================================================================
```

**5-3. 결과 확인:**

```bash
ls -lh test-output.md && head -20 test-output.md
```

---

### Step 6: 완료 메시지

설정이 완료되면 사용자에게 다음 메시지를 제공합니다:

```
🎉 Web Crawler + OCR 설정 완료!

✅ Python 가상환경 생성
✅ 필수 패키지 설치
✅ API 키 설정
✅ 테스트 크롤링 성공

📚 이제 다음과 같이 사용할 수 있습니다:

1️⃣ 대화로 사용:
   "https://competitor-cafe.com 분석해줘"
   "이 3개 사이트 크롤링해줘"

2️⃣ 직접 실행:
   cd skills/web-crawler-ocr/scripts
   source venv/bin/activate
   python3 web-crawler.py <URL> [출력파일명]

3️⃣ 상세 문서:
   - README.md: 사용 가이드
   - SETUP_GUIDE.md: 상세 설정 가이드
   - SKILL.md: Claude Code 통합 방법

💡 Tip:
   URL을 말하거나 "크롤링해줘", "분석해줘" 같은 키워드를 사용하면
   Claude Code가 자동으로 크롤링을 실행합니다!
```

---

## 🛠 트러블슈팅

### 1. Python이 없는 경우

```bash
# macOS (Homebrew)
brew install python

# Linux/WSL
sudo apt update
sudo apt install python3 python3-pip

# Windows
# Python 공식 사이트에서 설치: https://www.python.org/downloads/
```

### 2. 가상환경 생성 실패

```bash
# python3-venv 패키지 설치 (Linux/WSL)
sudo apt install python3-venv

# 재시도
python3 -m venv venv
```

### 3. 패키지 설치 오류

```bash
# pip 업그레이드
python3 -m pip install --upgrade pip

# requirements.txt 재설치
cd skills/web-crawler-ocr/scripts
source venv/bin/activate
pip install -r requirements.txt --upgrade
```

### 4. API 키 오류

**증상:**
```
❌ 다음 API 키가 설정되지 않았습니다: GEMINI_API_KEY
```

**해결:**
```bash
# .env 파일 확인
cat skills/web-crawler-ocr/scripts/.env

# 없으면 생성
cd skills/web-crawler-ocr/scripts
cat > .env <<'EOF'
GEMINI_API_KEY=your_gemini_key
FIRECRAWL_API_KEY=your_firecrawl_key
EOF

# 실제 키로 수정
nano .env
```

### 5. 가상환경 활성화 오류

**macOS/Linux에서 `command not found: activate`:**

```bash
# 올바른 명령어
source venv/bin/activate

# 또는
. venv/bin/activate
```

**Windows PowerShell 실행 정책 오류:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

---

## 📋 체크리스트

설정 완료 후 다음을 확인합니다:

- [ ] Python 3.8 이상 설치됨
- [ ] 가상환경 생성됨 (`skills/web-crawler-ocr/scripts/venv/`)
- [ ] 필수 패키지 6개 설치됨
- [ ] .env 파일 생성됨
- [ ] Gemini API Key 설정됨
- [ ] Firecrawl API Key 설정됨
- [ ] 테스트 크롤링 성공 (선택 사항)

---

## 🔒 보안 주의사항

**중요: 다음을 사용자에게 반드시 안내하세요**

1. **.env 파일을 Git에 커밋하지 마세요**
   ```bash
   # .gitignore 확인
   grep ".env" .gitignore

   # 없으면 추가
   echo ".env" >> .gitignore
   ```

2. **API 키 공유 금지**
   - 스크린샷, 문서, 채팅에 API 키 노출 주의

3. **무료 티어 모니터링**
   - Gemini: https://aistudio.google.com/apikey
   - Firecrawl: https://firecrawl.dev/dashboard

---

**예상 소요 시간:**
- 자동 설치: 2-3분
- API 키 발급: 5분
- 테스트: 1분
- **총 10분 이내**

**교육 최적화:**
- 학생들이 동일한 경험
- Claude가 자동화 가능한 부분은 모두 자동화
- 사용자는 API 키 발급과 .env 파일 생성만 수행
