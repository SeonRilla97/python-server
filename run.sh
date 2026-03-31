#!/bin/bash
# FastAPI 애플리케이션 실행 스크립트
echo "Starting FastAPI app..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
