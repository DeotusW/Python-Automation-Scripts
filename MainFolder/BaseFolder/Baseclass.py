from configparser import ConfigParser
from Auth.Auth import fuseAuth
from pathlib import Path


class Baseclass:
    @classmethod
    def setup_class(cls):
        CurrentFilePath = Path(__file__).resolve()
        config = ConfigParser()
        config.read(CurrentFilePath.parent.parent/"StepName_and_StepNumber"/"config.fg")
        cls.fuse = fuseAuth(config)
        cls.token = cls.fuse.authentication()