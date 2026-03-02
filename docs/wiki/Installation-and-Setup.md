# Installation and Setup

Get EAIS running locally in just a few minutes.

## 📋 Prerequisites
- Python 3.9+
- OpenAI API Key (for LLM orchestration)
- Serper API Key (optional, for web-searching agents)

## 🛠️ Step-by-Step Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/ruchirhuchgol-del/EAIS.git
    cd EAIS
    ```

2.  **Environment Setup**:
    Create a `.env` file from the example:
    ```bash
    cp .env.example .env
    ```
    Add your `OPENAI_API_KEY` to the `.env` file.

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch the System**:
    ```bash
    python run_streamlit_app.py
    ```

## 🐳 Docker Support
Launch all EAIS services using Docker Compose:
```bash
docker-compose up --build
```
- **Streamlit UI**: http://localhost:8501
- **API**: http://localhost:8000
