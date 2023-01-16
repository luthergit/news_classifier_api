from fastapi import FastAPI
from pydantic import BaseModel
from ten_notes import news_classifier, classifier

app = FastAPI()


@app.get("/")
async def root():
    return news_classifier()


@app.post("/input/{text}/{category}")
async def data(text: str, category: int):
    capital = text.upper()
    subcat = ((category * 100) + 1) ** 2
    return {"result": {capital: subcat}}


class UserData(BaseModel):
    #str,str is string for key and value
    text: dict[str,str]
    category: dict[str,str]

@app.post("/input")
async def information(info: UserData):
    # capital = info.text.upper()
    # subcat = ((info.category * 100) + 1) ** 2
    # return {"result": {capital: subcat}}
    # result = {"text":info.text, "category":info.category}
    return classifier(dict(info))


