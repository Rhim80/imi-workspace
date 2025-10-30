#!/usr/bin/env python3
"""
Google Calendar에서 키워드로 일정 검색
gcalcli search 기반
"""

import os
import sys
import subprocess
import re
from datetime import datetime

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

def parse_search_results_to_markdown(output):
    """검색 결과를 Markdown 형식으로 변환"""
    if not output.strip():
        return "검색 결과가 없습니다."

    # ANSI 색상 코드 제거 (모든 형태)
    output_clean = re.sub(r'\x1b\[[0-9;]*m|\[[0-9;]*m', '', output)

    lines = output_clean.strip().split('\n')
    markdown_lines = []
    markdown_lines.append("## 검색 결과\n")

    for line in lines:
        # gcalcli search 출력 파싱
        # 날짜와 시간 추출
        date_match = re.search(r'(\w{3} \w{3} \d{1,2})', line)
        time_match = re.search(r'(\d{1,2}:\d{2}[ap]m|All Day)', line, re.IGNORECASE)

        if date_match and time_match:
            date_str = date_match.group(1)
            time_str = time_match.group(1)

            # 이벤트 제목 추출
            event_start = time_match.end()
            event_text = line[event_start:].strip()

            # Markdown 형식
            if time_str.lower() == 'all day':
                markdown_lines.append(f"- **{date_str}** (종일) {event_text}")
            else:
                # 24시간 형식으로 변환
                time_24 = convert_to_24h(time_str)
                markdown_lines.append(f"- **{date_str}** {time_24} {event_text}")

    if len(markdown_lines) == 1:  # 제목만 있음
        return "검색 결과가 없습니다."

    return '\n'.join(markdown_lines)

def convert_to_24h(time_12h):
    """12시간 형식을 24시간 형식으로 변환"""
    try:
        dt = datetime.strptime(time_12h, '%I:%M%p')
        return dt.strftime('%H:%M')
    except:
        return time_12h

def search_events(keyword):
    """키워드로 일정 검색"""
    # 조회할 캘린더 지정 (이미커피 제외)
    calendars = ['Work', '개인 + 가족용', 'Money']

    cmd = ['search', keyword, '--nocolor', '--nodeclined']
    for cal in calendars:
        cmd.extend(['--calendar', cal])

    # gcalcli search 실행
    output = run_gcalcli(cmd)

    # Markdown 형식으로 변환
    markdown = parse_search_results_to_markdown(output)

    return markdown

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("❌ Usage: python3 search_events.py \"검색 키워드\"")
        print("   예시: python3 search_events.py \"강릉\"")
        sys.exit(1)

    keyword = ' '.join(sys.argv[1:])

    try:
        result = search_events(keyword)
        print(result)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
