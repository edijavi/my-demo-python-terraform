# app.py
from fastapi import FastAPI, HTTPException
import random, pathlib

app = FastAPI()
counter = 0

def load_langs(path="languages.txt"):
    p = pathlib.Path(path)
    try:
        lines = p.read_text(encoding="utf-8").splitlines()
    except Exception as e:
        raise RuntimeError(f"Cannot read {path}: {e}")
    langs = [l.strip() for l in lines if isinstance(l, str) and l.strip()]
    # Validación extra: sin None/valores no-str
    if not langs or not all(isinstance(x, str) and x for x in langs):
        raise RuntimeError("languages.txt está vacío o tiene valores no válidos.")
    return langs

LANGS = load_langs()

@app.get("/")
def root():
    global counter
    counter += 1
    try:
        greeting = random.choice(LANGS)
    except IndexError:
        # No debería pasar por la validación, pero por si acaso
        greeting = "Hello"
    return {"message": f"{greeting} visitor number {counter}!"}

@app.get("/health")
def health():
    return {"status": "ok"}
