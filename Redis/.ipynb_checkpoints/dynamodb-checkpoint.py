import json

from entities import Restaurant, Review


def fetch_restaurant_summary_from_database(restaurant_name):
    restaurants = []
    reviews = []

    with open("items.json", "r") as f:
        for row in f:
            data = json.loads(row)
            if data["PK"].startswith("REST#"):
                restaurants.append(Restaurant(data))
            else:
                reviews.append(Review(data))

    restaurant = list(filter(lambda x: x.name == restaurant_name, restaurants))[0]
    filtered_reviews = filter(lambda x: x.restaurant == restaurant_name, reviews)

    restaurant.reviews = sorted(
        filtered_reviews, key=lambda x: x.created_at, reverse=True
    )[:5]

    return restaurant
