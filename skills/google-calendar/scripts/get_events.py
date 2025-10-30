#!/usr/bin/env python3
"""
Google Calendar에서 오늘 일정을 가져와서 Markdown 형식으로 출력
gcalcli 기반 래퍼 스크립트
"""

import os
import sys
import subprocess
import re
from datetime import datetime

def run_gcalcli(args):
    """gcalcli 실행 및 출력 캡처"""
    try:
        # PATH에 ~/.local/bin 추가 (pipx 설치 위치)
        env = os.environ.copy()
        env['PATH'] = f"{os.path.expanduser('~/.local/bin')}:{env.get('PATH', '')}"

        result = subprocess.run(
            ['gcalcli'] + args,
            capture_output=True,
            text=True,
            env=env
        )

        if result.returncode != 0:
            # 인증 필요 메시지 확인
            if 'oauth' in result.stderr.lower() or 'authenticate' in result.stderr.lower():
                print("❌ Google Calendar 인증이 필요합니다.")
                print("   다음 명령어로 인증하세요:")
                print("   gcalcli init")
                print("")
                print("   또는 기존 Python API 스크립트를 사용하세요:")
                print("   python3 get_events_original.py.backup")
                sys.exit(1)
            else:
                print(f"❌ gcalcli 실행 오류: {result.stderr}")
                sys.exit(1)

        return result.stdout
    except FileNotFoundError:
        print("❌ Error: gcalcli가 설치되지 않았습니다.")
        print("   설치: pipx install gcalcli")
        print("")
        print("   또는 기존 Python API 스크립트를 사용하세요:")
        print("   python3 get_events_original.py.backup")
        sys.exit(1)

def parse_gcalcli_output_to_markdown(output):
    """gcalcli 출력을 Markdown 형식으로 변환"""
    if not output.strip():
        return "일정이 없습니다."

    # ANSI 색상 코드 제거 (모든 형태)
    output_clean = re.sub(r'\x1b\[[0-9;]*m|\[[0-9;]*m', '', output)

    lines = output_clean.strip().split('\n')
    markdown_lines = []

    for line in lines:
        # 날짜 헤더 행은 건너뛰기 (예: "Thu Oct 23")
        if re.match(r'^[A-Z][a-z]{2}\s+[A-Z][a-z]{2}\s+\d{1,2}', line.strip()):
            continue

        # gcalcli agenda 출력 형식 파싱
        # 1. 시간 있는 일정: "  9:00am  Team Meeting"
        # 2. 종일 일정: "         하나 94,000" (공백으로 시작)

        # 시간 정보 추출 (정규식)
        time_match = re.search(r'(\d{1,2}:\d{2}[ap]m|All Day)', line, re.IGNORECASE)
        if time_match:
            time_str = time_match.group(1)

            # 시간 이후의 텍스트가 이벤트 제목
            event_start = time_match.end()
            event_text = line[event_start:].strip()

            # Markdown 형식으로 변환
            if time_str.lower() == 'all day':
                markdown_lines.append(f"- **종일** {event_text}")
            else:
                # 12시간 형식을 24시간 형식으로 변환
                time_24 = convert_to_24h(time_str)
                markdown_lines.append(f"- **{time_24}** {event_text}")
        else:
            # 시간 정보가 없으면 종일 일정으로 처리
            event_text = line.strip()
            if event_text:  # 빈 줄이 아니면
                markdown_lines.append(f"- **종일** {event_text}")

    if not markdown_lines:
        return "일정이 없습니다."

    return '\n'.join(markdown_lines)

def convert_to_24h(time_12h):
    """12시간 형식을 24시간 형식으로 변환"""
    try:
        dt = datetime.strptime(time_12h, '%I:%M%p')
        return dt.strftime('%H:%M')
    except:
        return time_12h

def get_today_events():
    """오늘 일정 가져오기 - 일정과 알림을 분리"""
    from datetime import datetime, timedelta

    # 오늘 날짜
    today_date = datetime.now()
    today = today_date.strftime('%Y-%m-%d')
    # 종일 일정 포함을 위해 내일까지 조회 후 필터링
    tomorrow = (today_date + timedelta(days=1)).strftime('%Y-%m-%d')

    # 1. Work, 개인+가족용 일정 조회
    work_calendars = ['Work', '개인 + 가족용']
    cmd_work = ['agenda', today, tomorrow, '--nocolor', '--nodeclined']
    for cal in work_calendars:
        cmd_work.extend(['--calendar', cal])

    work_output = run_gcalcli(cmd_work)
    work_filtered = filter_today_only(work_output, today)
    work_markdown = parse_gcalcli_output_to_markdown(work_filtered)

    # 2. Money 알림 조회
    cmd_money = ['agenda', today, tomorrow, '--nocolor', '--nodeclined', '--calendar', 'Money']
    money_output = run_gcalcli(cmd_money)
    money_filtered = filter_today_only(money_output, today)
    money_markdown = parse_gcalcli_output_to_markdown(money_filtered)

    # JSON 형식으로 반환 (템플릿에서 두 변수로 분리하기 위해)
    import json
    result = {
        'calendar_events': work_markdown,
        'money_alerts': money_markdown
    }

    return json.dumps(result, ensure_ascii=False)

def filter_today_only(output, today_str):
    """gcalcli 출력에서 오늘 날짜만 필터링"""
    from datetime import datetime

    if not output.strip():
        return ""

    # ANSI 색상 코드 제거 (모든 형태)
    output_clean = re.sub(r'\x1b\[[0-9;]*m|\[[0-9;]*m', '', output)

    lines = output_clean.strip().split('\n')
    today_lines = []

    # 오늘 날짜 파싱 (예: "Tue Oct 22")
    today_date = datetime.strptime(today_str, '%Y-%m-%d')
    today_formatted = today_date.strftime('%a %b %d').replace(' 0', ' ')  # "Tue Oct 22"

    include_line = False
    for line in lines:
        # 빈 줄 건너뛰기
        if not line.strip():
            continue

        # 날짜 행인지 확인
        if today_formatted in line:
            include_line = True
            # 날짜 행에 일정이 같이 있는 경우 (예: "Thu Oct 23         하나 94,000")
            # 날짜 부분을 제거하고 일정만 추출
            event_part = line.replace(today_formatted, '').strip()
            if event_part:
                today_lines.append('         ' + event_part)  # 공백 추가로 종일 일정 형식 유지
            continue
        elif re.match(r'^[A-Z][a-z]{2}\s+[A-Z][a-z]{2}\s+\d{1,2}', line.strip()):
            # 다른 날짜 행이 나오면 중단
            include_line = False
        elif include_line:
            # 오늘 날짜의 일정 행
            today_lines.append(line)

    return '\n'.join(today_lines)

if __name__ == '__main__':
    try:
        result = get_today_events()
        print(result)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
