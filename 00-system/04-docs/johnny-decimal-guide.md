# Johnny Decimal Guide

Johnny Decimal 시스템 가이드입니다.

## 기본 개념

모든 것을 10개의 카테고리로 나누고, 각 카테고리를 다시 10개로 나눕니다.

```
00-09: 시스템
10-19: 프로젝트
20-29: 운영
30-39: 지식
40-49: 개인
50-59: 리소스
90-99: 아카이브
```

## 폴더 구조

### 00-09: System (시스템)
- 00-inbox: 빠른 캡처
- 00-system: 설정 및 템플릿

### 10-19: Projects (프로젝트)
마감일이 있는 시한부 프로젝트
- 11-xxx: 첫 번째 프로젝트 카테고리
- 12-xxx: 두 번째 프로젝트 카테고리

### 20-29: Operations (운영)
지속적으로 유지하는 업무
- 21-xxx: 첫 번째 운영 카테고리
- 22-xxx: 두 번째 운영 카테고리

### 30-39: Knowledge (지식)
학습 자료 및 참고 문서
- 31-xxx: 첫 번째 지식 카테고리
- 36-xxx: AI 관련 지식
- 37-xxx: 산업 지식

### 40-49: Personal (개인)
개인 노트 및 기록
- 41-daily: Daily Notes
- 42-weekly: Weekly Reviews
- 46-todos: 할 일 관리

### 50-59: Resources (리소스)
외부 자료 및 참고 문서
- 51-xxx: 첫 번째 리소스 카테고리

### 90-99: Archive (아카이브)
완료되거나 중단된 항목
- 91-completed: 완료된 프로젝트
- 92-cancelled: 중단된 프로젝트

## 사용 예시

### 프로젝트 생성
```
10-projects/
└── 11-website-redesign/
    ├── README.md
    ├── notes/
    └── resources/
```

### 운영 업무
```
20-operations/
└── 21-weekly-reports/
    ├── 2025-W43.md
    ├── 2025-W44.md
```

### 지식 축적
```
30-knowledge/
└── 36-ai-tools/
    ├── claude-code.md
    ├── chatgpt.md
```

## 장점

1. **명확한 구조**: 어디에 저장할지 고민 불필요
2. **빠른 검색**: 숫자로 즉시 이동
3. **확장 가능**: 필요에 따라 카테고리 추가
4. **AI 친화적**: AI가 파일 위치를 쉽게 이해

## 팁

- 완벽한 분류보다 일관성이 중요
- 잘못 분류했다면 언제든 이동
- 자신만의 규칙을 만들어도 OK
- 10개 제한은 가이드일 뿐, 유연하게 사용

## 더 알아보기

- [Johnny Decimal 공식 사이트](https://johnnydecimal.com)
