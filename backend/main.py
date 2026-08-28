import ollama  # <-- 1. Add this import at the very top
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models

# Initialize the FastAPI app
app = FastAPI(title="GenAI Log Analyzer")

# 1. Root health check endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the GenAI Log Analyzer API!"}

# 2. Endpoint to create a new log entry (Updated with Ollama!)
@app.post("/logs/")
def create_log(log_level: str, message: str, db: Session = Depends(get_db)):
    
    # Ask local Ollama (Llama 3) to analyze the log message
    try:
        response = ollama.chat(
            model='llama3', 
            messages=[
                {
                    'role': 'system',
                    'content': 'You are a technical log analyzer. Provide a brief, one-sentence diagnosis or summary of the following log message.'
                },
                {
                    'role': 'user',
                    'content': message
                },
            ]
        )
        ai_insight = response['message']['content']
    except Exception as e:
        ai_insight = f"AI analysis unavailable: {str(e)}"

    # Create a new LogEntry database object, including the AI analysis
    db_log = models.LogEntry(
        log_level=log_level, 
        message=message,
        ai_analysis=ai_insight  # <-- Saving the AI result into your database model
    )
    
    # Add it to the active database session
    db.add(db_log)
    
    # Commit the changes to save it permanently in PostgreSQL
    db.commit()
    
    # Refresh so we get back the auto-generated ID, timestamp, and AI analysis
    db.refresh(db_log)
    
    return {"status": "success", "data": db_log}

# 3. Endpoint to view all saved logs
@app.get("/logs/")
def get_logs(db: Session = Depends(get_db)):
    # Query all records from the log_entries table
    logs = db.query(models.LogEntry).all()
    return logs