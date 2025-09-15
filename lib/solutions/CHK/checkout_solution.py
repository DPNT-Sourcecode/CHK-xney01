from collections import Counter

class CheckoutSolution:
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
        +------+-------+------------------------+

        Notes:
         - For any illegal input return -1

        Args:
            skus (str): a string containing the SKUs of all the products in the basket

        Returns:
            int: an integer representing the total checkout value of the items
        """

        item_prices = {
            "A":{"unit_price":50,"special_offers":[(5,200),(3,130)]},
            "B":{"unit_price":30,"special_offers":[(2,45)]},
            "C":{"unit_price":20,"special_offers":[]},
            "D":{"unit_price":15,"special_offers":[]},
            "E":{"unit_price":40,"special_offers":[]},
            "F":{"unit_price":10,"special_offers":[(3,20)]},
        }

        extra_offers = {"E":(2,"B",1)}

        if not isinstance(skus,str):
            return -1
        
        for item in skus:
            if item not in item_prices.keys():
                return -1
        
        counted_items = Counter(skus)

        for item,(required_amount,free_item,free_amount) in extra_offers.items():
            if item in counted_items:
                free_count = (counted_items[item]//required_amount) * free_amount
                if free_item in counted_items:
                    counted_items[free_item] = counted_items[free_item] - free_count

        total = 0
        for item,count in counted_items.items():
            unit_price = item_prices[item]["unit_price"]
            special_offers = item_prices[item]["special_offers"]#Assuming sorted with better values first

            for offer_amount,offer_price in special_offers:
                num_applies,count = divmod(count,offer_amount)
                total += num_applies * offer_price

            total += count*unit_price

        return total



