# Skills

> Claude Code와 외부 서비스를 통합하는 기능 모음

## 🎯 사용 가능한 Skills

### ✅ Google Calendar (gcalcli 기반)

**상태**: 설정 가이드 완료 ✨

Google Calendar를 Claude와 통합하여 대화만으로 일정 관리:
- "오늘 일정 뭐 있어?"
- "이번 주 스케줄 알려줘"
- "강릉 관련 일정 찾아줘"
- "내일 오후 3시 미팅 잡아줘"

**설정 방법**: [google-calendar/SETUP_GUIDE.md](./google-calendar/SETUP_GUIDE.md) (5분 소요)

**특징**:
- ✅ gcalcli 기반 (빠르고 안정적)
- ✅ OAuth 인증 (Google Cloud Console 불필요)
- ✅ Python 스크립트 포함 (커스터마이징 가능)
- ✅ Daily Note 자동 통합

**시작하기**:
```bash
# 1. gcalcli 설치
pipx install gcalcli

# 2. OAuth 인증
gcalcli init

# 3. Claude와 대화
"오늘 일정 알려줘"
```

자세한 내용: [google-calendar/README.md](./google-calendar/README.md)

---

## 📖 Skills란?

Skills는 Claude Code를 외부 서비스와 연결하여 확장하는 기능입니다.

### Skills vs Commands

| 구분 | Skills | Commands |
|------|--------|----------|
| **목적** | 외부 서비스 통합 | 내부 워크플로우 자동화 |
| **예시** | Google Calendar, Notion | `/daily-note`, `/setup-workspace` |
| **위치** | `skills/` | `.claude/commands/` |
| **설정** | OAuth, API 키 필요 | 설정 불필요 (즉시 사용) |

---

## 🔮 추가 가능한 Skills 예시

**생산성:**
- **Notion** - Notion 페이지 생성/조회
- **Todoist** - 할 일 관리
- **Trello** - 보드 및 카드 관리

**커뮤니케이션:**
- **Slack** - 메시지 전송/채널 조회
- **Discord** - 봇 통합
- **Telegram** - 메시지 전송

**개발:**
- **GitHub** - 이슈/PR 관리
- **GitLab** - CI/CD 통합

**데이터:**
- **Airtable** - 데이터베이스 조회/수정
- **Google Sheets** - 스프레드시트 읽기/쓰기

---

## 🛠 커스텀 Skills 추가

자신만의 스킬을 추가하려면:

### 1. 폴더 생성
```bash
mkdir -p skills/skill-name/scripts
```

### 2. SKILL.md 작성
```markdown
---
name: skill-name
description: 스킬 설명 및 트리거 키워드
allowed-tools: Bash, Read
---

# Skill Name

## 사용 방법
...
```

### 3. 스크립트 작성 (선택)
```bash
# skills/skill-name/scripts/main.py
# 실제 기능 구현
```

### 4. README 작성
```markdown
# Skill Name

## 설정 가이드
...
```

### 참고 자료
- **예시**: [google-calendar/](./google-calendar/) 폴더 구조 참고
- **공식 문서**: [Claude Code Skills 가이드](https://docs.claude.com)

---

## 💡 Skills 사용 팁

### 자동 트리거

Skills는 대화 중 키워드를 감지하면 자동으로 실행됩니다:
```
사용자: "오늘 일정 뭐 있어?"
→ google-calendar skill 자동 실행
```

### 명시적 호출

특정 skill을 명시적으로 호출할 수도 있습니다:
```
사용자: "google-calendar skill로 이번 주 일정 조회해줘"
```

### PKM 통합

Skills를 `/daily-note`, `/weekly-review` 등의 commands와 결합하여 자동화:
```markdown
## Daily Note Template

### 📅 스케줄
{{calendar_events}}  ← google-calendar skill이 자동으로 채움
```

---

## ⚠️ 선택적 기능

Skills는 **선택적**입니다. 필요한 기능만 설정하세요.

- ✅ **google-calendar**: 일정 관리가 중요한 경우
- 🔜 **기타 skills**: 필요에 따라 추가

---

## 🎉 기여하기

새로운 skill을 만들었다면 공유해주세요!

1. `skills/your-skill/` 폴더 생성
2. SETUP_GUIDE.md 작성 (상세한 설정 방법)
3. SKILL.md 작성 (트리거 및 사용법)
4. README.md 작성 (개요 및 빠른 시작)

**좋은 Skill의 조건:**
- ✅ 상세한 설정 가이드 (초보자도 따라할 수 있게)
- ✅ 명확한 트리거 키워드 (자동 실행 조건)
- ✅ 실용적인 사용 예시
- ✅ 트러블슈팅 섹션
