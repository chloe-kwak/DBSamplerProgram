class Restaurant:
    def __init__(self, item):
        self.name = item.get("name")
        self.cuisine = item.get("cuisine")
        self.address = item.get("address")
        self.five_stars = item.get("five_stars", {})
        self.four_stars = item.get("four_stars", {})
        self.three_stars = item.get("three_stars", {})
        self.two_stars = item.get("two_stars", {})
        self.one_stars = item.get("one_stars", {})

    def __repr__(self):
        return "Restaurant<{} -- {}>".format(self.name, self.cuisine)


class Review:
    def __init__(self, item):
        self.restaurant = item.get("restaurant")
        self.username = item.get("username")
        self.rating = item.get("rating")
        self.review = item.get("review")
        self.id = item.get("id")
        self.created_at = item.get("created_at")

    def __repr__(self):
        return "Review<{} -- {} ({})>".format(
            self.restaurant, self.username, self.created_at
        )
