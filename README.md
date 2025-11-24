# 🤖 AI Web Automation Agent

An intelligent web automation agent that uses AI to create and execute browser automation plans for job applications. Built with FastAPI, Playwright, and OpenAI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **AI-Powered Planning**: Uses OpenAI GPT models to generate intelligent automation plans based on job requirements
- **Interactive Web UI**: Beautiful, modern frontend with real-time status updates and progress tracking
- **Multi-Site Support**: Automate job applications across multiple job boards (Indeed, Naukri, etc.)
- **Playwright Automation**: Robust browser automation with Chromium
- **Fallback Mode**: Works even without OpenAI API key using intelligent fallback plans
- **RESTful API**: Clean FastAPI backend with automatic documentation
- **Real-time Execution**: Watch automation steps execute in real-time

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) OpenAI API key for AI-powered planning

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-web-automation-agent
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**
   ```bash
   playwright install chromium
   ```

4. **Configure environment variables** (Optional)
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your-openai-api-key-here
   OPENAI_MODEL=gpt-4o-mini
   JOB_EMAIL=your-email@example.com
   JOB_NAME=Your Name
   ```

### Running the Application

1. **Start the backend server**
   ```bash
   uvicorn app.main_ai_agent:app --reload
   ```

2. **Open your browser**
   
   Navigate to `http://127.0.0.1:8000/`

3. **Use the web interface**
   - Enter job title, location, and target sites
   - Click "Generate Plan" to create an automation plan
   - Review the generated steps
   - Click "Execute Plan" to run the automation

## 📖 Usage

### Web Interface

1. Fill in the form:
   - **Job Title**: e.g., "Senior Automation Engineer"
   - **Location**: e.g., "Bengaluru"
   - **Target Sites**: Comma-separated list (e.g., "indeed.com, naukri.com")

2. Generate a plan by clicking "Generate Plan"
   - The AI will create a step-by-step automation plan
   - Review the steps in the plan preview panel

3. Execute the plan by clicking "Execute Plan"
   - Playwright will open a browser window
   - Watch the automation execute each step
   - Check the execution log for status updates

### API Endpoints

#### `POST /plan`

Generate an automation plan based on job requirements.

**Request Body:**
```json
{
  "job_title": "Senior Automation Engineer",
  "location": "Bengaluru",
  "target_sites": ["indeed.com", "naukri.com"]
}
```

**Response:**
```json
{
  "steps": [
    {
      "id": 1,
      "action": "open_site",
      "params": {"url": "https://indeed.com"}
    },
    {
      "id": 2,
      "action": "search_jobs",
      "params": {"keywords": "Senior Automation Engineer", "location": "Bengaluru"}
    },
    ...
  ]
}
```

#### `POST /execute`

Execute a generated automation plan.

**Request Body:**
```json
{
  "steps": [
    {
      "id": 1,
      "action": "open_site",
      "params": {"url": "https://indeed.com"}
    },
    ...
  ]
}
```

**Response:**
```json
{
  "status": "ok",
  "message": "Execution finished on server"
}
```

#### `GET /docs`

Interactive API documentation (Swagger UI) available at `http://127.0.0.1:8000/docs`

## 🏗️ Project Structure

```
ai-web-automation-agent/
├── app/
│   ├── __init__.py
│   ├── main_ai_agent.py      # FastAPI application and routes
│   ├── planner.py             # AI-powered plan generation
│   ├── executor.py            # Plan execution orchestrator
│   ├── browser.py             # Playwright browser automation
│   ├── schemas.py             # Pydantic data models
│   └── config.py              # Configuration and environment variables
├── static/
│   └── index.html             # Interactive web frontend
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (create this)
└── README.md                  # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPENAI_API_KEY` | OpenAI API key for AI planning | None | No (uses fallback) |
| `OPENAI_MODEL` | OpenAI model to use | `gpt-4o-mini` | No |
| `JOB_EMAIL` | Default email for job applications | `eshaanhegde29@gmail.com` | No |
| `JOB_NAME` | Default name for job applications | `Eshaan Hegde` | No |

### Supported Actions

The automation supports the following actions:

- **`open_site`**: Navigate to a URL
  ```json
  {"url": "https://example.com"}
  ```

- **`search_jobs`**: Search for jobs on a job board
  ```json
  {"keywords": "Software Engineer", "location": "Remote"}
  ```

- **`open_job`**: Open a specific job listing
  ```json
  {"job_index": 0}
  ```

- **`fill_form`**: Fill out a job application form
  ```json
  {}
  ```

## 🎨 Features

### Frontend Features

- **Modern UI**: Glassmorphism design with gradient backgrounds
- **Real-time Updates**: Live status indicators and progress tracking
- **Toast Notifications**: User-friendly success/error messages
- **Responsive Design**: Works on desktop and mobile devices
- **Interactive Plan Preview**: Visual step-by-step plan display
- **Execution Logs**: Real-time execution status updates

### Backend Features

- **AI Integration**: OpenAI GPT models for intelligent planning
- **Fallback Mode**: Works without API key using rule-based plans
- **Error Handling**: Comprehensive error handling and logging
- **CORS Support**: Cross-origin resource sharing enabled
- **Auto-reload**: Development server with hot reload

## 🛠️ Technologies Used

- **Backend**:
  - [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
  - [Uvicorn](https://www.uvicorn.org/) - ASGI server
  - [Pydantic](https://docs.pydantic.dev/) - Data validation
  - [OpenAI](https://platform.openai.com/) - AI planning
  - [Playwright](https://playwright.dev/python/) - Browser automation

- **Frontend**:
  - Vanilla JavaScript (ES6+)
  - Modern CSS (Grid, Flexbox, Animations)
  - Fetch API for HTTP requests

## 📝 Development

### Running in Development Mode

```bash
uvicorn app.main_ai_agent:app --reload --host 0.0.0.0 --port 8000
```

### Adding New Actions

1. Add the action handler in `app/browser.py`:
   ```python
   def your_action(self, param1: str, param2: int):
       # Your automation logic
       pass
   ```

2. Register it in `run_step()`:
   ```python
   elif action == "your_action":
       self.your_action(params["param1"], params["param2"])
   ```

3. Update the planner prompt in `app/planner.py` to include the new action

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is for educational and personal use only. Always respect website terms of service and robots.txt files. Use responsibly and ethically.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Playwright](https://playwright.dev/) for robust browser automation
- [OpenAI](https://openai.com/) for AI capabilities

## 📧 Support

For issues, questions, or contributions, please open an issue on GitHub.

---

Made with ❤️ using Python, FastAPI, and Playwright

