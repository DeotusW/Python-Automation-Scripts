from configparser import ConfigParser
from PythonAutomation.Pycharm.Auth.Auth import fuseAuth


class Baseclass:
    @classmethod
    def setup_class(cls):
        config = ConfigParser()
        config.read("C:/Users/dwilson3/Documents/Pycharm/PythonAutomation/Pycharm/StepName_and_StepNumber/config.fg")
        cls.fuse = fuseAuth(config)
        cls.token = cls.fuse.authentication()