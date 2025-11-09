---
name: google-calendar
description: Google Calendar 일정 조회, 검색, 등록. "일정", "스케줄", "캘린더" 등을 언급하면 자동 실행. Daily Note 작성, Weekly Review에 사용.
allowed-tools: Bash, Read
---

# Google Calendar Integration Skill

이 Skill은 **gcalcli**를 사용하여 Google Calendar와 통합합니다.

## ⚠️ 중요 규칙

### 일정 제목 작성 규칙
**제목에 날짜/시간 절대 포함 금지**

- ❌ "2025-11-13 13:00 커피챗"
- ❌ "11월 13일 알파브라더스"
- ❌ "2025-12-06 14:30 HFK 1회차"
- ✅ "알파브라더스 채중규 대표 커피챗"
- ✅ "HFK 겨울시즌 1회차: AI 파트너 만들기"

**이유**: 날짜와 시간은 Google Calendar의 메타데이터로 관리되며, 제목에 중복 포함 시 혼란을 야기합니다.

---

## 🎯 주요 기능

### 1. 일정 조회

**사용 도구**: `gcalcli agenda`

#### 기본 조회
```bash
# 오늘 일정
gcalcli agenda

# 특정 날짜 일정
gcalcli agenda 2025-11-13

# 특정 기간 일정
gcalcli agenda 2025-11-13 2025-11-15

# 특정 캘린더만 조회
gcalcli agenda --calendar "Work"
gcalcli agenda --calendar "개인+가족용"
gcalcli agenda --calendar "Money"

# 여러 캘린더 동시 조회
gcalcli agenda --calendar "Work" --calendar "개인+가족용"
```

#### TSV 형식 출력
```bash
# 파싱하기 쉬운 TSV 형식
gcalcli agenda --tsv 2025-11-13 2025-11-14

# 출력 형식:
# start_date	start_time	end_date	end_time	title
```

#### 상세 정보 포함
```bash
# 일정의 모든 정보 표시
gcalcli agenda --details all 2025-11-13 2025-11-14

# 출력 내용:
# - Calendar name
# - Link (Google Calendar URL)
# - Location
# - Duration
# - Description
```

---

### 2. 일정 검색

**사용 도구**: `gcalcli search`

```bash
# 기본 검색
gcalcli search "검색어"

# 특정 캘린더에서만 검색
gcalcli search "HFK" --calendar "AI"

# 예시
gcalcli search "알파브라더스" --calendar "Work"
gcalcli search "커피챗"
gcalcli search "강릉"
```

---

### 3. 일정 추가

**형식**:
```bash
gcalcli add --calendar "캘린더명" \
  --when "YYYY-MM-DD HH:MM" \
  --duration 분 \
  --title "제목" \
  --where "장소" \
  --description "설명"
```

**필수 규칙**:
- `--title`: **날짜/시간 포함 금지**
- `--when`: ISO 형식 날짜 + 시간
- `--duration`: 분 단위 (기본값 없음, 반드시 지정)

**예시**:
```bash
# 커피챗 일정 (1시간)
gcalcli add --calendar "Work" \
  --when "2025-11-13 13:00" \
  --duration 60 \
  --title "알파브라더스 채중규 대표 커피챗" \
  --where "가양역, 강서구 공항대로 45길 71 3층" \
  --description "알파브라더스 채중규 대표님과 커피챗"

# 강의 일정 (2.5시간)
gcalcli add --calendar "AI" \
  --when "2025-12-06 14:30" \
  --duration 150 \
  --title "HFK 겨울시즌 1회차: AI 파트너 만들기"

# 미팅 일정 (1.5시간)
gcalcli add --calendar "Work" \
  --when "2025-12-10 10:00" \
  --duration 90 \
  --title "강릉 프로젝트 2차 미팅" \
  --where "zoom"
```

---

### 4. 일정 수정

**사용 도구**: `gcalcli edit`

```bash
# 대화형 편집
gcalcli edit "검색어"

# 예시: "강릉" 포함된 일정 수정
gcalcli edit "강릉"
```

**⚠️ 제약**: 대화형 프롬프트로 Claude Code 환경에서 제한적

**해결책**: 기존 일정 삭제 후 새로 생성
```bash
# 1. 기존 일정 삭제
gcalcli delete "검색어" --iamaexpert

# 2. 새 일정 생성
gcalcli add --calendar "Work" --when "..." --title "..."
```

---

### 5. 일정 삭제

**사용 도구**: `gcalcli delete`

