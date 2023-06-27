# Aggregation Pipelines
# B. Sorting Documents

# cia uzdarom pylint, jis neduoda dirbti normaliai pymongo
# pylint: disable = all
from typing import Dict, Any
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.database import Database


def sort_documents(collection: Collection, sort_criteria: Dict[str, int]) -> Cursor:
    pipeline = [{"$sort": sort_criteria}]
    return collection.aggregate(pipeline)


# Establish a connection to the MongoDB server
client: MongoClient = MongoClient("mongodb://localhost:27017")
db: Database = client["Aggregation_Pipelines"]  # Type: Database
collection: Collection = db["SANDELIS"]  # Type: Collection

# Define the sort criteria
criteria: Dict[str, int] = {
    "kiekis": 1,  # iskart sortiruojam didejancia tvarka pagal lauka: kiekis,
    "pavadinimas": -1,  # po to (kai kiekis vienodas) sortiruojamas mazejancia tvarka pagal lauka: pavadinimas
}  # Sort by the 'name' field in ascending order (1) or descending order (-1)

# Call the sort_documents function
result: Cursor = sort_documents(collection, criteria)  # Type: Cursor

# Iterate over the cursor and print the sorted documents
for doc in result:
    print(doc)
