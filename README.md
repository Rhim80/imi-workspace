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

Johnny Decimal 시스템 기반:

```
imi-workspace/
├── 00-inbox/          # 빠른 캡처 공간
├── 00-system/         # 시스템 설정 및 템플릿
├── 10-projects/       # 활성 프로젝트 (시한부)
├── 20-operations/     # 비즈니스 운영 (지속적)
├── 30-knowledge/      # 지식 아카이브
├── 40-personal/       # 개인 노트
│   ├── 41-daily/      # Daily Notes
│   └── 42-weekly/     # Weekly Reviews
├── 50-resources/      # 참고 자료
└── 90-archive/        # 완료/중단 항목
```

### 각 폴더의 역할

- **00-inbox**: 빠르게 캡처한 아이디어, 링크, 메모
- **00-system**: 템플릿과 시스템 설정
- **10-projects**: 마감일이 있는 시한부 프로젝트
- **20-operations**: 지속적으로 유지해야 하는 업무
- **30-knowledge**: 검증된 지식과 학습 자료
- **40-personal**: 개인 노트 (daily, weekly)
- **50-resources**: 외부 자료와 참고 문서
- **90-archive**: 완료되거나 중단된 프로젝트

## Templates

`00-system/01-templates/`에서 사용 가능한 템플릿:

- **daily-note-template.md** - 매일 작성하는 노트
- **weekly-review-template.md** - 주간 회고
- **Project Template.md** - 새 프로젝트 시작

## Getting Started

### 1. 첫 Daily Note 만들기

`40-personal/41-daily/` 폴더에 오늘 날짜로 파일을 만듭니다:
- 파일명: `YYYY-MM-DD.md` (예: `2025-10-28.md`)
- 템플릿: `00-system/01-templates/daily-note-template.md` 복사

### 2. 프로젝트 시작하기

`10-projects/`에 새 폴더를 만들고 프로젝트를 시작하세요:
- 폴더명: `11-xxx` 형식 (Johnny Decimal)
- 프로젝트 폴더 안에 `README.md` 생성

### 3. 지식 축적하기

`30-knowledge/`에 카테고리별로 학습 내용을 정리하세요.

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