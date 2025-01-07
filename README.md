# Interactive Quiz Backend
This is a Flask-based backend application for managing an interactive quiz. The application supports user registration, login, quiz creation, and result tracking.

## Features
User Authentication: Secure user registration and login using hashed passwords and JWT-based authentication.
Question Management: Fetch multiple-choice questions with answers.
Quiz Submission: Calculate and store user quiz scores.
Results Tracking: Retrieve past quiz scores for a user.
## Getting Started
Prerequisites
Python 3.7 or higher
Virtual environment (optional, but recommended)
Flask and related dependencies (see requirements.txt)
## Installation
1. Clone the repository:

```bash
git clone <repository_url>
cd interactive-quiz-backend
```
2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip3 install -r requirements.txt
```
4. Run this command on your terminal
```bash
export FLASK_APP="app:create_app"
```
5. Set up the database:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
6. Run the development server:

```bash
python3 run.py
```
## Configuration
You can configure the application using environment variables or by editing the config.py file. Here are the key settings:

SECRET_KEY: Used for securing JWT tokens.
DATABASE_URL: Database connection string (default is SQLite).
## API Endpoints
#### Authentication
* Register:

<mark>POST /register</mark>

#### Request body:

```json
{
  "username": "example",
  "password": "password123"
}
```
#### Response:

```json
{
  "message": "User registered successfully"
}
```
* Login:

<mark>POST /login</mark>

#### Request body:

```json
{
  "username": "example",
  "password": "password123"
}
```
#### Response:

```json
{
  "token": "your-jwt-token"
}
```
#### Quiz Management
* Fetch Questions:

<mark>GET /questions</mark>

#### Response:

```json
[
  {
    "id": 1,
    "question": "What is the capital of France?",
    "options": ["Paris", "London", "Berlin", "Madrid"]
  }
]
```
* Submit Quiz:

<mark>POST /quiz/submit</mark>

#### Request body:

```json
{
  "answers": [
    { "id": 1, "answer": "Paris" },
    { "id": 2, "answer": "Berlin" }
  ]
}
```
#### Response:

```json
{
  "score": 2
}
```
* View Results:
<mark>GET /results</mark>

#### Response:

```json
[
  { "score": 5, "timestamp": "2025-01-07T14:23:45.123Z" }
]
```
## Folder Structure

```plaintext
interactive-quiz-backend/
│
├── app/
│   ├── __init__.py      # Application setup
│   ├── models.py        # Database models
│   ├── routes.py        # API routes
│   ├── utils.py         # Helper functions (if needed)
│
├── migrations/          # Flask-Migrate files
│
├── config.py            # Configuration file
├── run.py               # Entry point to run the app
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```
## Technologies Used
* Flask: Web framework
* Flask-SQLAlchemy: Database ORM
* Flask-Migrate: Database migrations
* Flask-JWT-Extended: JWT-based authentication
* SQLite: Default database
## Future Improvements
* Add an admin panel for managing questions.
* Implement real-time quiz sessions.
* Add support for multiple quizzes and categories.
* Integrate front-end with React or Vue.js.
## Author
Developed by Bassel Saleh.

Email: basselh26@gmail.com
Feel free to reach out with questions or suggestions!

## License
This project is licensed under the MIT License.

##### Let me know if you'd like any changes or additional details!
