from pr_tutorial.buggy_function import angle_to_sexigesimal


def test_angle_to_sexigesimal_360():
    """Simplest test for one crete case"""
    assert angle_to_sexigesimal(360.0) == '24:0:0.000'
