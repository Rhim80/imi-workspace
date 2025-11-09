# Google Calendar Skill - 설정 가이드

## ✅ 완료된 작업

### 1. gcalcli 설치 (완료)
```bash
pipx install gcalcli  # ✅ 설치 완료
```

### 2. Python 스크립트 생성 (완료)
- ✅ `get_events.py`: 오늘 일정 조회 (gcalcli 래퍼)
- ✅ `get_week_events.py`: 이번 주 일정 조회
- ✅ `search_events.py`: 키워드 검색
- ✅ `add_event.py`: 자연어 일정 등록

### 3. Skill 생성 (완료)
- ✅ `~/.claude/skills/google-calendar/SKILL.md`
- ✅ Skills README 업데이트
- ✅ Calendar README 업데이트

## ⚠️ 남은 작업 (사용자가 수동으로 진행)

### 1. gcalcli OAuth 인증 (필수)

**실행 방법:**
```bash
export PATH="$HOME/.local/bin:$PATH"
gcalcli init
```

**인증 과정:**
1. 명령어 실행 → 브라우저가 자동으로 열림
2. Google 계정으로 로그인
3. "Claude Code Calendar Integration" 앱 권한 승인
4. 완료 메시지 확인

**인증 완료 확인:**
```bash
gcalcli list  # 캘린더 목록이 표시되면 성공
```

### 2. 테스트 실행

**오늘 일정 조회:**
```bash
cd /Users/rhim/Projects/pkm/00-system/02-scripts/calendar
python3 get_events.py
```

**예상 출력:**
```
- **09:00** 팀 미팅
- **14:00** 프로젝트 리뷰
```

또는:
```
일정이 없습니다.
```

### 3. Claude Code Skill 테스트

Claude와 대화로 테스트:

```
"오늘 일정 뭐 있어?"
```

Claude가 자동으로 `google-calendar` Skill을 실행하여 일정을 보여줍니다.

## 📋 사용 가능한 명령어

### Claude와 대화 (Skill 자동 실행)

- "오늘 일정 알려줘"
- "이번 주 스케줄 뭐야?"
- "강릉 관련 일정 찾아줘"
- "내일 오후 3시에 미팅 잡아줘"

### 직접 스크립트 실행

```bash
# 오늘 일정
python3 /Users/rhim/Projects/pkm/00-system/02-scripts/calendar/get_events.py

# 이번 주 일정
python3 /Users/rhim/Projects/pkm/00-system/02-scripts/calendar/get_week_events.py

# 검색
python3 /Users/rhim/Projects/pkm/00-system/02-scripts/calendar/search_events.py "강릉"

# 일정 등록
python3 /Users/rhim/Projects/pkm/00-system/02-scripts/calendar/add_event.py "내일 오후 3시 회의"
```

### gcalcli 직접 사용

```bash
export PATH="$HOME/.local/bin:$PATH"

gcalcli agenda          # 오늘 일정
gcalcli calw            # 주간 캘린더
gcalcli calm            # 월간 캘린더
gcalcli search "강릉"   # 검색
```

## 🎯 PKM 통합

### Daily Note 자동 통합

`/daily-note` 실행 시 `get_events.py`가 자동으로 실행되어 `{{calendar_events}}` placeholder를 채웁니다.

### Weekly Review

Weekly Review 작성 시:
```bash
python3 get_week_events.py
```

## ⚠️ 문제 해결

### "Google Calendar 인증이 필요합니다"

**원인**: gcalcli OAuth 인증 미완료

**해결:**
```bash
export PATH="$HOME/.local/bin:$PATH"
gcalcli init
```

### "gcalcli가 설치되지 않았습니다"

**원인**: gcalcli 설치 안 됨 또는 PATH 문제

**해결:**
```bash
pipx install gcalcli
export PATH="$HOME/.local/bin:$PATH"
```

### 기존 Python API 스크립트 사용

gcalcli 인증이 안 될 경우 원본 스크립트 사용:
```bash
python3 /Users/rhim/Projects/pkm/00-system/02-scripts/calendar/get_events_original.py.backup
```

## 📚 참고 문서

- **Skill 정의**: `~/.claude/skills/google-calendar/SKILL.md`
- **스크립트 README**: `/Users/rhim/Projects/pkm/00-system/02-scripts/calendar/README.md`
- **Skills 목록**: `~/.claude/skills/README.md`
- **gcalcli 공식**: https://github.com/insanum/gcalcli

## 🔐 보안

- OAuth 토큰: `~/.gcalcli_oauth` (자동 생성, Git 제외)
- credentials.json: ✅ 이미 있음 (Git 제외)
- 본인 Google 계정만 접근 가능

---

**다음 단계**: `gcalcli init` 실행하여 인증을 완료하세요!
