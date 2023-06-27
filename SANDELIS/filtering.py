# Aggregation Pipelines

# A. Filtering Documents

# cia uzdarom pylint, jis neduoda dirbti normaliai pymongo
# pylint: disable = all
from typing import Dict, Any, List
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.database import Database


def filter_documents(
    collection: Collection, filter_criteria: List[Dict[str, Any]]
) -> Cursor:
    pipeline = [{"$match": {"$and": filter_criteria}}]
    return collection.aggregate(pipeline)


# Establish a connection to the MongoDB server
client: MongoClient = MongoClient("mongodb://localhost:27017")
db: Database = client["Aggregation_Pipelines"]
collection: Collection = db["SANDELIS"]

# Define the filter criteria
criteria: List[Dict[str, Any]] = [
    {
        "$and": [
            {
                "kiekis": {"$gte": 0, "$lte": 10}
            },  # didesnis, arba lygus 0 ir mazesnis, arba lygus 10
            {"kaina": {"$gte": 10, "$lte": 300}},
        ]
    }
]

# Call the filter_documents function
result = filter_documents(collection, criteria)

# Iterate over the cursor and print the filtered documents
for doc in result:
    print(doc)
