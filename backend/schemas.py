from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any

class LogEntryRequest(BaseModel):
    raw_log: str = Field(..., example="2026-08-05 14:32:10 [WARN] PaymentGateway: Timeout while connecting to host 192.168.1.45")

class ParsedLogResponse(BaseModel):
    timestamp: Optional[datetime] = None
    level: str
    service: str
    message: str
    metadata: Dict[str, Any] = {}