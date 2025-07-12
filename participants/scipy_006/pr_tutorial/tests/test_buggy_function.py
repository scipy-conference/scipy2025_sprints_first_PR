from pr_tutorial.buggy_function import angle_to_sexigesimal


def test_angle_to_sexigesimal():
    """Test for angle_to_sexigesimal function"""

    assert angle_to_sexigesimal(0) == '0:0:0.000'
    assert angle_to_sexigesimal(5) == '0:20:0.000'
    assert angle_to_sexigesimal(15) == '1:0:0.000'
    assert angle_to_sexigesimal(30) == '2:0:0.000'
    assert angle_to_sexigesimal(45) == '3:0:0.000'
    assert angle_to_sexigesimal(60) == '4:0:0.000'
    assert angle_to_sexigesimal(90) == '6:0:0.000'
    assert angle_to_sexigesimal(180) == '12:0:0.000'
    assert angle_to_sexigesimal(360) == '0:0:0.000'
