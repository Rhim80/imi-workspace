# Setup Workspace - 초기 설정 마법사

IMI Workspace를 처음 사용할 때 실행하는 설정 마법사입니다.

## 수행 작업

1. **사용자 정보 수집**
   - 이름
   - 주요 업무/관심사
   - 현재 진행 중인 프로젝트

2. **폴더 구조 확인**
   - Johnny Decimal 시스템 설명
   - 각 폴더 용도 안내

3. **필수 파일 생성**
   - `40-personal/46-todos/active-todos.md`
   - 첫 Daily Note

4. **다음 단계 안내**
   - `/daily-note` 사용법
   - `/thinking-partner` 소개
   - `/create-command` 활용법

## 실행

```bash
/setup-workspace
```

## 대화형 설정

Claude Code가 질문하며 설정을 진행합니다:

1. "이름이 무엇인가요?"
2. "주로 어떤 일을 하시나요?"
3. "현재 진행 중인 프로젝트가 있나요?"
4. "Google Calendar를 사용하시나요?"
5. "첫 Daily Note를 만들까요?"

## 선택적 설정

- Google Calendar 통합 (skills/google-calendar/)
- Git 원격 저장소 설정

## 재실행 가능

언제든 다시 실행하여 설정 변경 가능.
