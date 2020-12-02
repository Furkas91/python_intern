import uvicorn
from fastapi import FastAPI, Query

from app import is_alive_host

app = FastAPI()


@app.get("/")
async def get_is_alive_host(hostname: str = Query(...)):
    return {"host is ": "alive" if is_alive_host(hostname) else "dead"}

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)