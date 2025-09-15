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
        assert checkout.checkout("AAAAAAAA") == 330

    def test_extra_offers(self): 
        checkout = CheckoutSolution()
        assert checkout.checkout("EE") == 80
        assert checkout.checkout("EEB") == 80
        assert checkout.checkout("EEBB") == 110

    def test_large_mixed_basket(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("ABCDEEAA") == 245

    def test_illegal_inputs(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("X") == -1
        assert checkout.checkout(123) == -1

    def test_empty_basket(self):
        checkout = CheckoutSolution()
        assert checkout.checkout("") == 0