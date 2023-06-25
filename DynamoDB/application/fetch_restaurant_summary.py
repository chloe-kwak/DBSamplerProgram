import boto3

from entities import Restaurant, Review

dynamodb = boto3.client("dynamodb")


def fetch_restaurant_summary(restaurant_name):
    resp = dynamodb.query(
        TableName="Restaurants",
        IndexName="GSI1",
        KeyConditionExpression="GSI1PK = :gsi1pk",
        ExpressionAttributeValues={
            ":gsi1pk": {"S": "REST#{}".format(restaurant_name)},
        },
        ScanIndexForward=False,
        Limit=6,
    )

    restaurant = Restaurant(resp["Items"][0])
    restaurant.reviews = [Review(item) for item in resp["Items"][1:]]

    return restaurant


restaurant = fetch_restaurant_summary("AnyCompany Fine Dining")

print(restaurant)
for review in restaurant.reviews:
    print(review)
