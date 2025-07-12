import math


def angle_to_sexigesimal(angle_in_degrees: float, decimals=3):
    """
    Convert the given angle to a sexigesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`

    """
    if math.floor(decimals) != decimals:
        raise OSError('decimals should be an integer!')

    assert angle_in_degrees >= 0
    assert angle_in_degrees <= 360

    hours_num = angle_in_degrees*6/180.
    hours = math.floor(hours_num)

    min_num = (hours_num - hours)*60
    minutes = math.floor(min_num)

    seconds = (min_num - minutes)*60

    return f"{int(hours)}:{int(minutes)}:{int(seconds)}"
