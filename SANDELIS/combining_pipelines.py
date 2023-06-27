# Aggregation Pipelines

# A. Combining_pipelines (filtering, sorting, projecting documents)

# cia uzdarom pylint, jis neduoda dirbti normaliai pymongo
# pylint: disable = all
from typing import Dict, Any, List
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.database import Database


def aggregate_documents(collection: Collection, pipeline: Dict[str, Any]) -> Cursor:
    return collection.aggregate(pipeline)


# Establish a connection to the MongoDB server
client: MongoClient = MongoClient("mongodb://localhost:27017")
db: Database = client["Aggregation_Pipelines"]  # Type: Database
collection: Collection = db["SANDELIS"]  # Type: Collection


# Define the aggregation pipeline
pipeline: Dict[str, Any] = [
    {
        "$match": {
            "$or": [
                {"pavadinimas": "mqxystbjff"},
                {"pavadinimas": "cmxhabnpgt"},
            ],  # Filter documents by the 'pavadinimas' field
            "kaina": {
                "$gte": 10,
                "$lte": 300,
            },  # Filter documents where 'kaina' is greater than 10 or equal and less tharn 300 or equal
        }
    },
    {"$sort": {"kaina": -1}},  # Sort documents by 'kaina' in descending order
    {
        "$project": {
            "_id": 0,  # Exclude the '_id' field from the projection
            "pavadinimas": 1,  # Include the 'pavadinimas' field in the projection
            "kaina": 1,  # Include the 'kaina' field in the projection
            "gamintojas": 1,  # Include the 'gamintojas' field in the projection
        }
    },
]


# Call the aggregate_documents function
result: Cursor = aggregate_documents(collection, pipeline)  # Type: Cursor

# Iterate over the cursor and print the aggregated documents
for doc in result:
    print(doc)
