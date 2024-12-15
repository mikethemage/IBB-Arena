#!/bin/bash
source .venv/bin/activate
cd api
uvicorn api:app --reload --host 0.0.0.0 --port 8000
