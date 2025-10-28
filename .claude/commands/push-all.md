# Push All

워크스페이스를 Git에 push합니다.

## 실행

```bash
/push-all
```

## 수행 작업

1. 현재 디렉토리에서 `git add .`
2. 커밋 메시지 자동 생성 (변경사항 기반)
3. `git push`

## 자동 커밋 메시지

Claude Code가 변경사항을 분석하여 자동 생성:
- "📝 Daily Note 업데이트"
- "💡 아이디어 추가"
- "✅ Todo 완료"

## 주의사항

- 단순한 단일 저장소 push만 수행
- 서브모듈은 포함하지 않음
