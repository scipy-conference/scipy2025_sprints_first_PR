from pr_tutorial.simple_functions import factorial, is_prime


def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6

def test_is_prime():
    """Test for is_prime function"""
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)
