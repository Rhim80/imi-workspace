#!/bin/bash
#
# 웹 크롤러 + Gemini OCR 시스템 설치 스크립트
#

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║   웹 크롤러 + Gemini OCR 시스템 설치                      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# 1. Python 버전 확인
echo -e "${YELLOW}[1/5] Python 버전 확인${NC}"
python3 --version
echo ""

# 2. 의존성 설치
echo -e "${YELLOW}[2/5] 의존성 설치 중...${NC}"
pip install -r requirements.txt
echo -e "${GREEN}✅ 완료${NC}\n"

# 3. .env 파일 생성
if [ ! -f .env ]; then
    echo -e "${YELLOW}[3/5] .env 파일 생성${NC}"
    cp .env.example .env
    echo -e "${GREEN}✅ .env 파일 생성 완료${NC}\n"

    echo -e "${RED}⚠️ 중요: .env 파일을 편집하여 API 키를 입력하세요!${NC}"
    echo ""
    echo "편집: nano .env"
    echo ""
    echo "필요한 API 키:"
    echo "  1. GEMINI_API_KEY: https://aistudio.google.com/apikey"
    echo "  2. FIRECRAWL_API_KEY: https://firecrawl.dev"
    echo ""
else
    echo -e "${YELLOW}[3/5] .env 파일 이미 존재${NC}"
    echo -e "${GREEN}✅ 건너뛰기${NC}\n"
fi

# 4. 실행 권한 부여
echo -e "${YELLOW}[4/5] 실행 권한 설정${NC}"
chmod +x web-crawler.py
echo -e "${GREEN}✅ 완료${NC}\n"

# 5. API 키 확인
echo -e "${YELLOW}[5/5] API 키 확인${NC}"

if grep -q "your_gemini_api_key_here" .env 2>/dev/null; then
    echo -e "${RED}❌ GEMINI_API_KEY가 설정되지 않음${NC}"
    GEMINI_OK=false
else
    echo -e "${GREEN}✅ GEMINI_API_KEY 설정됨${NC}"
    GEMINI_OK=true
fi

if grep -q "your_firecrawl_api_key_here" .env 2>/dev/null; then
    echo -e "${RED}❌ FIRECRAWL_API_KEY가 설정되지 않음${NC}"
    FIRECRAWL_OK=false
else
    echo -e "${GREEN}✅ FIRECRAWL_API_KEY 설정됨${NC}"
    FIRECRAWL_OK=true
fi

echo ""

# 최종 상태
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

if [ "$GEMINI_OK" = true ] && [ "$FIRECRAWL_OK" = true ]; then
    echo -e "${GREEN}"
    echo "✅ 설치 완료! 바로 사용 가능합니다."
    echo -e "${NC}"
    echo "사용법:"
    echo "  python web-crawler.py <URL>"
    echo ""
    echo "예시:"
    echo "  python web-crawler.py https://example.com/article"
else
    echo -e "${YELLOW}"
    echo "⚠️ API 키 설정이 필요합니다."
    echo -e "${NC}"
    echo "다음 단계:"
    echo "  1. nano .env"
    echo "  2. API 키 입력"
    echo "  3. python web-crawler.py <URL>"
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
