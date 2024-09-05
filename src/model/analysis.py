from transformers import pipeline


class SentimentAnalysis:
    def __init__(self, prompt):
        self.prompt = prompt
        self.pipe = pipeline(task='sentiment-analysis')
        

    def get_sentiment(self):
       response=self.pipe(self.prompt)
       label=response[0]['label']
       score=response[0]['score']
       return {'label':label,'score':score}