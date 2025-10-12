from api.core.logging_config import setup_logging
from solving_simple_quadratic_equations import solve, extract_coef
import uvicorn

from fastapi import FastAPI
from api.router import router

setup_logging()

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():       #основной сайт, если никуда не переходить
    return {"message": "Тут ничего нет"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)