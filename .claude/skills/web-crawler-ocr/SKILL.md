---
name: web-crawler-ocr
description: 웹페이지 크롤링 + 이미지 OCR 자동 분석. "이 URL 분석해줘", "크롤링해줘", "웹사이트 분석", "사이트 크롤링", "경쟁사 분석", "페이지 추출", "analyze this URL", "crawl website", "competitor analysis", "extract webpage" 등을 언급하거나 https:// 또는 http:// URL을 제공하면 자동 실행. Claude의 5MB 이미지 제한을 Gemini OCR(20MB)로 우회.
allowed-tools: Bash, Read, Write
---

# Web Crawler + Gemini OCR Skill

Extract complete web page content (text + images) and save as markdown file.

## When to Use This Skill

This skill automatically activates when the user:
- Provides a URL: "https://example.com analyze this"
- Requests web crawling: "crawl this website", "extract webpage content"
- Mentions competitor analysis: "analyze competitor site"
- Needs image OCR from web: "OCR images from this page"
- Wants to bypass 5MB limit: "large images on this site"

## What This Skill Does

1. **Firecrawl**: Clean text extraction (removes ads/clutter)
2. **Gemini OCR**: Extract text from images (up to 20MB per image)
3. **Complete Markdown**: Text + image analysis in one file

## Instructions

### Step 1: Identify the URL
Extract URL(s) from user message:
- Look for `https://` or `http://`
- Multiple URLs? Process each one

### Step 2: Determine Output Location

Based on user context, choose appropriate path:

**Competitor Analysis:**
```
/Users/rhim/Projects/pkm/50-resources/competitor-analysis/
```

**Educational Reference (e.g. HFK):**
```
/Users/rhim/Projects/pkm/10-projects/12-education/{project-folder}/
```

**General Web Research:**
```
/Users/rhim/Projects/pkm/50-resources/web-research/
```

**Filename:** Use domain + timestamp or user-specified name.

### Step 3: Execute Web Crawler Script

**WSL Path:**
```bash
cd /home/rhim/claude-projects/imi-workspace/.claude/skills/web-crawler-ocr/scripts && \
python3 web-crawler.py "<URL>" "<output-path>"
```

**Mac Path:**
```bash
cd /Users/rhim/Projects/imi-workspace/.claude/skills/web-crawler-ocr/scripts && \
python3 web-crawler.py "<URL>" "<output-path>"
```

**Important:**
- Scripts are now located within the skill folder
- Always use full absolute paths for output
- Quote URLs to handle special characters
- Ensure output directory exists (create with `mkdir -p` if needed)
- Virtual environment setup: Run `bash setup.sh` in scripts folder first time

### Step 4: Read and Analyze Results

1. Use Read tool to open generated markdown file
2. Extract key insights
3. Summarize for user

### Step 5: Suggest Next Steps

- Additional URLs to analyze?
- Comparative analysis needed?
- PKM organization suggestions?

## Examples

### Example 1: Competitor Cafe Analysis

**User:** "Analyze this competitor cafe website: https://competitor-cafe.com"

**Claude Actions:**
```bash
# 1. Ensure directory exists
mkdir -p /Users/rhim/Projects/pkm/50-resources/competitor-analysis

# 2. Run crawler (Mac)
cd /Users/rhim/Projects/imi-workspace/.claude/skills/web-crawler-ocr/scripts && \
python3 web-crawler.py \
    "https://competitor-cafe.com" \
    /Users/rhim/Projects/pkm/50-resources/competitor-analysis/competitor-cafe-20251029.md

# 3. Read results (use Read tool)
# 4. Provide analysis
```

**Response:**
"Crawled competitor website successfully. Extracted 3,500 characters + 5 images with OCR.

Key insights:
1. Brand positioning: ...
2. Menu structure: ...
3. Differentiators: ..."

### Example 2: HFK Reference Material

**User:** "Analyze HFK AI team page: https://hfk.me/ai-team"

