import os
import logging
import datetime

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

    def __init__(self, name, url, selectors, name_verbose=None, filter=clean):
        self.name = name
        self.name_verbose = name_verbose
        self.url = url
        self.selectors = selectors
        self.filter = filter
        
    def get_pq(self):
        print self.url
        return pq(url=self.url)
        
    def get_items(self):
        log.info("Fetching '%s'." % self.name)
        d = self.get_pq()
        
        selectors = DEFAULT_SELECTORS.copy()
        selectors.update(self.selectors)
        
        items = []
        for article in d(selectors['stories']):
            item = {}
            for field in ('title', 'teaser', 'link'):
                elm = article.find(selectors[field])
                print selectors[field], elm
                item[field] = "" if elm is None and field == 'description' else elm.text
            item['content'] = self.get_content(item)
            items.append(item)
            logging.debug("Fetched article '%s'." % item['title'])
        return items
            
    def get_content(self, item):
        elm = pq(url=item[selectors['link']]).find(self.content)
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

