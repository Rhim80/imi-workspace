# IMI Workspace

> AI-powered workspace for non-coders
> 비개발자를 위한 AI 작업 환경

## What is IMI Workspace?

Claude Code와 Johnny Decimal 시스템을 결합한 실전 PKM 워크스페이스입니다.
15년 F&B 경력 + AI 활용 전문가의 실제 시스템을 기반으로 만들어졌습니다.

## Quick Start

1. Clone this repository
   ```bash
   git clone https://github.com/Rhim80/imi-workspace.git
   cd imi-workspace
   ```

2. Open in Claude Code

3. Start using:
   - Create your first daily note
   - Organize your projects
   - Build your knowledge base

## Philosophy

1. **AI amplifies thinking**, not just writing
2. **File system = AI memory**
3. **Structure enables creativity**
4. **Iteration over perfection**
5. **Immediate usability**

## Folder Structure

Johnny Decimal 시스템 기반 - **AI가 이해하기 쉬운 구조**

```
imi-workspace/
├── 00-inbox/          # 빠른 캡처 공간
├── 00-system/         # 시스템 설정 및 템플릿
│   ├── 01-templates/
│   └── 02-scripts/
├── 10-projects/       # 활성 프로젝트 (시한부)
│   ├── 11-xxx/        # 프로젝트 1
│   ├── 12-xxx/        # 프로젝트 2
│   └── 13-xxx/        # 프로젝트 3
├── 20-operations/     # 비즈니스 운영 (지속적)
│   ├── 21-xxx/        # 운영 업무 1
│   └── 22-xxx/        # 운영 업무 2
├── 30-knowledge/      # 지식 아카이브
│   ├── 31-xxx/        # 지식 분야 1
│   └── 32-xxx/        # 지식 분야 2
├── 40-personal/       # 개인 노트
│   ├── 41-daily/      # Daily Notes
│   ├── 42-weekly/     # Weekly Reviews
│   └── 46-todos/      # 할 일 관리
├── 50-resources/      # 참고 자료
└── 90-archive/        # 완료/중단 항목
```

### 📂 Johnny Decimal 시스템 이해하기

#### 기본 원칙
- **10단위 = 카테고리** (예: 10-projects, 20-operations)
- **1단위 = 하위 폴더** (예: 11-xxx, 12-xxx)
- **명확한 숫자 = 빠른 탐색**

#### 네이밍 규칙
```
[숫자]-[설명적-이름]

예시:
✅ 11-imi-cafe-project
✅ 21-daily-store-operations
✅ 31-business-frameworks
❌ my-project (숫자 없음)
❌ 11project (하이픈 없음)
```

### 각 카테고리 상세 설명

#### 00-inbox (빠른 캡처)
**용도**: 생각나는 즉시 기록
- 아이디어
- 링크
- 빠른 메모

**관리**: 주 1회 정리하여 적절한 폴더로 이동

---

#### 00-system (시스템 설정)
**용도**: 워크스페이스 설정 및 템플릿
- `01-templates/` - 재사용 가능한 템플릿
- `02-scripts/` - 자동화 스크립트

**수정 가능**: 필요에 따라 템플릿 커스터마이징

---

#### 10-projects (시한부 프로젝트)
**용도**: 시작일과 종료일이 있는 프로젝트
**특징**: 완료되면 90-archive로 이동

**하위 폴더 생성 예시**:
```
10-projects/
├── 11-website-redesign/
│   ├── README.md
│   ├── requirements.md
│   └── progress.md
├── 12-product-launch/
└── 13-marketing-campaign/
```

**네이밍 팁**:
- 11~19 사이 숫자 사용
- 프로젝트명은 구체적으로
- 완료되면 `90-archive/`로 이동

---

#### 20-operations (지속적 운영)
**용도**: 반복적이고 지속적인 업무
**특징**: 종료일 없이 계속 유지

