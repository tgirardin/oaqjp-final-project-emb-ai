import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am very happy today!")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        result = emotion_detector("I am feeling very down and depressed.")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_anger(self):
        result = emotion_detector("I hate waiting in long lines!")
        self.assertEqual(result["dominant_emotion"], "anger")

if __name__ == '__main__':
    unittest.main()
