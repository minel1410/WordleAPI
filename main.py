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
        return {
            "guess": guess_word,
            "was_correct": True,
            "was_word_in_list": True,
        }

    # Check if the word in the word list
    word_list = get_word_list()
    if guess_word.lower() in word_list:
        return {
            "guess": guess_word,
            "was_correct": False,
            "was_word_in_list": False,
        }

    # Check the word against the answer
    guess_result = []
    # Calculate guess_word
    for c in guess_word:
        guess_result.append(check_character(c, word_of_the_day))
    return {
        "guess": guess_word,
        "was_correct": False,
        "was_word_in_list": True,
        "character_info": guess_result,
    }


"""
uvicorn main:app --reload --port 5000
"""
