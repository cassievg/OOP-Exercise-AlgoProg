class Price:
    # Initialize
    def __init__(self, name, amt):
        self._food_name = name
        self._food_amt = amt
        self._standard_price = None
        self._calculated_price = None
        self._price_listCVG()

    # Store list of items and price per pound
    def _price_listCVG(self):
        if self._food_name == 'Dry Cured Iberian Ham':
            self._standard_price = 177.80
        elif self._food_name == 'Wagyu Steaks':
            self._standard_price = 177.80
        elif self._food_name == 'Matsutake Mushrooms':
            self._standard_price = 177.80
        elif self._food_name == 'Kopi Luwak Coffee':
            self._standard_price = 177.80
        elif self._food_name == 'Moose Cheese':
            self._standard_price = 177.80
        elif self._food_name == 'White Truffles':
            self._standard_price = 177.80
        elif self._food_name == 'Blue Fin Tuna':
            self._standard_price = 177.80
        elif self._food_name == 'Le Bonnotte Potatoes':
            self._standard_price = 177.80
        else:
            self._standard_price = 0.00

    # Calculate total cost of food according to its corresponding price and amounts
    def calculate_costCVG(self):
        return self._standard_price * self._food_amt

    # A function to get food name
    def get_food_nameCVG(self):
        return self._food_name
    
    # A function to get food amount
    def get_food_amtCVG(self):
        return self._food_amt
    
    # A function to get food standard price
    def get_standard_priceCVG(self):
        return self._standard_price

    # A function to get food total cost
    def get_calculated_costCVG(self):
        return self._calculated_price