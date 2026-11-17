
# MultiLingua AI

An intelligent multilingual campus support classification system.

## Supported Languages
- English
- Hindi
- Hinglish
- Punjabi

## Machine Learning
- TF-IDF
- Word-level features
- Character-level features
- Linear Support Vector Machine
- Probability Calibration

## Backend
- Python
- FastAPI
- SQLite

## Frontend
- Streamlit

## Features
- Multilingual text classification
- Department routing
- Confidence estimation
- Human-in-the-loop review
- Prediction history

## Run Backend

uvicorn main:app --reload --app-dir backend

## Run Frontend

streamlit run frontend/app.py
