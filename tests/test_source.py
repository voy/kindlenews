import os

from unittest import TestCase

from pyquery import PyQuery as pq

from kindlenews.source import NewsSource
from kindlenews.settings import NEWS_SOURCES_LOOKUP


def mock_content(filename):
    path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
    f = open(os.path.join(path, 'fixtures', filename))
    contents = '\n'.join(f.readlines())
    f.close()
    return lambda *args, **kwargs: pq(contents)


class ZdrojakTestCase(TestCase):
    
    def setUp(self):
        NewsSource.get_pq = mock_content("zdrojak.xml")
        NewsSource.get_content = mock_content("zdrojak_article.html")
        
    def testContent(self):
        zdrojak = NEWS_SOURCES_LOOKUP['zdrojak']
        ns = NewsSource(**zdrojak)
        items = ns.get_items()
        self.assertTrue(len(items) > 0)
        ns.render(items)


class ArsTechnicaTestCase(TestCase):
    
    def setUp(self):
        NewsSource.get_pq = mock_content("arstechnica.html")
        NewsSource.get_content = mock_content("arstechnica_article.html")
        
    def testContent(self):
        zdrojak = NEWS_SOURCES_LOOKUP['arstechnica']
        ns = NewsSource(**zdrojak)
        items = ns.get_items()
        self.assertTrue(len(items) > 0)
        ns.render(items)
