# -*- coding: utf-8 -*-

NEWS_SOURCES = (
    { 'name': 'zdrojak',
      'name_verbose': 'Zdroják',
      'url': 'http://www.zdrojak.cz/rss/clanky/',
      'selectors': {'content': '#main .urs'} },
    { 'name': 'smartmania',
      'name_verbose': 'SmartMania',
      'url': 'http://smartmania.cz/rss.php',
      'selectors': {'content': '#article-text'} },
    { 'name': 'arstechnica',
      'name_verbose': 'ars technica',
      'url': 'http://arstechnica.com/',
      #'max_items': 3,
      'continuations': lambda art: art.find(".pager li a"),
      'selectors': {
	      'stories': '#all-stories .story',
          'title': 'h2',
          'teaser': '.teaser',
          'link': '.read-more-link a',
          'content': '#story .body' } },
)


NEWS_SOURCES_LOOKUP = dict([(item['name'], item) for item in NEWS_SOURCES])


ALLOWED_TAGS = ('p', 'a', 'img', 'em', 'strong', 'pre', 'br', 'i', 'b', 'h2',
    		'h3')
    		
ALLOWED_ATTRIBUTES = ('href', 'src')

