from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class LogEntry(Base):
    __tablename__ = "log_entries"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    log_level = Column(String(50), index=True)  # e.g., INFO, ERROR, WARNING
    message = Column(Text, nullable=False)      # The raw log text
    ai_analysis = Column(Text, nullable=True)   # The GenAI analysis result later on