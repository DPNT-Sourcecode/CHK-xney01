from lib.solutions.CHK.checkout_solution import CheckoutSolution
import pytest

class TestCheckout:
    def test_single_items(self):
        assert CheckoutSolution.checkout("A") == 50