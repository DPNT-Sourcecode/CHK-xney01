from collections import Counter

class CheckoutSolution:
    
    ITEM_PRICES = {
        "A":{"unit_price":50,"special_offers":[(5,200),(3,130)]},
        "B":{"unit_price":30,"special_offers":[(2,45)]},
        "C":{"unit_price":20,"special_offers":[]},
        "D":{"unit_price":15,"special_offers":[]},
        "E":{"unit_price":40,"special_offers":[]},
        "F":{"unit_price":10,"special_offers":[(3,20)]},
        "G":{"unit_price":20,"special_offers":[]},
        "H":{"unit_price":10,"special_offers":[(10,80),(5,45)]},
        "I":{"unit_price":35,"special_offers":[]},
        "J":{"unit_price":60,"special_offers":[]},
        "K":{"unit_price":80,"special_offers":[(2,150)]},
        "L":{"unit_price":90,"special_offers":[]},
        "M":{"unit_price":15,"special_offers":[]},
        "N":{"unit_price":40,"special_offers":[]},
        "O":{"unit_price":10,"special_offers":[]},
        "P":{"unit_price":50,"special_offers":[(5,200)]},
        "Q":{"unit_price":30,"special_offers":[(3,80)]},
        "R":{"unit_price":50,"special_offers":[]},
        "S":{"unit_price":30,"special_offers":[]},
        "T":{"unit_price":20,"special_offers":[]},
        "U":{"unit_price":40,"special_offers":[(4,120)]},
        "V":{"unit_price":50,"special_offers":[(3,130),(2,90)]},
        "W":{"unit_price":20,"special_offers":[]},
        "X":{"unit_price":90,"special_offers":[]},
        "Y":{"unit_price":10,"special_offers":[]},
        "Z":{"unit_price":50,"special_offers":[]},
        }
    
    EXTRA_OFFERS = {
        "E":(2,"B",1),
        "N":(3,"M",1),
        "R":(3,"Q",1),
    }
    def checkout(self, skus:str)->int:
        """

        Our price table and offers:
        +------+-------+------------------------+
        | Item | Price | Special offers         |
        +------+-------+------------------------+
        | A    | 50    | 3A for 130, 5A for 200 |
        | B    | 30    | 2B for 45              |
        | C    | 20    |                        |
        | D    | 15    |                        |
        | E    | 40    | 2E get one B free      |
        | F    | 10    | 2F get one F free      |
        | G    | 20    |                        |
        | H    | 10    | 5H for 45, 10H for 80  |
        | I    | 35    |                        |
        | J    | 60    |                        |
        | K    | 80    | 2K for 150             |
        | L    | 90    |                        |
        | M    | 15    |                        |
        | N    | 40    | 3N get one M free      |
        | O    | 10    |                        |
        | P    | 50    | 5P for 200             |
        | Q    | 30    | 3Q for 80              |
        | R    | 50    | 3R get one Q free      |
        | S    | 30    |                        |
        | T    | 20    |                        |
        | U    | 40    | 3U get one U free      |
        | V    | 50    | 2V for 90, 3V for 130  |
        | W    | 20    |                        |
        | X    | 90    |                        |
        | Y    | 10    |                        |
        | Z    | 50    |                        |
        +------+-------+------------------------+

        Notes:
         - For any illegal input return -1

        Args:
            skus (str): a string containing the SKUs of all the products in the basket

        Returns:
            int: an integer representing the total checkout value of the items
        """

        if not isinstance(skus,str):
            return -1
        
        for item in skus:
            if item not in self.ITEM_PRICES.keys():
                return -1
        
        counted_items = Counter(skus)

        # Calculates the extra offers, across items
        for item,(required_amount,free_item,free_amount) in self.EXTRA_OFFERS.items():
            if item in counted_items:
                free_count = (counted_items[item]//required_amount) * free_amount
                if free_item in counted_items:
                    counted_items[free_item] = max(0,counted_items[free_item] - free_count)

        total = 0
        for item,count in counted_items.items():
            unit_price = self.ITEM_PRICES[item]["unit_price"]
            special_offers = self.ITEM_PRICES[item]["special_offers"]#Assuming sorted with better values first

            for offer_amount,offer_price in special_offers:
                num_applies,count = divmod(count,offer_amount)
                total += num_applies * offer_price

            total += count*unit_price

        return total




