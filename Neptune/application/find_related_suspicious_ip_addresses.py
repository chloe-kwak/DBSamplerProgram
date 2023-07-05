import os

from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python import statics

statics.load_statics(globals())


endpoint = os.environ["NEPTUNE_ENDPOINT"]

g = traversal().withRemote(
    DriverRemoteConnection(f"wss://{endpoint}:8182/gremlin", "g")
)


def find_related_suspicious_ip_addresses(ip_address):
    results = (
        g.V()
        .has("IPAddress", "address", ip_address)
        .as_("ip_address")
        .in_("Used")
        .aggregate("ip_address_users")
        .out("Used")
        .where(neq("ip_address"))
        .values("address")
        .groupCount()
        .order(local)
        .by(values, desc)
        .limit(local, 10)
        .toList()
    )

    return [
        {"ip_address": k, "user_overlap": v}
        for result in results
        for k, v in result.items()
    ]


suspicious_ip_addresses = find_related_suspicious_ip_addresses("173.153.51.29")

for user in suspicious_ip_addresses:
    print(
        f"IP address {user['ip_address']} has {user['user_overlap']} overlapping users."
    )
