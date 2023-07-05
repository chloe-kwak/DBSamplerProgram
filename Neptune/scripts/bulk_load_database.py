import json
import os

from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

endpoint = os.environ["NEPTUNE_ENDPOINT"]

g = traversal().withRemote(
    DriverRemoteConnection(f"wss://{endpoint}:8182/gremlin", "g")
)

with open("scripts/vertices.json", "r") as f:
    for row in f:
        data = json.loads(row)
        if data["label"] == "User":
            g.addV("User").property("username", data["username"]).next()
        elif data["label"] == "Restaurant":
            g.addV("Restaurant").property("name", data["name"]).next()
        elif data["label"] == "IPAddress":
            g.addV("IPAddress").property("address", data["address"]).next()

with open("scripts/edges.json", "r") as f:
    for row in f:
        data = json.loads(row)
        if data["label"] == "Used":
            g.V().has("User", "username", data["username"]).as_("user").V().has(
                "IPAddress", "address", data["ip_address"]
            ).as_("ip_address").addE("Used").from_("user").to("ip_address").next()
        elif data["label"] == "Reviewed":
            g.V().has("User", "username", data["username"]).as_("user").V().has(
                "Restaurant", "name", data["restaurant"]
            ).as_("restaurant").addE("Reviewed").from_("user").to(
                "restaurant"
            ).property(
                "rating", data["rating"]
            ).property(
                "username", data["username"]
            ).property(
                "restaurant", data["restaurant"]
            ).next()

print("Loaded data successfully!")
