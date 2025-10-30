# Google Calendar Skill

> Google Calendar를 Claude Code와 통합하여 대화만으로 일정 관리

## 🎯 주요 기능

- ✅ **오늘 일정 조회**: "오늘 일정 뭐 있어?"
- ✅ **이번 주 일정**: "이번 주 스케줄 알려줘"
- ✅ **일정 검색**: "강릉 관련 일정 찾아줘"
- ✅ **일정 추가**: "내일 오후 3시 미팅 잡아줘"

## ⚡ 빠른 시작

### 1. 설정 (5분 소요)

**전체 설정 가이드는 [SETUP_GUIDE.md](./SETUP_GUIDE.md)를 참고하세요!**

**요약:**
```bash
# 1. gcalcli 설치
pipx install gcalcli

# 2. PATH 설정
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# 3. OAuth 인증
gcalcli init
# → 브라우저가 열리면 Google 계정으로 로그인하고 권한 승인
```

### 2. 테스트

```bash
# 캘린더 목록 확인
gcalcli list

# 오늘 일정 확인
gcalcli agenda
```

### 3. Claude Code에서 사용

```
"오늘 일정 뭐 있어?"
```

Claude가 자동으로 일정을 조회하여 보여줍니다!

---

## 📖 사용 방법

### 대화형 사용 (권장)

Claude와 자연스럽게 대화하세요:

```
사용자: "오늘 일정 알려줘"
Claude:
- **10:00** 프로젝트 미팅
- **14:00** 팀 회의
```

```
사용자: "이번 주 스케줄 뭐야?"
Claude:
## 이번 주 일정
### Mon Oct 31
- **10:00** 프로젝트 미팅 (@Zoom)
...
```

```
사용자: "강릉 관련 일정 찾아줘"
Claude:
## 검색 결과
- **Mon Oct 31** 10:00 강릉 프로젝트 미팅
- **Wed Nov 02** 14:00 강릉 카페 브랜드 기획
```

```
사용자: "내일 오후 3시에 클라이언트 미팅 잡아줘"
Claude:
✅ 일정이 등록되었습니다!
   제목: 클라이언트 미팅
   시작: 2025-11-01 15:00
```

### Python 스크립트 직접 실행

```bash
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
gcalcli agenda       # 오늘 일정
gcalcli calw         # 주간 캘린더
gcalcli calm         # 월간 캘린더
gcalcli search "키워드"  # 검색
```

---

## 📂 폴더 구조

```
skills/google-calendar/
├── README.md           # 이 파일 (개요)
├── SETUP_GUIDE.md      # 상세 설정 가이드
├── SKILL.md            # Claude Code Skill 정의
└── scripts/
    ├── get_events.py      # 오늘 일정 조회
    ├── get_week_events.py # 이번 주 일정 조회
    ├── search_events.py   # 일정 검색
    └── add_event.py       # 일정 추가
```

---

## 🔧 문제 해결

### "command not found: gcalcli"

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### "Google Calendar 인증이 필요합니다"

```bash
gcalcli init
```

### 더 많은 문제 해결

**상세한 트러블슈팅은 [SETUP_GUIDE.md](./SETUP_GUIDE.md)의 "문제 해결" 섹션을 참고하세요.**

---

## 📚 더 알아보기

- **[SETUP_GUIDE.md](./SETUP_GUIDE.md)** - 전체 설정 가이드 (설치부터 OAuth까지)
- **[SKILL.md](./SKILL.md)** - Skill 상세 사용법 (트리거 키워드, 고급 기능)
- **[gcalcli 공식 문서](https://github.com/insanum/gcalcli)** - gcalcli 고급 사용법

---

## 🎉 빠른 활용 팁

### Daily Note 통합

`/daily-note` 명령어를 사용하면 자동으로 오늘 일정이 포함됩니다.

### Weekly Review

주간 회고를 작성할 때:
```
"이번 주 일정 요약해줘"
```

### 프로젝트 미팅 추적

특정 프로젝트의 모든 미팅 기록:
```
"[프로젝트명] 관련 일정 찾아줘"
```

---

## ⚠️ 선택적 기능

이 기능은 **선택적**입니다. Google Calendar 통합이 필요하지 않다면 설정하지 않아도 됩니다.

**설정을 원한다면 [SETUP_GUIDE.md](./SETUP_GUIDE.md)를 따라 진행하세요!**
