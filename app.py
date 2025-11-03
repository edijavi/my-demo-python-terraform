"""
Simple greeting web application for Just Eat interview demo.
Returns a random greeting in different languages with visitor counter.
"""
from fastapi import FastAPI
import random
import pathlib

app = FastAPI(title="Just Eat Greeting Service")
counter = 0


def load_languages(path: str = "languages.txt") -> list[str]:
    """
    Load greetings from a text file.
    
    Args:
        path: Path to the languages file
        
    Returns:
        List of greeting strings
        
    Raises:
        RuntimeError: If file cannot be read or is empty
    """
    file_path = pathlib.Path(path)
    try:
        lines = file_path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        raise RuntimeError(f"Language file not found: {path}")
    except Exception as e:
        raise RuntimeError(f"Cannot read {path}: {e}")
    
    # Filter out empty lines and strip whitespace
    languages = [line.strip() for line in lines if line.strip()]
    
    if not languages:
        raise RuntimeError("Language file is empty or contains no valid greetings.")
    
    return languages


# Load languages at startup
LANGS = load_languages()


@app.get("/")
def root():
    """
    Return a random greeting with visitor count.
    
    Returns:
        JSON response with greeting message
    """
    global counter
    counter += 1
    greeting = random.choice(LANGS)
    return {"message": f"{greeting} visitor number {counter}!"}


@app.get("/health")
def health():
    """
    Health check endpoint.
    
    Returns:
        JSON response with status
    """
    return {"status": "ok"}
