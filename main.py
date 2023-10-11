from utils import *

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

word_of_the_day: str = get_word_of_the_day()


@app.get("/")
def read_root():
    return {"ping": "Pong!"}


@app.get("/answer")
def read_root():
    return {"word": word_of_the_day}


@app.post("/{word}")
def send_guess_word(word: str):
    guess_word = word.upper()
    if guess_word == word_of_the_day:
        return {"game_won": True}

    # Check if the word in the word list
    word_list = get_word_list()
    if not binary_search(word_list, 0, len(word_list) - 1, guess_word.lower()):
        return {
            "game_won": False,
            "result": f"{guess_word} is not in the word list"}

    # Check the word against the answer
    guess_result = []
    # Calculate guess_word
    for c in guess_word:
        guess_result.append(check_character(c, word_of_the_day))
    return {
        "game_won": False,
        "result": guess_result}


"""
uvicorn main:app --reload --port 5000
"""
