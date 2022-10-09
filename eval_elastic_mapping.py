#! /usr/bin/python
from elasticsearch import Elasticsearch
import json
import warnings

import warnings
warnings.filterwarnings("ignore")

# Connexion au cluster
client = Elasticsearch(hosts = "http://@localhost:9200")

template = client.indices.get_mapping()

# Sauvegarde dans un fichier json
with open("./eval/{}.json".format("index_template"), "w") as f:
  json.dump(dict(template), f, indent=2)