from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/api/data')
async def get_data():
    # Логика для получения данных
    data = 'data from backend'
    return data