#### 기본 삭제 (대화형)
```bash
gcalcli delete "검색어"
```

#### 자동 삭제 (권장)
```bash
# --iamaexpert: 확인 없이 자동 삭제
gcalcli delete "검색어" --iamaexpert

# 특정 캘린더에서만 삭제
gcalcli delete "검색어" --calendar "Work" --iamaexpert
```

**예시**:
```bash
# 잘못 생성한 일정 삭제
gcalcli delete "2025-11-13 알파브라더스" --iamaexpert

# 특정 일정만 삭제
gcalcli delete "알파브라더스 커피챗" --calendar "Work" --iamaexpert
```

**⚠️ 주의**: `--iamaexpert` 옵션은 확인 없이 즉시 삭제하므로 신중히 사용

---

## 📝 PKM 통합

### Daily Note (`/daily-note`)

Daily Note 생성 시 Google Calendar 일정을 자동으로 가져옵니다.

**동작 방식**:
1. `gcalcli agenda --calendar "Work" --calendar "개인+가족용" --tsv` 실행
2. TSV 출력을 파싱하여 Markdown 리스트로 변환
3. Daily Note 템플릿의 `{{calendar_events}}` placeholder에 삽입

**Daily Note 예시**:
```markdown
### 📅 스케줄

#### Google Calendar (일정)
- **13:00-14:00**: 알파브라더스 채중규 대표 커피챗
- **14:30-17:00**: HFK 1회차 강의

#### 💰 알림 (대출/카드)
일정이 없습니다.
```

### Weekly Review

```bash
# 이번 주 일정 조회
gcalcli agenda "monday" "sunday"

# 주간 캘린더 뷰
gcalcli calw

# 월간 캘린더 뷰
gcalcli calm
```

---

## 💡 캘린더 종류

### 사용 가능한 캘린더
1. **Work**: 업무 일정 (미팅, 강의, 프로젝트)
2. **AI**: AI 교육 관련 (GPTers, HFK, 강의)
3. **개인+가족용**: 개인 및 가족 일정
4. **Money**: 금융 알림 (대출, 카드 결제)

### 캘린더 목록 확인
```bash
gcalcli list
```

### 특정 캘린더 지정
```bash
# 단일 캘린더
gcalcli agenda --calendar "Work"

# 여러 캘린더
gcalcli agenda --calendar "Work" --calendar "AI"
```

---

## ⚠️ 사전 준비

### gcalcli 설치
```bash
pipx install gcalcli
```

### OAuth 인증 (첫 사용 시)
```bash
gcalcli init
```

브라우저에서 Google 계정으로 로그인하고 권한을 승인하세요.

**인증 토큰 저장 위치**:
```
~/.gcalcli_oauth
```

---

## 🔧 트러블슈팅

### 1. "Google Calendar 인증이 필요합니다"
**해결**:
```bash
gcalcli init
```

### 2. "gcalcli가 설치되지 않았습니다"
**해결**:
```bash
pipx install gcalcli
pipx ensurepath
export PATH="$HOME/.local/bin:$PATH"
```

### 3. 대화형 프롬프트 문제
**문제**: `edit`, `delete` 명령어가 대화형 입력 요구

**해결**:
```bash
# --iamaexpert 옵션 사용 (확인 없이 실행)
gcalcli delete "검색어" --iamaexpert
```

### 4. 잘못된 제목으로 생성된 일정
**문제**: 제목에 날짜/시간 포함

**해결**:
```bash
# 1. 잘못된 일정 삭제
gcalcli delete "2025-11-13 13:00 커피챗" --iamaexpert

# 2. 올바른 제목으로 재생성
gcalcli add --calendar "Work" \
  --when "2025-11-13 13:00" \
  --duration 60 \
  --title "알파브라더스 커피챗"
```

---

## 🔐 보안

- OAuth 토큰은 `~/.gcalcli_oauth`에 저장됩니다
- 이 파일은 `.gitignore`에 포함되어야 합니다
- 본인 Google 계정만 접근 가능합니다

---

## 📚 참고 자료

- gcalcli 공식 문서: https://github.com/insanum/gcalcli
- 모든 명령어: `gcalcli --help`
- 특정 명령어 도움말: `gcalcli add --help`

---

## 📝 Version History

- **2025-11-09**: 제목 규칙 강화, gcalcli 직접 사용법 추가, --iamaexpert 옵션 명시
- **2025-10-31**: Daily Note 통합 추가
- **2025-10-22**: 초기 작성
