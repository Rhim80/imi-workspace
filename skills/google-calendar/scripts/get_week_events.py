#!/usr/bin/env python3
"""
Google Calendar에서 이번 주 일정을 가져와서 Markdown 형식으로 출력
Weekly Review용
"""

import os
import sys
import subprocess
import re
from datetime import datetime, timedelta

def run_gcalcli(args):
    """gcalcli 실행 및 출력 캡처"""
    try:
        # PATH에 ~/.local/bin 추가
        env = os.environ.copy()
        env['PATH'] = f"{os.path.expanduser('~/.local/bin')}:{env.get('PATH', '')}"

        result = subprocess.run(
            ['gcalcli'] + args,
            capture_output=True,
            text=True,
            env=env
        )

        if result.returncode != 0:
            if 'oauth' in result.stderr.lower() or 'authenticate' in result.stderr.lower():
                print("❌ Google Calendar 인증이 필요합니다.")
                print("   다음 명령어로 인증하세요:")
                print("   gcalcli init")
                sys.exit(1)
            else:
                print(f"❌ gcalcli 실행 오류: {result.stderr}")
                sys.exit(1)

        return result.stdout
    except FileNotFoundError:
        print("❌ Error: gcalcli가 설치되지 않았습니다.")
        print("   설치: pipx install gcalcli")
        sys.exit(1)

def parse_week_events_to_markdown(output):
    """주간 일정을 Markdown 형식으로 변환 (날짜별 그룹화)"""
    if not output.strip():
        return "일정이 없습니다."

    # ANSI 색상 코드 제거 (모든 형태)
    output_clean = re.sub(r'\x1b\[[0-9;]*m|\[[0-9;]*m', '', output)

    lines = output_clean.strip().split('\n')
    events_by_date = {}
    current_date = None

    for line in lines:
        # 빈 줄 건너뛰기
        if not line.strip():
            continue

        # 날짜 헤더 행 체크 (예: "Mon Oct 20")
        date_match = re.match(r'^([A-Z][a-z]{2} [A-Z][a-z]{2} \d{1,2})', line.strip())
        if date_match:
            current_date = date_match.group(1)
            # 날짜 헤더에 일정이 같이 있는 경우 처리
            event_part = line.replace(current_date, '').strip()
            if event_part:
                # 줄 시작 부분의 시간 확인
                time_match = re.match(r'^\s*(\d{1,2}:\d{2})([ap]m)?', event_part, re.IGNORECASE)
                if time_match:
                    time_str = time_match.group(1)
                    ampm = time_match.group(2)
                    event_text = event_part[time_match.end():].strip()

                    # 12시간 형식이면 24시간으로 변환
                    if ampm:
                        time_display = convert_to_24h(time_str + ampm)
                    else:
                        time_display = time_str  # 이미 24시간 형식
                else:
                    # 종일 일정
                    event_text = event_part
                    time_display = '종일'

                if current_date not in events_by_date:
                    events_by_date[current_date] = []
                events_by_date[current_date].append((time_display, event_text))
            continue

        # 일정 행 처리
        if current_date:
            # 줄 시작 부분의 시간 확인 (24시간 형식: HH:MM 또는 12시간 형식: HH:MMam/pm)
            time_match = re.match(r'^\s*(\d{1,2}:\d{2})([ap]m)?', line, re.IGNORECASE)
            if time_match:
                time_str = time_match.group(1)
                ampm = time_match.group(2)
                event_text = line[time_match.end():].strip()

                # 12시간 형식이면 24시간으로 변환
                if ampm:
                    time_display = convert_to_24h(time_str + ampm)
                else:
                    time_display = time_str  # 이미 24시간 형식
            else:
                # 종일 일정
                event_text = line.strip()
                time_display = '종일'

            if event_text:
                if current_date not in events_by_date:
                    events_by_date[current_date] = []
                events_by_date[current_date].append((time_display, event_text))

    if not events_by_date:
        return "일정이 없습니다."

    # Markdown 형식으로 변환
    markdown_lines = []
    markdown_lines.append("## 이번 주 일정\n")

    for date_str in sorted(events_by_date.keys(), key=lambda x: datetime.strptime(x, '%a %b %d')):
        markdown_lines.append(f"### {date_str}")
        for time, event in events_by_date[date_str]:
            markdown_lines.append(f"- **{time}** {event}")
        markdown_lines.append("")  # 날짜 구분

    return '\n'.join(markdown_lines)

def convert_to_24h(time_12h):
    """12시간 형식을 24시간 형식으로 변환"""
    try:
        dt = datetime.strptime(time_12h, '%I:%M%p')
        return dt.strftime('%H:%M')
    except:
        return time_12h

def get_week_events():
    """이번 주 일정 가져오기 (월요일~일요일)"""
    # 이번 주 월요일 계산
    today = datetime.now()
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)

    # gcalcli agenda 실행 (이번 주)
    start_date = monday.strftime('%Y-%m-%d')
    end_date = sunday.strftime('%Y-%m-%d')

    # 조회할 캘린더 지정 (이미커피 제외)
    calendars = ['Work', '개인 + 가족용', 'Money']

    cmd = ['agenda', start_date, end_date, '--nocolor', '--nodeclined']
    for cal in calendars:
        cmd.extend(['--calendar', cal])

    output = run_gcalcli(cmd)

    # Markdown 형식으로 변환
    markdown = parse_week_events_to_markdown(output)

    return markdown

if __name__ == '__main__':
    try:
        result = get_week_events()
        print(result)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
