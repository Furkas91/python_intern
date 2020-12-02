import uvicorn
from fastapi import FastAPI, Query

from app import is_alive_host

app = FastAPI()


@app.get("/healthz")
async def get_is_alive_host(hostname: str = Query(...)):
    return {"status": "up" if is_alive_host(hostname) else "down"}

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8001, reload=True)