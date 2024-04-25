from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float


app = FastAPI()


@app.get("/")
async def read_item():
    return {"message": "Welcome to our app"}


@app.get("/test")
async def read_item_test():
    return {"message": "Test....."}


@app.get("/hello/{name}")
async def read_item(name):
    return {"message": f"Hello {name}, how are you?"}


@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"{item.name} is priced at £{item.price}"}

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8888)))
