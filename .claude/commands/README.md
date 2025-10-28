# Claude Code 커스텀 커맨드 위치

## ⚠️ 중요: 커맨드 파일 위치

**모든 커스텀 커맨드는 유저 레벨에서 관리됩니다:**

- Windows: `C:\Users\hovoo\.claude\commands\`
- Mac: `/Users/rhim/.claude\commands\`

**이 폴더(프로젝트 레벨)에는 커맨드 파일을 두지 않습니다.**

## 사용 가능한 커맨드

유저 레벨 `.claude/commands/`에서 관리되는 커맨드:

- `/daily-note` - Daily Note 생성/열기
- `/daily-review` - Daily Review 생성
- `/idea [카테고리]` - 아이디어 추출 및 저장
- `/push-all` - 모든 Git 저장소 push
- `/pull-all` - 모든 Git 저장소 pull
- `/git-status` - 모든 Git 저장소 상태 확인

## Git 저장소 정보

유저 레벨 config:
- 저장소: https://github.com/Rhim80/claude-config.git
- 경로: `~/.claude/`

프로젝트:
- 저장소: https://github.com/Rhim80/claude-projects.git
- 경로: PKM 메인
