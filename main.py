from typing import List, Optional
from algop import bubbleSort, insertionSort
from fastapi import FastAPI, Query
app = FastAPI(
    title="Algop",
    description="Common Algorithms",
    version="1.0.1",
    contact={"url":"https://isahaji.com","name": "Isa Haji", "email": "isa@isahaji.com"}
)


@app.get('/')
async def main():
    return "Welcome to Algop API"


@app.get("/bubble/")
async def bubblesort(q: Optional[List[str]] = Query(None)):
    return {"array": bubbleSort(q)}


@app.get('/insertion')
async def insertionsort(q: Optional[List[str]] = Query(None)):
    return {"array": insertionSort(q)}
