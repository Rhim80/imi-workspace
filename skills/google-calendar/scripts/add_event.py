#!/usr/bin/env python3
"""
자연어로 Google Calendar 일정 등록
"""

import os
import sys
import re
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle

# Google Calendar API Scopes
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_credentials():
    """Google Calendar API 인증 처리"""
    creds = None
    token_path = os.path.join(os.path.dirname(__file__), 'token.pickle')

    # 저장된 토큰 확인
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    # 토큰이 없거나 만료된 경우
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            credentials_path = os.path.join(os.path.dirname(__file__), 'credentials.json')
            if not os.path.exists(credentials_path):
                print("❌ Error: credentials.json 파일이 없습니다.")
                print(f"   위치: {credentials_path}")
                print("   Google Cloud Console에서 OAuth 2.0 클라이언트 ID를 생성하고 credentials.json을 다운로드하세요.")
                sys.exit(1)

            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        # 토큰 저장
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def parse_natural_language(text):
    """자연어를 일정 정보로 파싱"""
    now = datetime.now()
    event = {
        'summary': '',
        'start': None,
        'end': None,
        'location': '',
        'all_day': False
    }

    # 위치 추출 (@위치명)
    location_match = re.search(r'@(\S+)', text)
    if location_match:
        event['location'] = location_match.group(1)
        text = text.replace(location_match.group(0), '').strip()

    # 날짜 파싱
    date = now
    if '내일' in text:
        date = now + timedelta(days=1)
        text = text.replace('내일', '').strip()
    elif '모레' in text:
        date = now + timedelta(days=2)
        text = text.replace('모레', '').strip()
    elif '오늘' in text:
        text = text.replace('오늘', '').strip()

    # 종일 일정
    if '종일' in text:
        event['all_day'] = True
        text = text.replace('종일', '').strip()
        event['start'] = date.strftime('%Y-%m-%d')
        event['end'] = (date + timedelta(days=1)).strftime('%Y-%m-%d')
    else:
        # 시간 파싱
        # "오후 3시" 형식
        time_match = re.search(r'(오전|오후)\s*(\d+)시', text)
        if time_match:
            period = time_match.group(1)
            hour = int(time_match.group(2))
            if period == '오후' and hour != 12:
                hour += 12
            elif period == '오전' and hour == 12:
                hour = 0
            start_time = date.replace(hour=hour, minute=0, second=0)
            text = text.replace(time_match.group(0), '').strip()
        # "14:00" 형식
        elif re.search(r'\d{1,2}:\d{2}', text):
            time_match = re.search(r'(\d{1,2}):(\d{2})', text)
            hour = int(time_match.group(1))
            minute = int(time_match.group(2))
            start_time = date.replace(hour=hour, minute=minute, second=0)
            text = text.replace(time_match.group(0), '').strip()
        else:
            # 시간 지정 없으면 기본 9시
            start_time = date.replace(hour=9, minute=0, second=0)

        # 종료 시간 (기본 1시간)
        end_time = start_time + timedelta(hours=1)

        event['start'] = start_time.isoformat()
        event['end'] = end_time.isoformat()

    # 남은 텍스트를 제목으로
    event['summary'] = text.strip()

    return event

def create_event(event_data):
    """Google Calendar에 일정 생성"""
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    # 이벤트 구조 생성
    event = {
        'summary': event_data['summary'],
    }

    if event_data['all_day']:
        event['start'] = {'date': event_data['start']}
        event['end'] = {'date': event_data['end']}
    else:
        event['start'] = {'dateTime': event_data['start'], 'timeZone': 'Asia/Seoul'}
        event['end'] = {'dateTime': event_data['end'], 'timeZone': 'Asia/Seoul'}

    if event_data['location']:
        event['location'] = event_data['location']

    # 일정 생성
    created_event = service.events().insert(calendarId='primary', body=event).execute()

    return created_event

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("❌ Usage: python3 add_event.py \"자연어 일정 텍스트\"")
        print("   예시: python3 add_event.py \"내일 오후 3시 회의\"")
        sys.exit(1)

    natural_text = ' '.join(sys.argv[1:])

    try:
        # 자연어 파싱
        event_data = parse_natural_language(natural_text)

        # 일정 생성
        created_event = create_event(event_data)

        print(f"✅ 일정이 등록되었습니다!")
        print(f"   제목: {event_data['summary']}")
        if event_data['all_day']:
            print(f"   날짜: {event_data['start']} (종일)")
        else:
            start_dt = datetime.fromisoformat(event_data['start'])
            print(f"   시작: {start_dt.strftime('%Y-%m-%d %H:%M')}")
        if event_data['location']:
            print(f"   위치: {event_data['location']}")
        print(f"   링크: {created_event.get('htmlLink')}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)
