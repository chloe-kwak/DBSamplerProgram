class Restaurant:
    def __init__(self, item):
        self.name = item.get("name").get("S")
        self.cuisine = item.get("cuisine").get("S")
        self.address = item.get("address").get("S")
        self.five_stars = item.get("five_stars", {}).get("N")
        self.four_stars = item.get("four_stars", {}).get("N")
        self.three_stars = item.get("three_stars", {}).get("N")
        self.two_stars = item.get("two_stars", {}).get("N")
        self.one_stars = item.get("one_stars", {}).get("N")

    def __repr__(self):
        return "Restaurant<{} -- {}>".format(self.name, self.cuisine)


class Review:
    def __init__(self, item):
        self.restaurant = item.get("restaurant").get("S")
        self.username = item.get("username").get("S")
        self.rating = item.get("rating").get("N")
        self.review = item.get("review").get("S")
        self.id = item.get("id").get("S")
        self.created_at = item.get("created_at").get("S")

    def __repr__(self):
        return "Review<{} -- {} ({})>".format(
            self.restaurant, self.username, self.created_at
        )
