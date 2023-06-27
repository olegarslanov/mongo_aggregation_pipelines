# Aggregation Pipelines

# A. Filtering Documents

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.database import Database
from typing import Dict, Any, List


def filter_documents(
    collection: Collection, filter_criteria: List[Dict[str, Any]]
) -> Cursor:
    pipeline = [{"$match": {"$and": filter_criteria}}]
    return collection.aggregate(pipeline)


# Establish a connection to the MongoDB server
client: MongoClient = MongoClient("mongodb://localhost:27017")
db: Database = client["grocery_store"]
collection: Collection = db["electronic"]

# Define the filter criteria
criteria: List[Dict[str, Any]] = [
    {
        "$and": [
            {"quantity": {"$gte": 60, "$lte": 65}},
            {"price": {"$gte": 100, "$lte": 1000}},
        ]
    },
]

# Call the filter_documents function
result = filter_documents(collection, criteria)

# Iterate over the cursor and print the filtered documents
for doc in result:
    print(doc)
