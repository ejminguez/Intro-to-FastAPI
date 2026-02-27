from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, I am Francis Reid <3"}

@app.get("/greet")
def greet(name: str = "friend"):
    return {"message": f"Hey {name}! You're Cute!!"}

@app.get("/compliment")
def compliment(name: str = "friend"):
    compliments = [
        "You're amazing!",
        "You light up the room!",
        "Your code is top-notch!",
        "You have great taste in music!",
        "You are unstoppable!"
    ]
    return {"message": f"Hey {name}, {random.choice(compliments)}"}
