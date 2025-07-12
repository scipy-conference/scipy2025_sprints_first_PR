from pr_tutorial.buggy_function import angle_to_sexigesimal

def test_angle_to_sexigesimal():
    assert angle_to_sexigesimal(360) == "24:0:0.000"
