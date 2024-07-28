class Perfumery:

    def __init__(
            self,
            url,
            name,
            brand,
            price,
            rating,
            description,
            instructions,
            compound,
            country,
    ):
        self.url = url
        self.name = name
        self.brand = brand
        self.price = price
        self.rating = rating
        self.description = description
        self.instructions = instructions
        self.compound = compound
        self.country = country

    def __getstate__(self) -> dict:
        state = self.__dict__.copy()
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.__init__(**state)
        return self
