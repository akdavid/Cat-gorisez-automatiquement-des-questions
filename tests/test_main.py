import unittest
from main import pred_ep

class TestMain(unittest.TestCase):
    def test_pred_ep(self):
        text = "How do I install Python in a Docker container?"
        expected_tags = ["python", "docker"]
        result = pred_ep(text)
        self.assertEqual(result, expected_tags)

if __name__ == "__main__":
    unittest.main()