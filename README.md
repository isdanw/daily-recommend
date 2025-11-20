# Daily Recommendation System

This is a daily recommendation system that provides personalized suggestions for outfits, diets, and lucky colors based on user preferences and weather conditions.

## Features

- Personalized outfit recommendations based on weather and user preferences
- Diet suggestions tailored to individual needs
- Lucky color calculation based on birthdate
- Weather integration for contextual recommendations
- AI-powered image generation for outfit visualization

## Tech Stack

- Backend: Python/FastAPI
- Frontend: HTML/CSS/JavaScript
- Database: SQLite
- APIs: QWeather API, DashScope AI API
- Deployment: Render

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - `QWEATHER_API_KEY`: Your QWeather API key
   - `DASHSCOPE_API_KEY`: Your DashScope API key

4. Run the server:
   ```
   python main.py
   ```

### Frontend Setup

Open `frontend/index.html` in a web browser.

## Deployment

The application is deployed on Render. The deployment script is located at `backend/deploy_to_render.sh`.

## Recent Fixes

- Fixed hardcoded API keys in the code
- Improved error handling for weather and image APIs
- Fixed date parsing issues in fortune calculation
- Removed external dependencies (pybazi) for better portability
- Fixed database query issues in recommendation modules
- Updated Git authentication to use personal access tokens