# Working Backwards Project Template
# Working Backwards 프로젝트 템플릿

> Amazon의 Working Backwards 방법론으로 비즈니스 아이디어를 구체화하는 템플릿입니다.

---

## 🎯 이 템플릿 사용법

### 1. 템플릿 복사하기

```bash
# 프로젝트 이름 정하기 (예: my-cafe-project)
cp -r 10-projects/00-working-backwards-template/ 10-projects/11-my-project-name/

# 폴더로 이동
cd 10-projects/11-my-project-name/
```

### 2. Working Backwards 워크플로우

```
Step 1: PR 작성 (가장 성공했을 때 상상)
   ↓
   /working-backwards-pr 실행
   ↓
   pr-document.md 완성

Step 2: FAQ 작성 (어려운 질문들)
   ↓
   faq.md 작성
   ↓
   Internal FAQ 완성

Step 3: 역순 로드맵 생성
   ↓
   /generate-roadmap 실행
   ↓
   roadmap.md 완성

Step 4: 실행 및 검증
   ↓
   customer-research/ 고객 인터뷰
   ↓
   daily-progress/ 진행 기록
```

---

## 📂 폴더 구조

### pr-document.md
**목적**: 프로젝트가 가장 성공했을 때의 보도자료
**작성법**: `/working-backwards-pr` 커맨드 실행

### faq.md
**목적**: 외부/내부 FAQ 작성
**구성**:
- External FAQ: 고객이 물어볼 질문 (5-10개)
- Internal FAQ: 팀이 답해야 할 질문 (10-20개)

### roadmap.md
**목적**: 역순으로 도출한 실행 계획
**작성법**: `/generate-roadmap` 커맨드 실행

### customer-research/
**목적**: 고객 인터뷰 및 검증
**파일**:
- `interview-01-[이름].md`
- `interview-02-[이름].md`
- `validation-summary.md`

### daily-progress/
**목적**: 일일 진행 상황 기록
**파일**:
- `YYYY-MM-DD.md` (날짜별 노트)
- 또는 `/daily-note` 사용

### final-presentation/
**목적**: 최종 발표 자료
**파일**:
- `presentation-outline.md`
- `demo/` (스크린샷, 영상 등)

---

## 🚀 GPTers 스터디 4주 체크리스트

### Week 1: PR/FAQ 초안
- [ ] 템플릿 복사 완료
- [ ] `/working-backwards-pr` 실행
- [ ] `pr-document.md` v1.0 작성
- [ ] `faq.md` 5-10개 작성
- [ ] `/daily-note`로 사고 과정 기록

### Week 2: 로드맵 및 피드백 반영
- [ ] Week 1 피드백 반영 → v2.0
- [ ] `/generate-roadmap` 실행
- [ ] `roadmap.md` 완성
- [ ] 4주 실행 계획 구체화

### Week 3: 실행 및 검증
- [ ] 고객 인터뷰 3-5명 실시
- [ ] `customer-research/` 정리
- [ ] MVP 또는 프로토타입 진행
- [ ] `daily-progress/` 지속 기록

### Week 4: 최종 발표
- [ ] `final-presentation/presentation-outline.md` 작성
- [ ] PR v1.0 vs 현재 비교
- [ ] 실행 결과 정리
- [ ] 다음 3개월 계획

---

## 💡 주요 커맨드

### `/working-backwards-pr`
Amazon Working Backwards PR/FAQ 문서 생성
- 대화형 5단계 프로세스
- 45-60분 소요

### `/generate-roadmap`
PR/FAQ 기반 역순 로드맵 생성
- Milestone 정의
- Dependencies 매핑
- Risk 식별

### `/thinking-partner`
아이디어 구체화 및 사고 촉진
- 즉시 답 주지 않고 질문으로 유도
- 모순점 발견

### `/daily-note`
일일 진행 노트 생성
- `40-personal/41-daily/` 자동 생성
- 매일의 사고 과정 기록

---

## 📚 참고 템플릿

### PR/FAQ 템플릿
`00-system/01-templates/pr-faq-template.md`

### 고객 인터뷰 템플릿
`00-system/01-templates/interview-template.md`

### Daily Note 템플릿
`00-system/01-templates/daily-note-template.md`

---

## 🎓 Working Backwards 핵심 원칙

1. **Start with the customer** - 고객에서 시작
2. **Work backwards** - 역순으로 일하기
3. **10x better, not 10%** - 10배 더 나은 솔루션
4. **"So What?" test** - 모든 문장이 의미 있어야 함
5. **Be specific** - 구체적인 숫자와 사례

---

**Created**: 2025-11-09
**For**: GPTers 19기 창업.BM 스터디
**Version**: v1.0
