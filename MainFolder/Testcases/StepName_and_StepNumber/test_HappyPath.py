from BaseFolder.BaseHappyPath import BaseHappyPath

class TestHappyPathSNSN(BaseHappyPath):

    EXPECTED = {
    "serialNumber": "0412-000105",
    "currentStepName": "Activation_Send_NCP",
    "currentStepNumber": 6
    }
    PARAMS = {
        "currentStepName": EXPECTED["currentStepName"],
        "currentStepNumber": EXPECTED["currentStepNumber"]
    }
    INDEX = 0

    def test_stepName_and_stepNumber(self):
        self.HappyPathTest()