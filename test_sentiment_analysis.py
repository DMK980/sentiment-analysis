"""
    This module is for testing the application
    using Unit tests to make sure everything works 
    
    created: 29/12/2023
"""

# importing required modules
import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        """
            This method tests the sentiment_analyzer module 
            to see if it works when a neutral,positive and negative
            text is inputed
        """

        # When  positive text is inputed
        testCase1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(testCase1["label"],"SENT_POSITIVE")

        # When  negative text is inputed
        testCase2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(testCase2["label"],"SENT_NEGATIVE")

        # When  neutral text is inputed 
        testCase3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(testCase3["label"],"SENT_NEUTRAL")

# calling the unit test
unittest.main()
