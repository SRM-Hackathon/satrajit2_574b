# Moodx

A chat-based recommendation system API utilizing facial and voice input to recommend something dependent on the **mood**!  

## Dependencies

- python3 (version 3.6.x)
- python3-pip
- virtualenv

## Setup Environment

1. Go to backend directory ```cd project-dir-path/backend```
2. Create virtual environment ```python3 -m venv venv```
3. Activate virtual environment ```source venv/bin/activate```
4. Install dependencies ```pip3 install -r requirements.txt```
5. Go to codebase (moodx) directory ```cd moodx```
6. Make migrations ```python3 manage.py makemigrations```
7. Migrate ```python3 manage.py migrate```
8. Start the server ```python3 manage.py runserver```
9. Now go to browser at **localhost:8000**
