#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Para obtener tu API Key:
https://developers.google.com/youtube/v3/getting-started?hl=es-419
"""

import os
import unittest

from youtube import YoutubeApi

#------------ TEST CONFIGURATION ------------

class TestConfig:
    YOUTUBE_API_KEY = os.environ["YOUTUBE_API_KEY"]
    MY_CHANNEL_ID = "UCAgyf7c-giXPM0zgEExB74w"
    VIDEO_URL = "https://www.youtube.com/watch?v=zAPEHIzHPT4"
    
config = TestConfig()

#------------ TEST YOUTUBE API --------------

class TestYoutubeApi(unittest.TestCase):
    def setUp(self):
        self.client = YoutubeApi(config.YOUTUBE_API_KEY)

    def test_channel_videos(self):
        actual = self.client.channel_videos(config.MY_CHANNEL_ID, 
                                            max_res=10)
        self.assertIsInstance(actual, list)

    def test_search_channel(self):
        actual = self.client.search_channel(config.MY_CHANNEL_ID)
        self.assertIsInstance(actual, dict)

    def test_search_video(self):
        actual = self.client.search_video(config.VIDEO_URL)
        self.assertIsInstance(actual, dict)

    def test_channel_video_urls(self):
        actual = self.client.channel_video_urls(config.MY_CHANNEL_ID)
        self.assertIsInstance(actual, list)

    def test_search_by_tag(self):
        actual = self.client.search_by_tag("Medicina germánica")
        self.assertIsInstance(actual, list)

    def test_video_comments(self):
        actual = self.client.video_comments(config.VIDEO_URL)
        self.assertIsInstance(actual, list)

if __name__ == "__main__":
    unittest.main()

""" 
- Para lanzar los tests:
python3 test.py

- Para lanzar un test:
python3 -m unittest test.TestYoutubeApi.search_video
"""