#! /usr/bin/python
from elasticsearch import Elasticsearch
import json
import warnings

import warnings
warnings.filterwarnings("ignore")

# Connexion au cluster
client = Elasticsearch(hosts = "http://@localhost:9200")

# Préciser le numéro de votre question ici.
# Si vous effectuez plusieurs requêtes pour la même question, écrivez "1-1", "1-2" ext...
question_number = "2-5_2-6"
# Copier coller votre requête Kibana ici (SANS l'instruction GET)
query = {
  "size" : 0,
  "aggs": {
    "div": {
      "terms": {
        "field": "Division Name.keyword",
        "size": 10
      },
      "aggs": {
        "dep": {
          "terms": {
            "field": "Department Name.keyword",
            "size": 10
          }, 
          "aggs": {
            "prod": {
              "terms": {
                "field": "Class Name.keyword",
                "size": 10
              }
            }
          }
        }
      }
    }
  }
}

response = client.search(index="eval", body=query)

# Sauvegarde de la requête et la réponse dans un fichier json
with open("./eval/{}.json".format("q_" + question_number + "_response"), "w") as f:
  json.dump(dict(response), f, indent=2)

with open("./eval/{}.json".format("q_" + question_number + "_request"), "w") as f:
  json.dump(query, f, indent=2)