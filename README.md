# Wordle api

A simple API to host your own Wordle. By default, this word list uses https://github.com/Kinkelin/WordleCompetition/blob/main/data/official/combined_wordlist.txt 

## Usage

To find out the answer for today's wordle, you can make a GET request to https://wordle-api-kappa.vercel.app/answer.

To consume the API, Send a POST request to `https://wordle-api-kappa.vercel.app/{GUESS}`.
eg: https://wordle-api-kappa.vercel.app/quote where `quote` is the guessed word

### Response
 If the guess word is correct the API response will be 
```json
{
  "guess": "QUOTE",
  "is_correct": true,
  "is_word_in_list": true
}
```
if the word is not in the word list, the API response will be
```json
{
  "guess": "ABCDE",
  "is_correct": false,
  "is_word_in_list": false
}
```
else if the guessed word is in the list but the guess is incorrect, the API response will be
```json
{
  "guess": "QUOTE",
  "is_correct": false,
  "is_word_in_list": true,
  "character_info": [
    {
      "char": "Q",
      "scoring": {
        "in_word": false,
        "correct_idx": false
      }
    },
    {
      "char": "U",
      "scoring": {
        "in_word": false,
        "correct_idx": false
      }
    },
    {
      "char": "O",
      "scoring": {
        "in_word": true,
        "correct_idx": true
      }
    },
    {
      "char": "T",
      "scoring": {
        "in_word": false,
        "correct_idx": false
      }
    },
    {
      "char": "E",
      "scoring": {
        "in_word": false,
        "correct_idx": false
      }
    }
  ]
}
```

## Getting started

### Run from source

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
### Docker

```shell
docker run -p 80:80 moofywoofy/wordle
```
Or docker compose

```yaml
version: "3.8"

services:
  wordle:
    container_name: Wordle
    image: moofywoofy/wordle
    ports:
      - "80:80"
#    volumes:
#      - ./word_list.txt:/app/word_list.txt  # if you want to use your own word list
```


## Pseudorandomness
The word of the day is pseudorandomly-selected by generating a seed of the current date `"YYYYMMDD"`


---

inspired by https://github.com/petergeorgas/Wordle-Api
