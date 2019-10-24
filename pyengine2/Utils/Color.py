from pyengine2.Utils.Utils import clamp


class Color:
    def __init__(self):
        """
            Initialize Color object with all parameters to 0

            .. note:: You may not use this constructor. Use "from" classmethod.
        """
        self.r = 0
        self.g = 0
        self.b = 0
        self.a = 255

    def darker(self, force=1):
        """
            Create darker color object with a force multiplier

            :param force: Force multiplier
            :type force: int
            :return: Color object
            :rtype: Color
        """
        nb = clamp(force, 1)
        rgb = (clamp(x - 10*nb, 0, 255) for x in self.get_rgb())
        return Color.from_rgba(*rgb, self.a)

    def lighter(self, force=1):
        """
            Create lighter color object with a force multiplier

            :param force: Force multiplier
            :type force: int
            :return: Color object
            :rtype: Color
        """
        nb = clamp(force, 1)
        rgb = (clamp(x + 10*nb, 0, 255) for x in self.get_rgb())
        return Color.from_rgba(*rgb, self.a)

    def get_rgb(self):
        """
            Return tuple with rgb values

            :return: Tuple with rgb values
            :rtype: Tuple[int, int, int]
        """
        return self.r, self.g, self.b

    def get_rgba(self):
        """
            Return tuple with rgba values

            :return: Tuple with rgba values
            :rtype: Tuple[int, int, int]
        """
        return self.r, self.g, self.b, self.a

    def get_html(self):
        """
            Return html color format for Color object

            :return: html color
            :rtype: str
        """
        return ("#"+hex(self.r)[2:]+hex(self.g)[2:]+hex(self.b)[2:]+hex(self.a)[2:]).upper()

    def __repr__(self):
        """
            Represents Color Object

            :return: RGBA Values convert in string
            :rtype: str
        """
        return str(self.get_rgba())

    @classmethod
    def from_rgb(cls, r, g, b):
        """
            Create Color object from rgb values

            :param r: Red Value
            :param g: Green Value
            :param b: Blue Value
            :type r: int
            :type g: int
            :type b: int
            :return: Color Object
            :rtype: Color
        """
        color = Color()
        color.r = r
        color.g = g
        color.b = b
        return color

    @classmethod
    def from_rgba(cls, r, g, b, a):
        """
            Create Color object from rgba values

            :param r: Red Value
            :param g: Green Value
            :param b: Blue Value
            :param a: Alpha Value
            :type r: int
            :type g: int
            :type b: int
            :type a: int
            :return: Color Object
            :rtype: Color
        """
        color = Color.from_rgb(r, g, b)
        color.a = a
        return color

    @classmethod
    def from_color(cls, color):
        """
            Create Color object from anthor color object

            :param color: Basic Color
            :type color: Color
            :return: Color Object
            :rtype: Color
        """
        return Color.from_rgba(*color.get_rgba())

    @classmethod
    def from_html(cls, html):
        """
            Create Color object from html color format

            :param html: HTML Color format
            :type html: str
            :return: Color Object
            :rtype: Color
        """
        if len(html) == 7 or len(html) == 9:
            if len(html) == 7:
                html += "FF"
            return Color.from_rgba(*(int(html[1:3], 16), int(html[3:5], 16), int(html[5:7], 16), int(html[7:9], 16)))
        else:
            raise ValueError("Hexa must be a 7 or 9 lenght string (#RRGGBBAA)")

    @classmethod
    def from_name(cls, name):
        """
            Create Color object from name

            :param name: Name
            :type name: str
            :return: Color Object
            :rtype: Color
        """
        colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "gray": (128, 128, 128),
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "fuchsia": (255, 0, 255),
            "yellow": (255, 255, 0),
            "cyan": (0, 255, 255),
            "lime": (0, 128, 0),
            "brown": (128, 0, 0),
            "navyblue": (0, 0, 128),
            "olive": (128, 128, 0),
            "purple": (128, 0, 128),
            "teal": (0, 128, 128),
            "silver": (192, 192, 192),
            "orange": (255, 128, 0)
        }
        return Color.from_rgb(*colors[name])


