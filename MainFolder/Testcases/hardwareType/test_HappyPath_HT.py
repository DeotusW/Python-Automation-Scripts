from BaseFolder.BaseHappyPath import BaseHappyPath
from BaseFolder.Baseclass import Baseclass
from RequestMethods.requestMethods import RequestMain


class TestHappyPathHT(BaseHappyPath):
    EXPECTED = {
        "serialNumber": "0411-000014",
        "hardwareType": "ACM"
    }

    PARAMS = {
        "hardwareType": EXPECTED["hardwareType"]
    }
    INDEX = 1

    def test_Hardware_Type(self):
        self.HappyPathTest()