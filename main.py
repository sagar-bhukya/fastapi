from fastapi import FastAPI

app =FastAPI()


@app.get('/')
def index():
    return "Hi sagar"

@app.get('/about')
def about():
    return {'data':{"sagar","bhukya"}}