**하위 폴더 생성 예시**:
```
20-operations/
├── 21-daily-store-management/
│   ├── opening-checklist.md
│   └── closing-checklist.md
├── 22-team-management/
│   ├── onboarding.md
│   └── training-materials/
└── 23-customer-service/
```

**네이밍 팁**:
- 21~29 사이 숫자 사용
- 반복적 업무 중심
- 프로세스 문서화

---

#### 30-knowledge (지식 아카이브)
**용도**: 검증된 지식과 학습 자료
**특징**: 재사용 가능한 인사이트

**하위 폴더 생성 예시**:
```
30-knowledge/
├── 31-business-frameworks/
│   ├── lean-canvas.md
│   └── okr-system.md
├── 32-technical-guides/
│   ├── api-integration.md
│   └── automation-workflows.md
└── 33-industry-insights/
```

**네이밍 팁**:
- 31~39 사이 숫자 사용
- 주제별로 분류
- 검증된 내용만 저장

---

#### 40-personal (개인 노트)
**용도**: 개인적인 기록과 회고
**특징**: 날짜 기반 파일명

**구조**:
```
40-personal/
├── 41-daily/
│   ├── 2025-10-28.md
│   ├── 2025-10-29.md
│   └── 2025-10-30.md
├── 42-weekly/
│   ├── 2025-W44.md
│   └── 2025-W45.md
└── 46-todos/
    └── active-todos.md
```

**파일명 규칙**:
- Daily: `YYYY-MM-DD.md`
- Weekly: `YYYY-WXX.md`

---

#### 50-resources (참고 자료)
**용도**: 외부 자료 저장
- PDF, 이미지
- 다운로드한 문서
- 참고 링크 모음

---

#### 90-archive (아카이브)
**용도**: 완료/중단된 프로젝트
**관리**: 분기별로 정리

**구조 예시**:
```
90-archive/
├── 2024-Q4/
│   ├── 11-website-redesign/
│   └── 12-product-launch/
└── 2025-Q1/
```

## Templates

`00-system/01-templates/`에서 사용 가능한 템플릿:

- **daily-note-template.md** - 매일 작성하는 노트
- **weekly-review-template.md** - 주간 회고
- **Project Template.md** - 새 프로젝트 시작
- **pr-faq-template.md** - Amazon Working Backwards PR/FAQ 문서

## Slash Commands

`.claude/commands/`에서 사용 가능한 커맨드:

### 📝 Daily Workflow
- `/daily-note` - 오늘 날짜의 Daily Note 생성/열기
- `/daily-review` - 어제와 오늘 변경사항 분석
- `/weekly-synthesis` - 주간 회고 생성
- `/todo` / `/todos` - 할 일 관리

### 🎯 Project Management
- `/working-backwards-pr` - Amazon Working Backwards PR/FAQ 문서 생성 (대화형)
- `/generate-roadmap` - PR/FAQ 기반 역순 로드맵 생성

### 💡 Thinking & Ideas
- `/thinking-partner` - 생각 정리 파트너
- `/idea` - 대화에서 아이디어 추출 및 저장

### 🔧 System
- `/setup-workspace` - 초기 워크스페이스 설정
- `/inbox-processor` - Inbox 파일 정리
- `/pull-all` / `/push-all` - Git 동기화

### 🛠️ Setup Commands
- `/setup-google-calendar` - Google Calendar 통합 설정
- `/setup-web-crawler` - Web Crawler 스킬 설정

## Getting Started

### 🚀 빠른 시작 (5분)

#### 1. Clone & Setup
```bash
git clone https://github.com/Rhim80/imi-workspace.git
cd imi-workspace
```

#### 2. VS Code에서 열기
Claude Code로 이 폴더를 엽니다.

#### 3. 초기 설정 실행
```bash
/setup-workspace
```
- 이름 입력
- 첫 Daily Note 자동 생성
- 다음 단계 안내 받기

---

### 📝 첫 Daily Note 만들기

