from fastapi import FastAPI, HTTPException, status
from schemas import LogEntryRequest, ParsedLogResponse
from parser import parse_raw_log

app = FastAPI(title="Enterprise GenAI Log Analyzer")

@app.post(
    "/api/v1/logs/parse", 
    response_model=ParsedLogResponse,
    status_code=status.HTTP_200_OK
)
async def parse_log_endpoint(payload: LogEntryRequest):
    if not payload.raw_log.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Raw log line cannot be empty."
        )

    timestamp, level, service, message, metadata = parse_raw_log(payload.raw_log)

    return ParsedLogResponse(
        timestamp=timestamp,
        level=level,
        service=service,
        message=message,
        metadata=metadata
    )