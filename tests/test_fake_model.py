import unittest
from fake_model import fake_pred_ep

class TestFakeModel(unittest.TestCase):
    def test_fake_pred_ep(self):
        text = "How do I install Python on Arch Linux?"
        expected_tags = ["python", "linux"]
        result = fake_pred_ep(text)
        self.assertEqual(result, expected_tags)

if __name__ == "__main__":
    unittest.main()