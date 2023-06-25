import datetime

import boto3
from ksuid import ksuid

dynamodb = boto3.client("dynamodb")

RATINGS = {
    1: "one_stars",
    2: "two_stars",
    3: "three_stars",
    4: "four_stars",
    5: "five_stars",
}


def create_review(restaurant, username, rating, review_text):
    review_id = str(ksuid())
    rating_attr = RATINGS[rating]
    try:
        resp = dynamodb.transact_write_items(
            TransactItems=[
                {
                    "Put": {
                        "TableName": "Restaurants",
                        "Item": {
                            "PK": {"S": "USER#{}".format(username)},
                            "SK": {"S": "REST#{}".format(restaurant)},
                            "GSI1PK": {"S": "REST#{}".format(restaurant)},
                            "GSI1SK": {"S": "REVIEW#{}".format(review_id)},
                            "username": {"S": username},
                            "restaurant": {"S": restaurant},
                            "id": {"S": review_id},
                            "rating": {"N": str(rating)},
                            "review": {"S": review_text},
                            "created_at": {"S": datetime.datetime.now().isoformat()},
                        },
                        "ConditionExpression": "attribute_not_exists(PK)",
                    },
                },
                {
                    "Update": {
                        "TableName": "Restaurants",
                        "Key": {
                            "PK": {"S": "REST#{}".format(restaurant)},
                            "SK": {"S": "REST#{}".format(restaurant)},
                        },
                        "ConditionExpression": "attribute_exists(PK)",
                        "UpdateExpression": "SET #rating = if_not_exists(#rating, :zero) + :inc",
                        "ExpressionAttributeNames": {"#rating": rating_attr},
                        "ExpressionAttributeValues": {
                            ":inc": {"N": "1"},
                            ":zero": {"N": "0"},
                        },
                    }
                },
            ]
        )
        print("Added review from {} to restaurant {}".format(username, restaurant))
        return True
    except Exception as e:
        print("Could not add review to restaurant")


create_review("AnyCompany French", "hungryhank", 5, "Great food, great price!")
