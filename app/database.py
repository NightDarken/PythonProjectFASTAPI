import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv #load environment variables

load_dotenv() #To load the variables from the .env file

class Database:
    def __init__(self):
        # These will hold the mongodb connection client snd reference to a specific database
        self.client = None
        self.database = None
async def connect_to_database():
    """Here is where the connection to the mongoDb occurs. Am actually using mongodb atlas"""
    try:
        #MONGODB ATLAS CONNECTION STRING
      connection = os.getenv("MONGODB_URL")
        #Recommended for atlas
      client = AsyncIOMotorClient(connection,maxPoolSize=100,minPoolSize=100)
      '''Test The connection'''
      await client.admin.command('ping')

      '''Get the database'''
      database=client[os.getenv("DATABASE_NAME")]
      print(f"Connected to database MONOGODB Succesfullly{database}")
    except Exception as error:
        print(f"Failed to connect to database: {error}")
        print(f"Check your environment variables and try again")
        raise error
async def close(self):
    "Close the connection to the database"
    if self.client:
        self.client.close()
        print("MonogoDb connection closed")


def get_collection(self, collection_name: str):
    """Get a collection from the database for review"""
    if self.database is None:
        raise Exception("Database not connected. Call connect() first")
    return self.database[collection_name]

#Create n instance
mongodb = Database()