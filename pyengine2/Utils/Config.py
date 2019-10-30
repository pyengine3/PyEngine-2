import json
import os

from pyengine2.Utils import logger


class Config:
    def __init__(self, file):
        """
            Config of Game

            :param file: Path of config
        """
        self.dic = {}
        self.created = False
        self.file = file

    def get(self, key, default):
        """
            Get value from config

            :param key: Key of value
            :param default: Default value if key doesn't exist
            :return: Value or default value
        """
        keys = key.split(".")
        if len(keys) == 1:
            return self.dic.get(key, default)
        else:
            value = self.dic
            for i in keys:
                if i != keys[-1]:
                    value = value[i]
                else:
                    value = value.get(i, default)
            return value

    def set(self, key, val):
        """
            Set value of a key

            :param key: Key of value
            :param val: Value
        """
        keys = key.split(".")
        if len(keys) == 0:
            self.dic[key] = val
        else:
            value = self.dic
            for i in keys:
                if i != keys[-1]:
                    value = value[i]
                else:
                    value[i] = val

    def save(self):
        """Save config"""
        with open(self.file, "w") as f:
            f.write(json.dumps(self.dic, indent=4))
        logger.info("Config File saved")

    @property
    def file(self):
        """
            Get path of config file

            :return: Path of file
        """
        return self.__file

    @file.setter
    def file(self, val):
        """
            Set path of config file

            :param val: Path of file
        """
        self.__file = val
        if os.path.exists(val):
            self.created = True
            with open(val, "r") as f:
                self.dic = json.load(f)
        else:
            self.created = False

    def create(self, dic):
        """
            Create config from dict

            :param dic: Dictionary of config
        """
        if self.created:
            logger.warning("Config File already exist but recreated")
        else:
            logger.info("Config File created")
        with open(self.file, "w") as f:
            f.write(json.dumps(dic, indent=4))
        self.dic = dic
