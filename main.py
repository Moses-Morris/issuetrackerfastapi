from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return { "status" : "ok"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return "Item not found"
    raise ValueError("Item not Found in the list.")



##For the urls with limits and pagination.
##E.G. /items?skip=10?limit=10 
@app.get("/items")
async def show_items(skip: int=0, limit: int=0):
    return items[skip: skip + limit]

@app.post("/items")
async def create_item(item: dict):
    items.append(item)
    return item



