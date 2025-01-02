from model.analysis import SentimentAnalysis
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class RequestModel(BaseModel):
    prompt:str


@app.post('/sentiment')
def get_sentiment(request:RequestModel):
    prompt=request.prompt
    sentiment=SentimentAnalysis(prompt)
    return sentiment.get_sentiment()




