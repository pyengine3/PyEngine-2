from tkinter import Tk


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


def set_clipboard(text):
    """
        Put text in Clipboard

        :param text: Text to put
    """
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()
    r.destroy()


def get_clipboard():
    """
        Get text of Clipboard

        :return: Text of Clipboard
    """
    root = Tk()
    # keep the window from showing
    root.withdraw()
    text = root.clipboard_get()
    root.destroy()
    return text
