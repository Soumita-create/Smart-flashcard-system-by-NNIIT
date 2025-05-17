# Smart-flashcard-system-by-NNIIT
# Flashcards API

This is a simple backend API built with FastAPI for managing flashcards. It supports adding flashcards with automatic subject classification and retrieving mixed-subject flashcards for a specific student.

## Features

- Add a flashcard with question, answer, and student ID
- Automatically classify the subject of a flashcard based on its question
- Retrieve a mix of flashcards from different subjects for a student
- Built with FastAPI and SQLAlchemy (SQLite database)

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic

# Run the app with
uvicorn main:app --reload

# Project Structure
main.py — FastAPI app with endpoints

database.py — SQLAlchemy database setup

models.py — SQLAlchemy models for flashcards

schemas.py — Pydantic schemas for request and response validation

subject_classifier.py — logic to classify the subject of flashcards
