import os

from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

endpoint = os.environ["NEPTUNE_ENDPOINT"]

g = traversal().withRemote(
    DriverRemoteConnection(f"wss://{endpoint}:8182/gremlin", "g")
)

g.V().drop().iterate()
g.E().drop().iterate()
