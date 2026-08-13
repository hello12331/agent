# 📖 Technical Master User Guide — GenMitra Autonomous LinkedIn AI System

Welcome to the comprehensive technical documentation for **GenMitra**, an autonomous AI content research, copywriting, scheduling, and analytics engine built for LinkedIn.

---

## 📋 Table of Contents
1. [Prerequisites](#-prerequisites)
2. [Environment Configuration (`.env`)](#-environment-configuration-env)
3. [LinkedIn Developer Portal Setup](#-linkedin-developer-portal-setup)
4. [Command-Line Interface (CLI) Guide](#-command-line-interface-cli-guide)
5. [Web Dashboard & Control Panel](#-web-dashboard--control-panel)
6. [Automated Daily Pipeline Schedule](#-automated-daily-pipeline-schedule)
7. [REST API Documentation](#-rest-api-documentation)
8. [Troubleshooting & Common Issues](#-troubleshooting--common-issues)

---

## ⚙️ Prerequisites
- **Python**: Version 3.10+ or 3.11+
- **Google Gemini API Key**: Free tier or paid key from [Google AI Studio](https://aistudio.google.com/)
- **LinkedIn Account & App**: OAuth Access Token & Person URN

---

## 🔑 Environment Configuration (`.env`)

Create a `.env` file in the root directory using `.env.example` as a reference:

```env
# Core AI Credentials
GEMINI_API_KEY=your_gemini_api_key_here

# LinkedIn API Credentials
LINKEDIN_ACCESS_TOKEN=your_linkedin_oauth_access_token
LINKEDIN_PERSON_URN=urn:li:person:YOUR_MEMBER_ID

# Optional News & Trend Sources
X_BEARER_TOKEN=
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
NEWS_API_KEY=

# Application & Schedule Settings
TIMEZONE=Asia/Kolkata
BRAND_NAME=GenMitra AI
CONTENT_NICHE=Artificial Intelligence, Technology, Business, Startups
DASHBOARD_PORT=5000
DASHBOARD_SECRET_KEY=dev-secret-key-change-in-production
```

---

## 🚀 Command-Line Interface (CLI) Guide

```bash
# Start background daemon scheduler
python main.py

# Run full pipeline immediately (Research -> Generate -> Preview)
python main.py --run-now

# Test individual components
python main.py --test-research
python main.py --test-generate
python main.py --test-publish 1

# Launch Flask control dashboard
python main.py --dashboard
```

---

## 🔌 REST API Documentation

- `GET /api/status`: System status and API health.
- `GET /api/posts/today`: Current day's generated posts.
- `GET /api/posts/<date>`: Specific date's posts (`YYYY-MM-DD`).
- `GET /api/logs`: Last 60 system execution log events.
- `GET /api/analytics`: Overview analytics and engagement metrics.

---

## 🛡️ License
Distributed under the MIT License. Copyright (c) 2026 Manohar Challa.
