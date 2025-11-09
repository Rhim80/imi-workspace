# Setup Google Calendar - 대화형 설정 마법사

Google Calendar를 Claude Code와 연결하는 전체 과정을 자동으로 진행합니다.

## 🎯 수행 작업

### Phase 1: 자동 설치 (Claude가 실행)
1. ✅ pipx 설치 확인 및 설치 (필요 시)
2. ✅ gcalcli 설치
3. ✅ PATH 설정 확인 및 추가 (필요 시)
4. ✅ 설치 확인 테스트

### Phase 2: OAuth 인증 (사용자 필요)
1. 🔐 OAuth 인증 실행 안내
2. 🌐 브라우저 로그인 가이드
3. ✅ 인증 완료 확인

### Phase 3: 테스트 및 완료
1. 📋 캘린더 목록 조회
2. 🎉 완료 메시지
3. 💡 사용 가능한 기능 안내

---

## 📋 실행 순서

### Step 1: 환영 메시지

```
안녕하세요! Google Calendar 설정을 시작합니다. 🎉

**소요 시간:** 약 5분
**필요한 것:** Google 계정

이 과정에서 대부분은 자동으로 진행되고,
OAuth 인증만 직접 해주시면 됩니다.

준비되셨으면 'start' 또는 '시작'이라고 입력해주세요.
```

---

### Step 2: 자동 설치 시작

사용자가 'start' 입력하면:

```
좋아요! 자동 설치를 시작합니다...

**Phase 1: pipx 설치 확인**
```

**2-1. pipx 확인:**
```bash
which pipx
```

**결과에 따라:**
- **있음**: "✅ pipx가 이미 설치되어 있습니다."
- **없음**: pipx 자동 설치 진행

**2-2. pipx 자동 설치 (없을 경우):**

**macOS (Homebrew):**
```bash
# Homebrew 확인
which brew

# Homebrew 있으면
brew install pipx
pipx ensurepath

# Homebrew 없으면
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

**Linux/WSL:**
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

설치 후:
```bash
# 현재 세션에 PATH 적용
export PATH="$HOME/.local/bin:$PATH"

# pipx 버전 확인
pipx --version
```

결과 출력: "✅ pipx 설치 완료! (버전: X.X.X)"

---

### Step 3: gcalcli 설치

```
**Phase 2: gcalcli 설치**
```

**3-1. gcalcli 확인:**
```bash
which gcalcli
```

**결과에 따라:**
- **있음**: "✅ gcalcli가 이미 설치되어 있습니다."
- **없음**: gcalcli 자동 설치 진행

**3-2. gcalcli 자동 설치 (없을 경우):**
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

설치 후 확인:
```bash
gcalcli --version
```

결과 출력: "✅ gcalcli 설치 완료! (버전: X.X.X)"

---

### Step 4: PATH 설정 확인 및 추가

```
**Phase 3: PATH 설정 확인**
```

**4-1. 현재 PATH 확인:**
```bash
echo $PATH | grep -q "$HOME/.local/bin" && echo "YES" || echo "NO"
```

**4-2. Shell 확인:**
```bash
echo $SHELL
```

**4-3. PATH 추가 (필요 시):**

**zsh 사용자:**
```bash
# .zshrc에 PATH 추가 (중복 체크)
grep -q 'export PATH="$HOME/.local/bin:$PATH"' ~/.zshrc || echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc

# 현재 세션 적용
export PATH="$HOME/.local/bin:$PATH"

# 확인
source ~/.zshrc
```

**bash 사용자:**
```bash
# .bashrc에 PATH 추가 (중복 체크)
grep -q 'export PATH="$HOME/.local/bin:$PATH"' ~/.bashrc || echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# 현재 세션 적용
export PATH="$HOME/.local/bin:$PATH"

# 확인
source ~/.bashrc
```

결과 출력: "✅ PATH 설정 완료!"

---

### Step 5: OAuth 인증 안내 (사용자 직접)

```
✅ 자동 설치가 완료되었습니다!

이제 **OAuth 인증**이 필요합니다.
이 부분은 직접 해주셔야 합니다. 🔐

**다음 명령어를 터미널에 복사해서 실행해주세요:**

gcalcli init

