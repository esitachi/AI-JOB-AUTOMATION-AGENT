# 🤖 AI Web Automation Agent

An AI-powered agent that automates job application workflows using **FastAPI, Playwright, and OpenAI**.

---

## ⭐ Key Features
- AI‑generated automation plans (GPT models)
- Clean Web UI for planning & execution
- Automates job applications (Indeed, Naukri, etc.)
- Playwright Chromium automation
- Works even without OpenAI API key (fallback mode)
- FastAPI backend with automatic docs
- Real‑time execution tracking

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Install Playwright browser
```bash
playwright install chromium
```

### 3. (Optional) Create `.env`
```
OPENAI_API_KEY=your-key
OPENAI_MODEL=gpt-4o-mini
JOB_EMAIL=your-email
JOB_NAME=Your Name
```

### 4. Run server
```bash
uvicorn app.main_ai_agent:app --reload
```

Open: **http://127.0.0.1:8000/**

---

## 💻 How to Use
1. Enter job title, location, target sites
2. Click **Generate Plan**
3. Review the AI-generated steps
4. Click **Execute Plan**
5. Watch real-time automation in the UI

---

## 🧩 API Endpoints
- **POST /plan** – generate automation plan  
- **POST /execute** – execute plan  
- **GET /docs** – Swagger documentation  

---

## 📁 Project Structure
```
app/
  main_ai_agent.py
  planner.py
  executor.py
  browser.py
  schemas.py
  config.py
static/
  index.html
requirements.txt
README.md
```

---

## ⚙️ Tech Stack
- Python, FastAPI, Pydantic  
- Playwright (Chromium)  
- OpenAI GPT Models  
- HTML, CSS, JS  

---

## 🛠️ Development
```bash
uvicorn app.main_ai_agent:app --reload --host 0.0.0.0 --port 8000
```

---

##  Credits
Made using Python, FastAPI, Playwright & OpenAI.