**방법 1: 커맨드 사용 (추천)**
```bash
/daily-note
```

**방법 2: 수동 생성**
1. `40-personal/41-daily/` 폴더로 이동
2. 오늘 날짜로 파일 생성: `YYYY-MM-DD.md`
3. `00-system/01-templates/daily-note-template.md` 복사

---

### 🗂️ 프로젝트 폴더 만들기

#### 대화형 방식 (추천)
Claude Code에게 물어보세요:
```
"imi 카페 브랜딩 프로젝트를 시작하고 싶어.
어디에 폴더를 만들면 좋을까?"
```

Claude가 제안:
- 📂 위치: `10-projects/11-imi-cafe-branding/`
- 📄 필수 파일: `README.md`, `requirements.md`
- 📋 템플릿 활용

#### 수동 방식
1. **프로젝트 폴더 생성**
   ```
   10-projects/11-my-first-project/
   ```

2. **README.md 생성**
   ```markdown
   # My First Project

   ## 목표
   - ...

   ## 타임라인
   - 시작: YYYY-MM-DD
   - 목표 종료: YYYY-MM-DD
   ```

3. **필요한 파일 추가**
   - `requirements.md` - 요구사항
   - `progress.md` - 진행 상황
   - `notes/` - 관련 노트

---

### 📚 지식 정리하기

#### 학습한 내용을 정리할 때
1. **카테고리 결정**
   - 비즈니스 관련? → `31-business/`
   - 기술 관련? → `32-technical/`
   - 산업 인사이트? → `33-industry/`

2. **폴더가 없으면 생성**
   ```
   30-knowledge/31-business-frameworks/
   ```

3. **문서 작성**
   ```markdown
   # Lean Canvas

   ## 개요
   ...

   ## 사용법
   ...
   ```

---

### 💡 대화형으로 Claude와 작업하기

**예시 1: 프로젝트 생성**
```
You: "매장 운영 체크리스트를 만들고 싶어. 어디에 저장하면 좋을까?"

Claude: "20-operations/21-daily-store-management/ 폴더를 만들고
opening-checklist.md와 closing-checklist.md를 생성하는 것을 추천합니다."
```

**예시 2: 폴더 정리**
```
You: "inbox에 있는 아이디어들을 정리하고 싶어."

Claude: "inbox 파일들을 확인하고 각각 적절한 위치로 이동시켜드리겠습니다.
- 프로젝트 아이디어 → 10-projects/
- 학습 메모 → 30-knowledge/
- 개인 일기 → 40-personal/41-daily/에 통합"
```

**예시 3: 구조 질문**
```
You: "고객 관리 프로세스 문서는 어디에 넣어야 해?"

Claude: "지속적인 업무이므로 20-operations/23-customer-service/
폴더를 만들어서 저장하는 것이 좋습니다."
```

## Tips

1. **Inbox Zero**: `00-inbox/`는 정기적으로 비우세요
2. **Daily Habit**: 매일 Daily Note를 작성하세요
3. **Weekly Review**: 주말에 한 주를 돌아보세요
4. **Archive 활용**: 완료된 프로젝트는 `90-archive/`로 이동
5. **템플릿 커스터마이징**: 자신에게 맞게 템플릿을 수정하세요

## Why Johnny Decimal?

Johnny Decimal 시스템은:
- 명확한 카테고리 구조
- 쉬운 파일 찾기
- 확장 가능한 시스템
- AI가 이해하기 쉬운 구조

## Credits

Inspired by:
- [Claudesidian](https://github.com/heyitsnoah/claudesidian) by Noah Brier
- 15 years of F&B operations experience
- Real-world AI automation workflows

## License

MIT License - 자유롭게 사용하고 수정하세요!

## Support

Issues나 질문이 있으시면 GitHub Issues를 활용해주세요.

---

**Made with ❤️ by hovoo (이림)**
F&B Professional × AI Practitioner