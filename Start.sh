#!/usr/bin/env bash

echo "Lancement de l'application FastAPI via Uvicorn..."
uvicorn app.main:app --host 0.0.0.0 --port 10000