**Claude Actions:**
```bash
mkdir -p /Users/rhim/Projects/pkm/10-projects/12-education/12.06-hfk-winter-ai

cd /Users/rhim/Projects/imi-workspace/.claude/skills/web-crawler-ocr/scripts && \
python3 web-crawler.py \
    "https://hfk.me/ai-team" \
    /Users/rhim/Projects/pkm/10-projects/12-education/12.06-hfk-winter-ai/hfk-ai-team-reference.md
```

### Example 3: Multiple URLs

**User:** "Analyze these 3 competitor sites:
- https://cafe-a.com
- https://cafe-b.com
- https://cafe-c.com"

**Claude:** Process each URL sequentially, then provide comparative analysis.

## Environment Setup

### Required Environment Variables

This skill requires two API keys:

```bash
export GEMINI_API_KEY="your_gemini_key_here"
export FIRECRAWL_API_KEY="your_firecrawl_key_here"
```

### Alternative: .env File

Create `.env` in the scripts folder:

**WSL:**
```bash
cd /home/rhim/claude-projects/imi-workspace/.claude/skills/web-crawler-ocr/scripts
cp .env.example .env
# Edit .env with your actual API keys
```

**Mac:**
```bash
cd /Users/rhim/Projects/imi-workspace/.claude/skills/web-crawler-ocr/scripts
cp .env.example .env
# Edit .env with your actual API keys
```

### Initial Setup

Run setup script once to install dependencies:

```bash
cd /home/rhim/claude-projects/imi-workspace/.claude/skills/web-crawler-ocr/scripts
bash setup.sh
```

### Check Setup

```bash
# Verify .env file exists
cat .claude/skills/web-crawler-ocr/scripts/.env

# Test script
cd .claude/skills/web-crawler-ocr/scripts && python3 web-crawler.py --help
```

## Limitations

- **Gemini Free Tier**: 15 requests per minute
- **Firecrawl Free Tier**: 500 credits
- **Image Limit**: Maximum 10 images per page
- **File Size**: 20MB per image maximum

## Troubleshooting

### API Key Errors

```bash
# Check if keys are set
echo $GEMINI_API_KEY
echo $FIRECRAWL_API_KEY

# Set if missing
export GEMINI_API_KEY="your_key"
export FIRECRAWL_API_KEY="your_key"
```

### Python Package Errors

```bash
cd .claude/skills/web-crawler-ocr/scripts
bash setup.sh
```

Or manually:
```bash
pip install -r .claude/skills/web-crawler-ocr/scripts/requirements.txt
```

### Script Not Found

Verify script location:
```bash
ls -la .claude/skills/web-crawler-ocr/scripts/web-crawler.py
```

## Script Location

**All scripts are now contained within the skill folder:**

- **Main Script**: `.claude/skills/web-crawler-ocr/scripts/web-crawler.py`
- **OCR Script**: `.claude/skills/web-crawler-ocr/scripts/gemini-ocr.py`
- **Config Example**: `.claude/skills/web-crawler-ocr/scripts/.env.example`
- **Setup Script**: `.claude/skills/web-crawler-ocr/scripts/setup.sh`
- **Dependencies**: `.claude/skills/web-crawler-ocr/scripts/requirements.txt`
- **Documentation**: `.claude/skills/web-crawler-ocr/README.md`

## Inspired By

Noah Brier's Claudesidian project:
- Firecrawl for web research
- Gemini for large image/PDF analysis
- Unix philosophy: simple composable tools

## Version History

- **v1.1.0 (2025-11-10)**: Unified skill structure
  - Moved all scripts into `.claude/skills/web-crawler-ocr/scripts/`
  - Follows Claude Code Skills official best practices
  - Self-contained skill folder (no external dependencies)
  - Added setup.sh and .env.example
- **v1.0.0 (2025-10-29)**: Initial skill creation
  - Firecrawl + Gemini OCR integration
  - Model-invoked automation
  - PKM-aware file organization
