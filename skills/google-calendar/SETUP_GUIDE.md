# Google Calendar Skill - 설정 가이드

> 5분 만에 Google Calendar를 Claude Code와 통합하세요!

## 📋 전체 설정 과정

1. ✅ Python 스크립트 설치 (이미 완료)
2. 🔧 gcalcli 설치 (5분)
3. 🔐 OAuth 인증 (3분)
4. ✅ 테스트 및 사용

---

## 1. ✅ Python 스크립트 설치 (이미 완료)

이미 다음 스크립트가 포함되어 있습니다:
```
skills/google-calendar/scripts/
├── get_events.py         # 오늘 일정 조회
├── get_week_events.py    # 이번 주 일정 조회
├── search_events.py      # 일정 검색
└── add_event.py          # 일정 추가
```

---

## 2. 🔧 gcalcli 설치

### Step 1: pipx 설치 확인

gcalcli는 pipx로 설치하는 것이 권장됩니다.

**pipx가 설치되어 있는지 확인:**
```bash
pipx --version
```

**출력 예시:**
```
1.2.0
```

**pipx가 없다면 설치:**
```bash
# macOS (Homebrew)
brew install pipx
pipx ensurepath

# Linux/WSL
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# 설치 후 터미널 재시작 또는:
source ~/.zshrc  # zsh 사용자
source ~/.bashrc # bash 사용자
```

### Step 2: gcalcli 설치

```bash
pipx install gcalcli
```

**예상 출력:**
```
  installed package gcalcli 4.4.0, installed using Python 3.11.5
  These apps are now globally available
    - gcalcli
done! ✨ 🌟 ✨
```

### Step 3: PATH 설정

gcalcli가 설치되면 `~/.local/bin`에 위치합니다. PATH를 영구적으로 설정하세요.

**자동 설정 (권장):**
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**zsh 사용자:**
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**bash 사용자:**
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Step 4: 설치 확인

```bash
gcalcli --version
```

**예상 출력:**
```
gcalcli v4.4.0 (Python 3.11.5)
```

---

## 3. 🔐 OAuth 인증

### Step 1: OAuth 인증 시작

```bash
gcalcli init
```

### Step 2: 브라우저 자동 실행

명령어를 실행하면 브라우저가 자동으로 열리고 Google 로그인 페이지가 나타납니다.

**브라우저가 열리지 않으면:**
- 터미널에 표시된 URL을 복사하여 브라우저에 붙여넣기

### Step 3: Google 계정 선택

1. 사용할 Google 계정을 선택합니다
2. "계정 선택" 화면에서 Calendar에 접근할 계정 클릭

### Step 4: 권한 승인

**"gcalcli에서 Google 계정에 액세스하려고 합니다"** 화면이 나타나면:

1. **권한 목록 확인:**
   - ✅ Google Calendar 이벤트 보기
   - ✅ Google Calendar 이벤트 편집

2. **"허용" 버튼 클릭**

### Step 5: 인증 완료 확인

**터미널에 돌아가서:**
```
Authentication successful!
```

**OAuth 토큰 파일 생성 확인:**
```bash
ls -la ~/.gcalcli_oauth
```

**출력 예시:**
```
-rw------- 1 username staff 1234 Oct 30 23:59 /Users/username/.gcalcli_oauth
```

---

## 4. ✅ 테스트 및 사용

### 테스트 1: 캘린더 목록 확인

```bash
gcalcli list
```

**예상 출력:**
```
owner  Calendar Name
-----  -------------
owner  rhim@example.com
```

### 테스트 2: 오늘 일정 확인

```bash
gcalcli agenda
```

**예상 출력:**
```
Thu Oct 31   10:00am  프로젝트 미팅
             02:00pm  팀 회의
```

**일정이 없다면:**
```
No Events Found...
```

### 테스트 3: Python 스크립트 실행

**워크스페이스로 이동:**
```bash
cd /path/to/imi-workspace
```

**오늘 일정 조회:**
```bash
cd skills/google-calendar/scripts
python3 get_events.py
```

**예상 출력:**
```
- **10:00** 프로젝트 미팅
- **14:00** 팀 회의
```

