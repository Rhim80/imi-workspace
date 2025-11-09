# Pull All Git Repositories

모든 독립 Git 저장소를 한번에 pull합니다.

## 실행 순서

**환경별 경로:**

### 1. PKM 메인
- Windows: `c:\Users\hovoo\Documents\claude-projects\pkm\`
- WSL: `/home/rhim/claude-projects/pkm/`
- Mac: `/Users/rhim/Projects/pkm/`
- 명령: `git pull`

### 2. imi-office-team (팀 프로젝트 메인)
- Windows: `c:\Users\hovoo\Documents\claude-projects\imi-office-team\`
- Mac: `/Users/rhim/Projects/imi-office-team/`
- 명령: `git pull` + `git submodule update --init --recursive`

### 3. 강릉 카페 프로젝트 (imi-office-team submodule)
- 경로: `imi-office-team/projects/gangneung-cafe-2025/`
- 명령: `git pull origin main`

### 4. 카페 운영 (imi-office-team submodule)
- 경로: `imi-office-team/projects/cafe-operations/`
- 명령: `git pull origin main`

## 지시사항

- **Step 1**: PKM 메인 저장소에서 `git pull` 실행
- **Step 2**: imi-office-team 저장소에서 `git pull` 실행
- **Step 3**: imi-office-team에서 `git submodule update --init --recursive` 실행
- **Step 4**: 각 submodule 폴더에서 `git pull origin main` 실행 (최신 커밋 받기)
- 변경사항이 없으면 "Already up to date" 표시
- 각 단계의 성공/실패 여부를 명확히 알려주세요
- 모든 작업 완료 후 요약 리포트를 제공하세요

## 출력 예시

```
========================================
모든 Git 저장소 Pull 시작
========================================

[Step 1] PKM 메인 pull
✅ Already up to date

[Step 2] imi-office-team pull
✅ Pull 완료 (3 files changed)

[Step 3] Submodule 업데이트
✅ 강릉 카페 프로젝트 submodule 업데이트
✅ 카페 운영 submodule 업데이트

[Step 4] 각 프로젝트 최신 커밋
✅ 강릉 카페: Already up to date
✅ 카페 운영: Already up to date

========================================
✅ 모든 저장소 동기화 완료!
========================================
```

## 참고

- imi-office-team은 팀 메인 저장소
- 강릉 카페, 카페 운영은 imi-office-team의 submodule
- Submodule은 특정 커밋을 가리키므로 Step 4에서 최신 커밋을 받아야 함
- PKM에는 더 이상 팀 프로젝트 submodule이 없음
