from BaseFolder.BaseHappyPath import BaseHappyPath

class TestHappyPathSNSN(BaseHappyPath):

    EXPECTED = {
    "id":"985775ee-470a-4970-9a19-8fdf6d9d6ff9",
    "serialNumber": "0412-000105",
    "currentStepName": "Activation_Send_NCP",
    "currentStepNumber": 6
    }
    PARAMS = {
        "currentStepName": EXPECTED["currentStepName"],
        "currentStepNumber": EXPECTED["currentStepNumber"]
    }

    def test_stepName_and_stepNumber(self):
        self.HappyPathTest()