import os

from pyengine2.Utils import logger


class Lang:
    def __init__(self, file):
        """
            Create Lang file

            :param file: Path of lang file
        """
        self.file = file

    @property
    def file(self):
        """
            Get path of lang file

            :return: Path of lang file
        """
        return self.__file

    @file.setter
    def file(self, file):
        """
            Set lang file

            :param file: Path of lang file
        """
        self.dic = {}
        self.__file = file
        if os.path.exists(file):
            with open(file) as f:
                for i in f.readlines():
                    if len(i.split(": ")) == 2:
                        self.dic[i.split(": ")[0]] = i.split(": ")[1].replace("\n", "")
                    else:
                        logger.warning("Unknown format of Lang. You must use 'key: value'")
        else:
            logger.error("Lang file doesn't exist")

    def get_translate(self, key, default, *args):
        """
            Get translate of key

            :param key: Key of translation
            :param default: Default value of translation
            :param args: Args to format translation
            :return: Translation
        """
        return self.dic.get(key, default).format(*args)
