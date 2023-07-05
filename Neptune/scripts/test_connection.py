import os

from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

endpoint = os.environ["NEPTUNE_ENDPOINT"]

g = traversal().withRemote(
    DriverRemoteConnection(f"wss://{endpoint}:8182/gremlin", "g")
)

results = g.V().count().next()

print(f"Connected to Neptune! There are {results} vertices in the database")
