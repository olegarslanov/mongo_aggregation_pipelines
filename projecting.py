# Aggregation Pipelines

# C. Projecting Documents (galima filtruoti be tam tikru dokumentu lauku)

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.cursor import Cursor
from typing import Dict, Any


def project_documents(
    collection: Collection, projection_fields: Dict[str, int]
) -> Cursor:
    pipeline = [{"$project": projection_fields}]
    return collection.aggregate(pipeline)


# Establish a connection to the MongoDB server
client: MongoClient = MongoClient("mongodb://localhost:27017")
db: Database = client["task_manager"]  # Type: Database
collection: Collection = db["tasks"]  # Type: Collection

# Define the projection fields
projection: Dict[str, int] = {
    # "name": 1,  # Include the 'name' field in the projection (1 indicates inclusion)
    # "price": 1,  # Include this field in the projection
    "food.quantity": 1,
    # "_id": 0,  # Exclude this field from the projection (0 indicates exclusion)
}

# Call the project_documents function
result: Cursor = project_documents(collection, projection)  # Type: Cursor

# Iterate over the cursor and print the projected documents
for doc in result:
    print(doc)
