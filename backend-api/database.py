from dotenv.main import load_dotenv
import os
load_dotenv()

db_password = os.environ["DB_PASSWORD"]


from models import Item

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb+srv://teri:{db_password}@cluster0.7fnya95.mongodb.net/test")
# client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.ItemList
collection = database.item

async def fetch_all_items():
  items = []
  cursor = collection.find({})
  async for document in cursor:
    items.append(Item(**document))
  return items

async def fetch_item(title):
  document = await collection.find_one({"title": title})
  return document

async def post_item(item):
  document = item
  result = await collection.insert_one(document)
  return document

async def put_item(title, description):
  await collection.update_one({"title": title}, {"$set":{
    "description": description}})
  document = await collection.find_one({"title": title})
  return document

async def delete_item(title):
  # await collection.delete_one({"title": title})
  # return True
  document = await collection.find_one({"title": title})
  await collection.delete_one({"title": title})
  return document