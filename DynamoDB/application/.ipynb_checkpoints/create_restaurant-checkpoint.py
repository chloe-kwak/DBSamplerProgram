import boto3

dynamodb = boto3.client("dynamodb")


def create_restaurant(name, cuisine, address):
    try:
        resp = dynamodb.put_item(
            TableName="Restaurants",
            Item={
                "PK": {"S": "REST#{}".format(name)},
                "SK": {"S": "REST#{}".format(name)},
                "GSI1PK": {"S": "REST#{}".format(name)},
                "GSI1SK": {"S": "REST#{}".format(name)},
                "name": {"S": name},
                "cuisine": {"S": cuisine},
                "address": {"S": address},
            },
            ConditionExpression="attribute_not_exists(PK)",
        )
        return {"name": name, "cuisine": cuisine, "address": address}
    except Exception as e:
        print("Could not create restaurant")
        print(e)
        return False


restaurant = create_restaurant(
    "AnyCompany French", "French", "541 Salazar Ranch, South Kristen, MS 00857"
)

if restaurant:
    print("Created restaurant: {}".format(restaurant["name"]))
