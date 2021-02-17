from django.test import TestCase
from desiderata.templatetags.youtube import embedded_youtube_url

class TestEmbeddedYoutubeUrl(TestCase):

    def test_not_an_url_returns_input(self):
        self.assertEqual(None, embedded_youtube_url(None))
        self.assertEqual('', embedded_youtube_url(''))
        self.assertEqual('not-an-url', embedded_youtube_url('not-an-url'))

    def test_video_id_given(self):
        url = 'https://www.youtube.com/watch?v=2Q1O8XBVbZQ&feature=emb_title'
        self.assertEqual('https://www.youtube.com/embed/2Q1O8XBVbZQ', embedded_youtube_url(url))
    
    def test_url_does_not_contain_vido_id(self):
        url = 'https://www.youtube.com/watch?XXX=2Q1O8XBVbZQ&feature=emb_title'
        self.assertEqual(url, embedded_youtube_url(url))