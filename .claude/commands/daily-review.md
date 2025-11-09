---
description: 어제와 오늘의 변경사항 분석 및 Daily Review 생성
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

어제와 오늘의 프로젝트 진행 상황을 분석하고 Daily Review를 생성합니다.

**수행할 작업:**

1. **어제 변경된 파일 찾기**
   ```bash
   cd /Users/rhim/Projects
   git log --since="yesterday" --name-only --pretty=format: | sort | uniq
   ```

2. **주요 프로젝트별 변경사항 분석**
   - `pkm/10-projects/12-education/`: 교육 사업 (GPTers, Insight Platform 등)
   - `pkm/10-projects/13-imi-work/`: IMI WORK 브랜드 (OSMU 시스템)
   - `pkm/10-projects/14-brand-identity/`: Brand Identity Builder 웹앱
   - `pkm/20-operations/21-cafe-operations/`: 카페 운영 (페어링, 커머스, 롯데마켓)
   - `pkm/20-operations/22-automation/`: n8n 자동화 시스템
   - `pkm/`: PKM 시스템 전반
   - `.claude/`: Claude 설정

3. **오늘의 Daily Note 열기 또는 생성**
   - `/daily-note` 커맨드 실행

4. **Telegram Inbox 수집 (NEW)**

   **Phase 1: Python으로 링크 수집 (무료)**
   ```bash
   cd /Users/rhim/Projects/pkm
   python3 00-system/02-scripts/telegram-collector.py --limit 20
   ```

   **동작:**
   - Telegram Bot API로 메시지 조회
   - 링크 포함 메시지 필터링
   - `00-inbox/raw/` 임시 저장
   - Claude API 호출 없음 (무료!)

   **Phase 2: Claude Code로 분석 (무료!)**
   - `00-inbox/raw/` 파일 읽기
   - URL 및 메모 추출
   - Claude Code로 요약 및 분류 제안
   - `00-inbox/YYYY-MM-DD_[제목].md` 최종 저장
   - raw 파일 정리

   **에러 처리:**
   - 환경변수 누락 시: `.env` 파일 확인 안내
   - 라이브러리 누락 시: `pip3 install --break-system-packages requests` 안내
   - 새 메시지 없을 시: "✨ No new messages" (정상)

5. **Todo 시스템 통합 분석**
   ```bash
   # active-todos.md 읽기
   cat pkm/40-personal/46-todos/active-todos.md
   ```

   **분석할 내용:**
   - Inbox에 있는 미처리 Todo 개수
   - 1주일 이상 된 Overdue Todo
   - 오늘 할 일로 지정된 Todo
   - 장기 프로젝트 중 2주 이상 업데이트 없는 것

6. **Daily Note에 다음 내용 추가:**

   ### 📊 어제 진행 상황
   - [프로젝트명]: [변경 내용 요약]

   ### 📥 Telegram Inbox (NEW)

   **Phase 1: Python 수집**
   - 총 메시지: [total]개
   - 링크 포함: [processed]개
   - raw 파일 저장: [files]개

   **Phase 2: Claude Code 분석**
   - 처리 완료: [processed]개
   - 실패: [failed]개

   **수집된 항목:**
   1. **[제목1]**
      - 분류: `[category_suggestion]`
      - 키워드: [keywords]
   2. **[제목2]**
      - 분류: `[category_suggestion]`
      - 키워드: [keywords]

   **처리 제안:**
   - [ ] `00-inbox/` 폴더에서 파일 확인
   - [ ] 각 파일을 제안된 폴더로 이동
   - [ ] 불필요한 항목 삭제

   **💰 비용**: $0.00 (완전 무료!)

   ### 📋 Todo 상태 체크
   - **미처리 Todo**: [Inbox 개수]개
   - **오늘 할 일**: [Today 개수]개
   - **지연 중**: [Overdue 개수]개 (⚠️ 1주일 이상)

   **오늘 처리 제안:**
   1. [High priority todo 1]
   2. [High priority todo 2]
   3. [오래된 todo 중 급한 것]

   ### 🎯 오늘 우선순위 제안
   1. [AI 분석 기반 우선순위]
   2. [미완료 작업 연속성]
   3. [프로젝트 마감일 고려]
   4. [Todo 시스템 기반 제안] ← NEW!

   ### 💡 인사이트
   - [패턴 발견]
   - [개선 기회]
   - [Todo 관리 패턴] ← NEW!

7. **사용자에게 확인 요청**
   - 우선순위 조정 필요 여부
   - 추가 컨텍스트 필요 여부
   - Todo 제안 수용 여부
   - Telegram Inbox 처리 시작 여부 ← NEW!
