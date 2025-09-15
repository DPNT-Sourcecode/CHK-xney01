from lib.solutions.CHK.checkout_solution import CheckoutSolution
import pytest

# Not doing extensive tests due to time
class TestCheckout:
    def test_single_items(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("A") == 50
        assert checkout.checkout("B") == 30

    def test_many_items(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("ABACA") == 180


    def test_empty_basket(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("") == 0