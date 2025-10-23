from BaseFolder.BaseHappyPath import BaseHappyPath
from BaseFolder.Baseclass import Baseclass
from RequestMethods.requestMethods import RequestMain


class TestHappyPathHT(BaseHappyPath):
    EXPECTED = {
        "serialNumber": "0412-000105",
        "hardwareType": "ACM"
    }

    PARAMS = {
        "hardwareType": EXPECTED["hardwareType"]
    }

    def test_Hardware_Type(self):
        self.HappyPathTest()