---
name: google-calendar
description: Google Calendar 일정 조회, 검색, 등록. "일정", "스케줄", "캘린더" 등을 언급하면 자동 실행. Daily Note 작성, Weekly Review에 사용.
allowed-tools: Bash, Read
---

# Google Calendar Integration Skill

이 Skill은 gcalcli를 사용하여 Google Calendar와 통합합니다.

## ⚠️ 사전 준비

**첫 사용 시 OAuth 인증 필요:**
```bash
export PATH="$HOME/.local/bin:$PATH"
gcalcli init
```

브라우저에서 Google 계정으로 로그인하고 권한을 승인하세요.

## 📂 스크립트 위치

모든 스크립트는 다음 경로에 있습니다:
```
skills/google-calendar/scripts/
```

## 🎯 사용 시나리오 및 실행 방법

### 1. 오늘 일정 조회

**Trigger 키워드:**
- "오늘 일정 뭐 있어?"
- "오늘 스케줄 알려줘"
- "today's schedule"
- "오늘 뭐하지?"

**실행:**
```bash
cd skills/google-calendar/scripts && python3 get_events.py
```

**출력 예시:**
```
- **09:00** 팀 미팅
- **14:00** 프로젝트 리뷰 (@회의실 A)
- **종일** 휴가
```

### 2. 이번 주 일정 조회 (Weekly Review용)

**Trigger 키워드:**
- "이번 주 일정 알려줘"
- "이번 주 스케줄 뭐야?"
- "weekly schedule"
- "주간 일정 보여줘"

**실행:**
```bash
cd skills/google-calendar/scripts && python3 get_week_events.py
```

**출력 예시:**
```markdown
## 이번 주 일정

### Mon Oct 21
- **10:00** 프로젝트 미팅 (@Zoom)
- **14:00** 스터디 준비

### Tue Oct 22
- **15:00** 온라인 교육 논의
```

### 3. 일정 검색

**Trigger 키워드:**
- "강릉 관련 일정 찾아줘"
- "미팅 일정 검색해줘"
- "search calendar for [키워드]"
- "[키워드] 일정 언제야?"

**실행:**
```bash
cd skills/google-calendar/scripts && python3 search_events.py "강릉"
```

**출력 예시:**
```markdown
## 검색 결과

- **Mon Oct 21** 10:00 강릉 프로젝트 미팅 (@Zoom)
- **Wed Oct 23** 14:00 강릉 카페 브랜드 기획
```

### 4. 일정 등록

**Trigger 키워드:**
- "일정", "스케줄", "캘린더"
- 추가, 등록, 잡아줘

**실행:**
```bash
cd skills/google-calendar/scripts
python3 add_event.py "<캘린더>" "<제목>" "<날짜>" "<시간>" [지속시간(분)]
```

**예시:**
```bash
# 기본 (2.5시간 자동)
python3 add_event.py "AI" "HFK 1회차" "2025-12-06" "14:30"

# 지속 시간 지정
python3 add_event.py "AI" "팀 미팅" "2025-12-06" "14:30" "60"
```

**파라미터:**
- 캘린더: "AI", "Work", "개인 + 가족용", "Money"
- 제목: 일정 제목 (따옴표로 감싸기)
- 날짜: YYYY-MM-DD 형식
- 시간: HH:MM 형식 (24시간)
- 지속시간: 분 단위 (선택, 기본 150분 = 2.5시간)

**출력 예시:**
```
📅 일정 추가 중...
   캘린더: AI
   제목: HFK 1회차
   시작: 2025-12-06 14:30
   시간: 150분 (2.5시간)
✅ 일정이 추가되었습니다!
```

## 🔧 고급 기능 (gcalcli 직접 사용)

사용자가 더 복잡한 작업을 요청하면 gcalcli를 직접 호출하세요:

### 캘린더 뷰 (주간/월간)
```bash
export PATH="$HOME/.local/bin:$PATH"
gcalcli calw  # 주간 캘린더
gcalcli calm  # 월간 캘린더
```

### 일정 수정
```bash
gcalcli edit "강릉"  # "강릉" 포함 일정 수정
```

### 일정 삭제
```bash
gcalcli delete "테스트"  # "테스트" 포함 일정 삭제
```

### 날짜 범위 조회
```bash
gcalcli agenda "3 days"           # 앞으로 3일
gcalcli agenda "monday" "friday"  # 이번 주 월~금
```

## 📝 PKM 통합

### Daily Note (`/daily-note`)

Daily Note 생성 시 `get_events.py`가 자동으로 실행되어 `{{calendar_events}}` placeholder를 채웁니다.

**Daily Note 예시:**
```markdown
### 📅 스케줄

#### Google Calendar
- **10:00** 프로젝트 미팅 (@Zoom)
- **14:00** 스터디 준비
```

### Weekly Review

Weekly Review 작성 시 `get_week_events.py`를 사용하여 이번 주 일정을 요약합니다.

```bash
python3 get_week_events.py
```

### 프로젝트 미팅 검색

특정 프로젝트의 미팅 일정을 찾을 때:
```bash
python3 search_events.py "프로젝트명"
```

## ⚠️ 에러 처리

### "Google Calendar 인증이 필요합니다"
**해결:**
```bash
export PATH="$HOME/.local/bin:$PATH"
gcalcli init
```

### "gcalcli가 설치되지 않았습니다"
**해결:**
```bash
pipx install gcalcli
```

## 🎯 사용 예시

**대화형 사용:**
```
사용자: "오늘 일정 뭐 있어?"
Claude: (google-calendar skill 자동 실행)
- **10:00** 프로젝트 미팅 (@Zoom)
- **14:00** 스터디 준비
```

```
사용자: "강릉 관련 미팅 언제야?"
Claude: (google-calendar skill 자동 실행 - search)
## 검색 결과
- **Mon Oct 21** 10:00 강릉 프로젝트 미팅 (@Zoom)
```

```
사용자: "AI 캘린더에 내일 오후 3시에 클라이언트 미팅 잡아줘"
Claude: (google-calendar skill 자동 실행 - add)
📅 일정 추가 중...
   캘린더: AI
   제목: 클라이언트 미팅
   시작: 2025-11-01 15:00
   시간: 150분 (2.5시간)
✅ 일정이 추가되었습니다!
```

## 💡 스크립트 선택 가이드

| 사용자 요청 | 실행할 스크립트 | 커맨드 |
|-----------|--------------|--------|
| "오늘 일정" | get_events.py | `python3 get_events.py` |
| "이번 주 일정" | get_week_events.py | `python3 get_week_events.py` |
| "키워드 검색" | search_events.py | `python3 search_events.py "키워드"` |
| "일정 추가" | add_event.py | `python3 add_event.py "캘린더" "제목" "날짜" "시간" [분]` |
| "주간 캘린더 뷰" | gcalcli 직접 | `gcalcli calw` |
| "월간 캘린더 뷰" | gcalcli 직접 | `gcalcli calm` |

## 🔐 보안

- OAuth 토큰은 `~/.gcalcli_oauth`에 저장됩니다.
- 이 파일은 `.gitignore`에 포함되어야 합니다.
- 본인 Google 계정만 접근 가능합니다.
