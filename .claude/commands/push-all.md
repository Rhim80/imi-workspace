# Push All Git Repositories

모든 독립 Git 저장소를 한번에 commit 후 push합니다.

## 실행 순서

### Step 0: Daily Note 업데이트 (Commit 전 필수)
- `/daily-note` 슬래시 커맨드 실행
- 오늘 날짜 Daily Note가 자동으로 업데이트됨
- Daily Note 파일이 PKM 메인에 추가됨

### Step 1: Git Commit

**커밋 메시지**: "🔄 자동 업데이트"

**환경별 경로:**

1. **IMI Office Team (팀 통합 저장소)**
   - Windows: `c:\Users\hovoo\Documents\claude-projects\imi-office-team\`
   - WSL: `/home/rhim/claude-projects/imi-office-team/`
   - Mac: `/Users/rhim/Projects/imi-office-team/`
   - **주의**: Submodule 2개 포함 (강릉 카페, 카페 운영)

2. **강릉 카페 프로젝트 (Submodule)**
   - Windows: `c:\Users\hovoo\Documents\claude-projects\imi-office-team\projects\gangneung-cafe-2025\`
   - WSL: `/home/rhim/claude-projects/imi-office-team/projects/gangneung-cafe-2025/`
   - Mac: `/Users/rhim/Projects/imi-office-team/projects/gangneung-cafe-2025/`

3. **카페 운영 (Submodule)**
   - Windows: `c:\Users\hovoo\Documents\claude-projects\imi-office-team\projects\cafe-operations\`
   - WSL: `/home/rhim/claude-projects/imi-office-team/projects/cafe-operations/`
   - Mac: `/Users/rhim/Projects/imi-office-team/projects/cafe-operations/`

4. **PKM 메인**
   - Windows: `c:\Users\hovoo\Documents\claude-projects\pkm\`
   - WSL: `/home/rhim/claude-projects/pkm/`
   - Mac: `/Users/rhim/Projects/pkm/`

### Step 2: Git Push

**순서 (중요!):**
1. Submodule 먼저 push (강릉 카페, 카페 운영)
2. IMI Office Team push (submodule 참조 업데이트)
3. PKM 메인 push

## 지시사항

- **Step 0**: `/daily-note` 커맨드를 먼저 실행하세요
- **Step 1**: 각 저장소에서 `git add . && git commit -m "🔄 자동 업데이트"` 실행
  - 순서: 강릉 카페 → 카페 운영 → IMI Office Team → PKM 메인
- **Step 2**: 각 저장소에서 `git push origin main` 실행 (명시적으로!)
  - 순서: 강릉 카페 → 카페 운영 → IMI Office Team → PKM 메인
  - **중요**: `git push` 대신 `git push origin main`을 사용하여 확실하게 push
- **Submodule 규칙**: 자식(submodule)을 먼저 push하고, 부모(imi-office-team)는 나중에 push
- 변경사항이 없는 경우 "변경사항 없음"을 알려주세요
- 각 단계의 성공/실패 여부를 명확히 알려주세요
- 모든 작업 완료 후 요약 리포트를 제공하세요

## 출력 예시

```
========================================
모든 Git 저장소 Push 시작
========================================

커밋 메시지: "🔄 자동 업데이트"

[Step 0] Daily Note 업데이트
✅ Daily Note 업데이트 완료

[Step 1] Commit 단계
[1/4] 강릉 카페 프로젝트 (Submodule)
✅ Commit 완료 (3 files changed)

[2/4] 카페 운영 (Submodule)
ℹ️ 변경사항 없음

[3/4] IMI Office Team (통합 저장소)
✅ Commit 완료 (submodule 참조 업데이트)

[4/4] PKM 메인
✅ Commit 완료 (2 files changed)

[Step 2] Push 단계
[1/4] 강릉 카페 프로젝트
✅ Push 완료

[2/4] 카페 운영
ℹ️ Push 건너뜀 (변경사항 없음)

[3/4] IMI Office Team
✅ Push 완료

[4/4] PKM 메인
✅ Push 완료

========================================
✅ 모든 작업 완료!
========================================
```
