from models import Item

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://teri:{db_password}@cluster0.7fnya95.mongodb.net/test")
database = client.ItemList
collection = database.item

async def fetch_all_items():
  items = []
  cursor = collection.find({})
  async for document in cursor:
    items.append(Item(**document))
  return items

async def post_item(item):
  document = item
  result = await collection.insert_one(document)
  return document