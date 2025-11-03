"""
Simple greeting web application for Just Eat interview demo.
Returns a random greeting in different languages with visitor counter.
"""
from fastapi import FastAPI, Request
import random
import pathlib

app = FastAPI(title="Just Eat Greeting Service")


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


@app.on_event("startup")
def startup_event() -> None:
    app.state.languages = load_languages()
    app.state.counter = 0


@app.get("/")
async def root(request: Request):
    """
    Return a random greeting with visitor count.
    
    Returns:
        JSON response with greeting message
    """
    request.app.state.counter += 1
    greeting = random.choice(request.app.state.languages)
    return {"message": f"{greeting} visitor number {request.app.state.counter}!"}


@app.get("/health")
async def health():
    """
    Health check endpoint.
    
    Returns:
        JSON response with status
    """
    return {"status": "ok"}
