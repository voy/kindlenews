import os
import logging
import datetime

import lxml.html
from pyquery import PyQuery as pq
from google.appengine.ext.webapp import template

from kindlenews.filter import clean


log = logging.getLogger(__name__)


DEFAULT_SELECTORS = {
    'stories': 'item',
    'title': 'title',
    'teaser': 'description',
    'link': 'link',
    'content': None
}


class NewsSource:

    def __init__(self, name, url, selectors, name_verbose=None, filter=clean,
            **config):
        self.name = name
        self.name_verbose = name_verbose
        self.url = url
        self.filter = filter
        self.config = config
        
        self.selectors = DEFAULT_SELECTORS.copy()
        self.selectors.update(selectors)
        
    def get_pq(self):
        return pq(url=self.url)
        
    def get_items(self):
        log.info("Fetching '%s'." % self.name)
        d = self.get_pq()
             
        max_items = self.config.get('max_items', None)
        items = []
        i = 0
        for article in d(self.selectors['stories']):
            if i == max_items:
                break
            article.make_links_absolute(base_url=self.url)
            item = self.get_item(article)
            items.append(item)
            logging.debug("Fetched article '%s'." % item['title'])
            i += 1
            
        return items
        
    def get_item(self, article):
        item = {}
        
        for field in ('title', 'teaser', 'link'):
            elm = pq(article).find(self.selectors[field])
            
            if elm.size() == 0:
                if field == 'description':
                    item[field] = ""
                else:
                    raise ValueError("Field '%s' should have some value." % field)
            
            if field == 'link' and elm[0].tag == 'a':
                item[field] = elm[0].get('href')
            else:
                item[field] = elm.text()
                
        item['content'] = self.get_content(item)
        
        continuations = self.config.get('continuations', None)
        if continuations:
            continuations = continuations(article) or []
            for link in continuations:
                url = link.get("href")
                logging.debug("Fetching part %s of %s." %
                        (link.text(), len(continuations)))
                item['content'] += self.get_content(item)
        
        return item
            
    def get_content(self, item):
        elm = pq(url=item['link']).find(self.selectors['content'])
        content = self.filter(elm.html())
        return content
            
    def render(self, items):
        template_values = {
            'name': self.name,
            'name_verbose': self.name_verbose,
            'items': items,
            'today': datetime.date.today()
        }
        path = os.path.join(os.path.dirname(__file__), 'templates', 'book.html')
        print template.render(path, template_values)