### 테스트 4: Claude Code Skill 테스트

**Claude Code를 시작하고:**
```
"오늘 일정 뭐 있어?"
```

**Claude가 자동으로 google-calendar skill을 실행하여 일정을 보여줍니다.**

---

## 🎯 사용 가능한 명령어

### 일상적인 대화로 사용

Claude와 자연스럽게 대화하세요:

```
"오늘 일정 알려줘"
"이번 주 스케줄 뭐야?"
"강릉 관련 일정 찾아줘"
"내일 오후 3시에 미팅 잡아줘"
```

### Python 스크립트 직접 실행

```bash
# 워크스페이스 루트에서
cd skills/google-calendar/scripts

# 오늘 일정
python3 get_events.py

# 이번 주 일정
python3 get_week_events.py

# 검색
python3 search_events.py "키워드"

# 일정 추가
python3 add_event.py "내일 오후 3시 회의"
```

### gcalcli 직접 사용

```bash
gcalcli agenda              # 오늘 일정
gcalcli calw                # 주간 캘린더 (색상 포함)
gcalcli calm                # 월간 캘린더
gcalcli search "키워드"      # 검색
gcalcli add "내일 10시 회의" # 빠른 추가
```

---

## ⚠️ 문제 해결

### 1. "command not found: gcalcli"

**원인:** PATH 설정이 안 됨

**해결:**
```bash
export PATH="$HOME/.local/bin:$PATH"
# 또는 터미널 재시작
```

**영구 해결:**
```bash
# zsh
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### 2. "Google Calendar 인증이 필요합니다"

**원인:** OAuth 인증 미완료 또는 토큰 만료

**해결:**
```bash
gcalcli init
```

### 3. "ModuleNotFoundError: No module named 'google'"

**원인:** Python Google API 라이브러리 미설치 (스크립트가 Google API를 직접 호출하는 경우)

**해결:**
```bash
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

**참고:** 현재 스크립트는 gcalcli를 래핑하므로 이 문제는 발생하지 않을 수 있습니다.

### 4. "Permission denied" (스크립트 실행 시)

**원인:** 실행 권한 없음

**해결:**
```bash
chmod +x skills/google-calendar/scripts/*.py
```

### 5. OAuth 토큰 재생성

토큰이 손상되었다면:
```bash
rm ~/.gcalcli_oauth
gcalcli init
```

---

## 🔐 보안 및 개인정보

### OAuth 토큰 저장 위치
```
~/.gcalcli_oauth
```

### 권한 범위
- ✅ 본인의 Google Calendar 읽기
- ✅ 본인의 Google Calendar 쓰기
- ❌ 다른 Google 서비스 접근 불가

### Git 보안
`.gitignore`에 다음을 추가하세요:
```
.gcalcli_oauth
```

### 권한 취소 방법
1. [Google 계정 보안 설정](https://myaccount.google.com/permissions) 접속
2. "gcalcli" 앱 찾기
3. "액세스 권한 삭제" 클릭

---

## 📚 참고 자료

### 공식 문서
- **gcalcli GitHub**: https://github.com/insanum/gcalcli
- **gcalcli 사용법**: `gcalcli --help`

### 내부 문서
- **Skill 정의**: `skills/google-calendar/SKILL.md`
- **스크립트 위치**: `skills/google-calendar/scripts/`

### 고급 사용법
```bash
# 특정 캘린더만 조회
gcalcli --calendar "Work" agenda

# 색상 없이 출력 (파싱용)
gcalcli --nocolor agenda

# 앞으로 7일간 일정
gcalcli agenda "7 days"

# 특정 날짜 범위
gcalcli agenda "2025-11-01" "2025-11-07"
```

---

## 🎉 완료!

이제 Google Calendar를 Claude Code와 함께 사용할 수 있습니다!

**다음 단계:**
1. `/daily-note`를 실행하여 Daily Note에 일정 자동 포함
2. "오늘 일정 뭐 있어?"로 대화형 사용
3. 필요에 따라 스크립트 커스터마이징

**피드백이나 문제가 있다면:**
- SKILL.md의 "에러 처리" 섹션 확인
- 또는 Claude에게 질문하세요!
