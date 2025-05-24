# api.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load CSV data once
df = pd.read_csv("marks.csv")

@app.get("/api")
async def get_marks(name: list[str] = []):
    results = []
    for n in name:
        row = df[df['name'] == n]
        if not row.empty:
            results.append(int(row['marks'].values[0]))
        else:
            results.append(None)
    return {"marks": results}
