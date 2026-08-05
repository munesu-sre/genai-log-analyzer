# 1. Base image: Use lightweight official Python 3.11 runtime
FROM python:3.11-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy dependencies list first (enables layer caching)
COPY requirements.txt .

# 4. Install dependencies without saving temp installer cache
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code into /app
COPY . .

# 6. Expose the default FastAPI port for documentation
EXPOSE 8000

# 7. Default container launch command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]