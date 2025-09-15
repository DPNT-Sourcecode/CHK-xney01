from collections import Counter


class CheckoutSolution:
    ITEM_PRICES = {
        "A": {"unit_price": 50, "special_offers": [(5, 200), (3, 130)]},
        "B": {"unit_price": 30, "special_offers": [(2, 45)]},
        "C": {"unit_price": 20, "special_offers": []},
        "D": {"unit_price": 15, "special_offers": []},
        "E": {"unit_price": 40, "special_offers": []},
        "F": {"unit_price": 10, "special_offers": [(3, 20)]},
        "G": {"unit_price": 20, "special_offers": []},
        "H": {"unit_price": 10, "special_offers": [(10, 80), (5, 45)]},
        "I": {"unit_price": 35, "special_offers": []},
        "J": {"unit_price": 60, "special_offers": []},
        "K": {"unit_price": 70, "special_offers": [(2, 150)]},
        "L": {"unit_price": 90, "special_offers": []},
        "M": {"unit_price": 15, "special_offers": []},
        "N": {"unit_price": 40, "special_offers": []},
        "O": {"unit_price": 10, "special_offers": []},
        "P": {"unit_price": 50, "special_offers": [(5, 200)]},
        "Q": {"unit_price": 30, "special_offers": [(3, 80)]},
        "R": {"unit_price": 50, "special_offers": []},
        "S": {"unit_price": 20, "special_offers": []},
        "T": {"unit_price": 20, "special_offers": []},
        "U": {"unit_price": 40, "special_offers": [(4, 120)]},
        "V": {"unit_price": 50, "special_offers": [(3, 130), (2, 90)]},
        "W": {"unit_price": 20, "special_offers": []},
        "X": {"unit_price": 17, "special_offers": []},
        "Y": {"unit_price": 20, "special_offers": []},
        "Z": {"unit_price": 21, "special_offers": []},
    }

    EXTRA_OFFERS = {
        "E": (2, "B", 1),  # Format is item:(item_quantity,free_item,free_item_quantity)
        "N": (3, "M", 1),
        "R": (3, "Q", 1),
    }

    GROUP_OFFERS = [
        {"group_items": ["S", "T", "X", "Y", "Z"], "group_size": 3, "group_price": 45}
    ]

    def checkout(self, skus: str) -> int:
        """
        Notes:
         - For any illegal input return -1

        Args:
            skus (str): a string containing the SKUs of all the products in the basket

        Returns:
            int: an integer representing the total checkout value of the items
        """

        # Validating input type
        if not isinstance(skus, str):
            return -1
        for item in skus:
            if item not in self.ITEM_PRICES.keys():
                return -1

        counted_items = Counter(skus)

        # Calculates the extra offers, across items
        for item, (
            required_amount,
            free_item,
            free_amount,
        ) in self.EXTRA_OFFERS.items():
            if item in counted_items:
                free_count = (counted_items[item] // required_amount) * free_amount
                if free_item in counted_items:
                    counted_items[free_item] = max(
                        0, counted_items[free_item] - free_count
                    )

        total = 0
        for group in self.GROUP_OFFERS:
            group_items = group["group_items"]
            group_size = group["group_size"]
            group_price = group["group_price"]

            # Should use most expensive items from group first
            group_list = []
            for item in group_items:
                group_list += [item] * counted_items.get(item, 0)
            group_list.sort(
                key=lambda x: self.ITEM_PRICES[x]["unit_price"], reverse=True
            )
            num_groups, _ = divmod(len(group_list), group_size)
            total += num_groups * group_price

            # Removing used items, these should be the most expensive since we sort by price
            for i in range(num_groups * group_size):
                counted_items[group_list[i]] -= 1

        for item, count in counted_items.items():
            unit_price = self.ITEM_PRICES[item]["unit_price"]

            special_offers = sorted(
                self.ITEM_PRICES[item]["special_offers"],
                key=lambda x: x[0],
                reverse=True,
            )

            for offer_amount, offer_price in special_offers:
                num_applies, count = divmod(count, offer_amount)
                total += num_applies * offer_price

            total += count * unit_price

        return total
    





