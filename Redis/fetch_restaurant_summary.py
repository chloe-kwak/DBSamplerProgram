from dynamodb import fetch_restaurant_summary_from_database
from cache import fetch_restaurant_summary_from_cache, store_restaurant_summary_in_cache


def fetch_restaurant_summary(restaurant_name):
    restaurant = fetch_restaurant_summary_from_cache(restaurant_name)
    if restaurant:
        print("Using cached result!")
        return restaurant

    restaurant = fetch_restaurant_summary_from_database(restaurant_name)
    store_restaurant_summary_in_cache(restaurant)

    print("Using uncached result!")

    return restaurant


restaurant = fetch_restaurant_summary("AnyCompany Fine Dining")

print(restaurant)
for review in restaurant.reviews:
    print(review)