**실행하면:**
1. 브라우저가 자동으로 열립니다
2. Google 계정을 선택하세요
3. "gcalcli가 Google 계정에 액세스하려고 합니다" 화면이 나타나면
4. "허용" 버튼을 클릭하세요
5. "Authentication successful!" 메시지가 터미널에 나타나면 완료!

**브라우저가 자동으로 열리지 않으면:**
- 터미널에 표시된 URL을 복사해서 브라우저에 붙여넣으세요

OAuth 인증을 완료하셨으면 '완료' 또는 'done'이라고 입력해주세요.
```

---

### Step 6: 인증 확인 및 테스트

사용자가 '완료' 입력하면:

```
좋아요! 인증이 완료되었는지 확인해볼게요.

**OAuth 토큰 파일 확인:**
```

```bash
ls -la ~/.gcalcli_oauth
```

**결과에 따라:**
- **파일 있음**: "✅ OAuth 토큰이 생성되었습니다!"
- **파일 없음**: "❌ 인증이 완료되지 않았습니다. 다시 시도해주세요."

**캘린더 목록 조회 테스트:**
```bash
gcalcli list
```

**예상 출력:**
```
owner  Calendar Name
-----  -------------
owner  your-email@gmail.com
```

결과 출력: "✅ 캘린더 연결 성공!"

**오늘 일정 조회 테스트:**
```bash
cd .claude/skills/google-calendar/scripts
python3 get_events.py
```

결과 출력 (있으면 일정, 없으면 "일정이 없습니다.")

---

### Step 7: 완료 및 안내

```
🎉 축하합니다! Google Calendar 설정이 완료되었습니다!

**이제 사용 가능한 기능:**

1. **대화형 일정 조회**
   - "오늘 일정 뭐 있어?"
   - "이번 주 스케줄 알려줘"
   - "강릉 관련 일정 찾아줘"

2. **일정 추가**
   - "내일 오후 3시에 미팅 잡아줘"
   - "다음 주 월요일 10시 회의 등록"

3. **Daily Note 자동 통합**
   - /daily-note 실행 시 자동으로 오늘 일정 포함

4. **직접 스크립트 실행**
   cd .claude/skills/google-calendar/scripts
   python3 get_events.py        # 오늘 일정
   python3 get_week_events.py   # 이번 주 일정
   python3 search_events.py "키워드"  # 검색

5. **gcalcli 직접 사용**
   gcalcli agenda    # 오늘 일정
   gcalcli calw      # 주간 캘린더 (색상 포함)
   gcalcli calm      # 월간 캘린더

**더 알아보기:**
- 상세 가이드: .claude/skills/google-calendar/SETUP_GUIDE.md
- 사용법: .claude/skills/google-calendar/SKILL.md

**테스트해보세요:**
"오늘 일정 뭐 있어?"
```

---

## ⚠️ 오류 처리

### OAuth 인증 실패

**증상:** "Authentication failed" 또는 토큰 파일 없음

**해결:**
1. 기존 토큰 삭제: `rm ~/.gcalcli_oauth`
2. 다시 시도: `gcalcli init`
3. 브라우저에서 정확히 "허용" 클릭 확인

### "command not found: gcalcli"

**원인:** PATH 설정 안됨 또는 설치 실패

**해결:**
```bash
# PATH 수동 설정
export PATH="$HOME/.local/bin:$PATH"

# gcalcli 재설치
pipx install --force gcalcli
```

### pipx 설치 실패

**원인:** Python 또는 pip 미설치

**해결:**
```bash
# macOS
brew install python3

# Linux/WSL
sudo apt-get install python3 python3-pip
```

### 브라우저가 열리지 않음

**해결:**
1. 터미널에 표시된 URL 복사
2. 브라우저에 수동으로 붙여넣기
3. 로그인 및 권한 승인

---

## 🔄 재실행

설정을 다시 하고 싶다면:

```bash
# 기존 토큰 삭제
rm ~/.gcalcli_oauth

# 커맨드 재실행
/setup-google-calendar
```

---

## 📚 참고 자료

- **SETUP_GUIDE.md**: 상세 설치 가이드 (수동 설치 시)
- **SKILL.md**: 고급 기능 및 트리거 키워드
- **README.md**: 빠른 시작 가이드
