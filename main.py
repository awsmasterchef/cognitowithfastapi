from typing import Union

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request

from auth import auth_required

app = FastAPI()


@app.get("/user")
@auth_required()
def read_root(request: Request):
    return {"User": "User Information Comes Here"}


if __name__ == '__main__':
    uvicorn.run(app=app,port=8001)