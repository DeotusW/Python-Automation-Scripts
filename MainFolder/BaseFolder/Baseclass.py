from configparser import ConfigParser
from Auth.Auth import fuseAuth
from pathlib import Path


class Baseclass:
    @classmethod
    def setup_class(cls):
        CurrentFilePath = Path(__file__).resolve()
        config = ConfigParser()
        try:
            config.read(CurrentFilePath.parent.parent/"Testcases"/"config.fg")
            cls.fuse = fuseAuth(config)
            cls.token = cls.fuse.authentication()
        except FileNotFoundError:
            raise FileNotFoundError("The Config file is missing - File not Found!")