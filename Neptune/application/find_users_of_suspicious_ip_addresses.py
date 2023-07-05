import os

from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python import statics

statics.load_statics(globals())


endpoint = os.environ["NEPTUNE_ENDPOINT"]

g = traversal().withRemote(
    DriverRemoteConnection(f"wss://{endpoint}:8182/gremlin", "g")
)


def find_users_of_suspicious_ip_addresses(ip_address):
    results = (
        g.V()
        .has("IPAddress", "address", ip_address)
        .as_("ip_address")
        .in_("Used")
        .aggregate("ip_address_users")
        .outE("Reviewed")
        .has("rating", 1)
        .values("username")
        .groupCount()
        .order(local)
        .by(values, desc)
        .limit(local, 10)
        .toList()
    )

    return [
        {"username": k, "1-star reviews": v}
        for result in results
        for k, v in result.items()
    ]


suspicious_users = find_users_of_suspicious_ip_addresses("173.153.51.29")

for user in suspicious_users:
    print(
        f"User {user['username']} has written {user['1-star reviews']} one-star reviews."
    )
