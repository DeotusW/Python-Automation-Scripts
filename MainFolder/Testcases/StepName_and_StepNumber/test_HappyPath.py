from BaseFolder.BaseHappyPath import BaseHappyPath

class TestHappyPathSNSN(BaseHappyPath):

    EXPECTED = {
    "serialNumber": "0411-000014",
    "currentStepName": "Activation_Send_NCP",
    "currentStepNumber": 6
    }
    PARAMS = {
        "currentStepName": EXPECTED["currentStepName"],
        "currentStepNumber": EXPECTED["currentStepNumber"]
    }

    def test_stepName_and_stepNumber(self):
        self.HappyPathTest()