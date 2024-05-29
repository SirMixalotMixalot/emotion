import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def help_me_test(self, phrase : str, dominant_emotion: str):
        self.assertEqual(emotion_detector(phrase)['dominant_emotion'], dominant_emotion )
    def test_dominant_emotion(self):
        self.help_me_test("I am glad this happened", "joy")
        self.help_me_test("I am really mad about this", "anger")
        self.help_me_test("I feel disgusted just hearing about this", "disgust")
        self.help_me_test("I am so sad about this", "sadness")
        self.help_me_test("I am really afraid that this will happen", "fear")

if __name__ == "__main__":
    unittest.main()


