# 🤖 GenAI Chatbot

A simple chatbot application built as part of my exploration of **Generative AI and LLM-based applications**.

This is an introductory, tutorial-based project created to understand the basic workflow of building a chatbot application, connecting it with an LLM, and creating a simple user interface using Streamlit.

## 🎯 Purpose

The main purpose of this project is learning and experimentation.

Through this project, I am getting familiar with:

* Generative AI fundamentals
* LLM API integration
* Building a basic chatbot
* Managing Python dependencies with `uv`
* Creating a simple UI with Streamlit
* Working with environment variables and API keys
* Structuring a Python-based GenAI project

## ✨ Features

* 💬 Basic conversational chatbot
* 🤖 LLM-powered responses
* 🖥️ Streamlit-based user interface
* 🔐 API configuration through environment variables
* 🐍 Python-based implementation

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Generative AI / LLM API**
* **uv** – Python package and project management

## 📁 Project Structure

```text
Chatbot/
│
├── chatmodel/
│   ├── chat.py
│   ├── chatbot.py
│   └── UI chatbot.py
│
├── src/
│   └── gen_ai/
│       └── __init__.py
│
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/aman-devTech/Chatbot.git
cd Chatbot
```

### 2. Install dependencies

This project uses `uv` for Python project and dependency management.

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project directory and add the required API credentials.

For example:

```env
API_KEY=your_api_key_here
```

> **Important:** Never commit your `.env` file or expose API keys in your repository.

### 4. Run the application

Run the Streamlit application using the appropriate UI file:

```bash
streamlit run "path/to/UI chatbot.py"
```

Replace the path with the actual location of the Streamlit UI file in your local project.

## 📚 Learning Note

This project was created while following a Generative AI tutorial and experimenting with the concepts demonstrated in it.

The project is intentionally basic and is primarily intended for **learning, experimentation, and documenting my progress while exploring the GenAI field**.

The user interface was created with assistance from **ChatGPT**.

This project serves as an initial step toward exploring more advanced GenAI concepts such as:

* Prompt Engineering
* LangChain
* Retrieval-Augmented Generation (RAG)
* LangGraph
* AI Agents
* Agentic AI

## 🚧 Future Exploration

As I continue learning Generative AI, I plan to build more projects that go beyond this introductory chatbot and explore more advanced LLM application architectures.

---

**Learning Generative AI — one project at a time. 🚀**
