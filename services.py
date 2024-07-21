
class Perfumery:

    def __init__(self, url, name, brand, price, rating, description, instructions, country):
        self.url = url
        self.name = name
        self.brand = brand
        self.price = price
        self.rating = rating
        self.description = description
        self.instructions = instructions
        self.country = country

    def __str__(self):
        return self.name
