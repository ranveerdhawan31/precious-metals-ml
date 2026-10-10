# Learning Notes

## Session 1: Project Setup

### What I Set Up

- Created the project folder
- Created and activated a Python virtual environment
- Selected the virtual environment in VS Code
- Installed Streamlit and its dependencies
- Created the first Streamlit application
- Created a `.gitignore` file
- Created `requirements.txt`
- Created the project README

### Concepts I Learned

#### Virtual Environment

A virtual environment gives the project an isolated Python installation and package environment. The `.venv` folder contains the Python interpreter and packages used by this project.

#### Streamlit

Streamlit converts Python code into an interactive web application. The current application entry point is `app.py`.

#### Localhost

`localhost:8501` is the local address where the Streamlit application runs on this Mac. Other internet users cannot access it yet.

#### Deployment

Deployment means publishing the application to a public server so that recruiters and other users can open it through a public URL.

#### requirements.txt

`requirements.txt` records the Python packages needed to recreate the project environment.

#### .gitignore

`.gitignore` tells Git not to track generated or sensitive files such as `.venv`, `.env`, and Streamlit secrets.

### Important Commands

```text
python3 -m venv .venv
source .venv/bin/activate
python -m pip install streamlit
python -m streamlit run app.py
python -m pip freeze > requirements.txt