def clamp(value, mini=None, maxi=None):
    """
        Block value between mini and maxi

        :param value: Actual value
        :param mini: Minimum value
        :param maxi: Maximum value
        :return: Final value
    """
    if mini is not None and value < mini:
        return mini
    elif maxi is not None and value > maxi:
        return maxi
    return value
