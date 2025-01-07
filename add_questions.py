from app import create_app, db
from app.models import Question

app = create_app()

with app.app_context():
    # Define the questions
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Venus", "Jupiter"],
            "correct_answer": "Mars"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"],
            "correct_answer": "Blue Whale"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Shakespeare", "Dickens", "Austen", "Hemingway"],
            "correct_answer": "Shakespeare"
        }
    ]
    
    # Add each question to the database
    for q in questions:
        question = Question(
            question=q["question"],
            options=q["options"],
            correct_answer=q["correct_answer"]
        )
        db.session.add(question)

    # Commit changes to the database
    db.session.commit()

    print("Questions added successfully!")
