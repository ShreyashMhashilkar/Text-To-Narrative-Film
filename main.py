from read_text import readText
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



app = FastAPI()



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Text(BaseModel):
    name: str
    

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/send_text')
def get_data(text:Text):
    path = r"C:\Users\lenovo\Documents\TextToNarrativeFilms\\"
    print(text.name)
    print(type(text.name))

    data = readText(text.name,path)
    print(data)
    if data:
        return {"response": "Video is created"}
    else:
        return {"response":"Video is not created"}

