from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {'about': "This is the about page."}

app.include_router(todo_router)