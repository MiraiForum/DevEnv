import os
import json
import uuid

secret = uuid.uuid1()
config = {
    "url": os.environ.get("URL",None),
    "secret": str(secret),
    "database": "mongo",
    "port": "4567",
    "bind_address":"0.0.0.0",
    "mongo": {
        "host": "mongo",
        "port": "27017",
        "username": os.environ.get("DB_USER",None),
        "password": os.environ.get("DB_PASSWORD",None),
        "database": "admin",
        "uri": ""
    }
}

with open("/NodeBB/config.json","w") as f:
    json.dump(config,f)