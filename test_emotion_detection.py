"""Unit tests for the EmotionDetection package."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases verifying that the dominant emotion is correctly identified."""

    def test_joy_emotion(self):
        """Statement expressing gladness should return joy as dominant emotion."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        """Statement expressing anger should return anger as dominant emotion."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        """Statement expressing disgust should return disgust as dominant emotion."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        """Statement expressing sadness should return sadness as dominant emotion."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        """Statement expressing fear should return fear as dominant emotion."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
