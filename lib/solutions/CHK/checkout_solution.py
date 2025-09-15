
class CheckoutSolution:

    def checkout(self, skus:str)->int:
        """In a normal supermarket, things are identified using Stock Keeping Units, or SKUs.
        In our store, we'll use individual letters of the alphabet (A, B, C, and so on).
        Our goods are priced individually. In addition, some items are multi-priced: buy n of them, and they'll cost you y pounds.
        For example, item A might cost 50 pounds individually, but this week we have a special offer:
        buy three As and they'll cost you 130.

        Our price table and offers:
        +------+-------+----------------+
        | Item | Price | Special offers |
        +------+-------+----------------+
        | A    | 50    | 3A for 130     |
        | B    | 30    | 2B for 45      |
        | C    | 20    |                |
        | D    | 15    |                |
        +------+-------+----------------+

        Notes:
         - For any illegal input return -1

        Args:
            skus (str): a string containing the SKUs of all the products in the basket

        Raises:
            NotImplementedError: _description_

        Returns:
            int: an integer representing the total checkout value of the items
        """
        item_prices = {}
        raise NotImplementedError()

