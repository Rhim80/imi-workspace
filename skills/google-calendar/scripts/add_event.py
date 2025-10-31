#!/usr/bin/env python3
"""
gcalcli를 사용하여 Google Calendar에 일정 추가
"""

import subprocess
import sys
from datetime import datetime

def run_gcalcli(cmd):
    """gcalcli 명령어 실행"""
    full_cmd = ['gcalcli'] + cmd
    result = subprocess.run(full_cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        sys.exit(1)

    return result.stdout

def add_event(calendar, title, start_date, start_time, duration_minutes=150):
    """
    Google Calendar에 일정 추가

    Args:
        calendar: 캘린더 이름 (예: "AI", "Work", "개인 + 가족용")
        title: 일정 제목
        start_date: 시작 날짜 (YYYY-MM-DD)
        start_time: 시작 시간 (HH:MM)
        duration_minutes: 지속 시간 (분, 기본 150분 = 2.5시간)
    """
    # 날짜/시간 검증
    try:
        dt = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M")
    except ValueError as e:
        print(f"❌ 날짜 형식 오류: {e}")
        print(f"   올바른 형식: YYYY-MM-DD HH:MM")
        sys.exit(1)

    # gcalcli add 명령어 구성
    when = dt.strftime("%Y-%m-%d %H:%M")

    cmd = [
        'add',
        '--calendar', calendar,
        '--title', title,
        '--when', when,
        '--duration', str(duration_minutes),
        '--noprompt'  # 대화형 입력 건너뛰기
    ]

    print(f"📅 일정 추가 중...")
    print(f"   캘린더: {calendar}")
    print(f"   제목: {title}")
    print(f"   시작: {when}")
    print(f"   시간: {duration_minutes}분 ({duration_minutes/60:.1f}시간)")

    output = run_gcalcli(cmd)
    print(f"✅ 일정이 추가되었습니다!")

    return output

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("❌ Usage: python3 add_event.py <캘린더> <제목> <날짜> <시간> [지속시간(분)]")
        print("")
        print("예시:")
        print("  python3 add_event.py \"AI\" \"HFK 1회차\" \"2025-12-06\" \"14:30\"")
        print("  python3 add_event.py \"AI\" \"HFK 1회차\" \"2025-12-06\" \"14:30\" \"150\"")
        print("")
        print("캘린더 옵션: AI, Work, 개인 + 가족용, Money")
        sys.exit(1)

    calendar = sys.argv[1]
    title = sys.argv[2]
    start_date = sys.argv[3]
    start_time = sys.argv[4]
    duration = int(sys.argv[5]) if len(sys.argv) > 5 else 150  # 기본 2.5시간

    add_event(calendar, title, start_date, start_time, duration)
