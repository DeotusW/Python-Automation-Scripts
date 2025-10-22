from BaseFolder.BaseHappyPath import BaseHappyPath
from BaseFolder.Baseclass import Baseclass
from RequestMethods.requestMethods import RequestMain


class TestHappyPathHT(BaseHappyPath):
    EXPECTED = {
        "id":"1b3eb239-28a8-4ced-b999-2a7ec1ea17d0",
        "serialNumber": "0412-000105",
        "hardwareType": "ACM"
    }

    PARAMS = {
        "hardwareType": EXPECTED["hardwareType"]
    }

    def test_Hardware_Type(self):
        self.HappyPathTest()