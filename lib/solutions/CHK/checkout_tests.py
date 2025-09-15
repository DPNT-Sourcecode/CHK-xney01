from lib.solutions.CHK.checkout_solution import CheckoutSolution
import pytest

# Not doing extensive tests 
class TestCheckout:
    def test_single_items(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("A") == 50
        assert checkout.checkout("B") == 30