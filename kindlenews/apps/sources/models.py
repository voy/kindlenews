import os
import logging
import datetime

import lxml.html
from pyquery import PyQuery as pq
from django.db import models

from kindlenews.filter import clean

log = logging.getLogger(__name__)

DEFAULT_SELECTORS = {
    'stories': 'item',
    'title': 'title',
    'teaser': 'description',
    'link': 'link',
    'content': None
    
}


class NewsSource(models.Model):

    name = models.CharField(max_length=255, verbose_name="Name", unique=True)
    name_verbose = models.CharField(max_length=255, verbose_name="Verbose name")
    url = models.URLField(max_length=255, verbose_name="URL sel.")
    
    # selectors
    sel_stories = models.CharField(max_length=255, verbose_name="Stories",
        default="item")
    sel_title = models.CharField(max_length=255, verbose_name="Title",
        default="title")
    sel_teaser = models.CharField(max_length=255, verbose_name="Teaser",
        default="description")
    sel_link = models.CharField(max_length=255, verbose_name="Link",
        default="link")
    sel_content = models.CharField(max_length=255, verbose_name="Content")
    
    sel_continuations = models.CharField(max_length=255, blank=True, null=True,
        default=None, verbose_name="Continuations")
    
    max_items = models.IntegerField(blank=True, null=True, default=None,
        verbose_name="Max. items")

    def get_pq(self):
        return pq(url=self.url)
        
    def get_items(self):
        log.info("Fetching '%s'." % self.name)
        d = self.get_pq()
             
        items = []
        i = 0
        for article in d(self.selectors['stories']):
            if i == self.max_items:
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
        
        if self.continuations:
            continuations = pg(article).find(self.continuations)
            for link in continuations:
                url = link.get("href")
                logging.debug("Fetching part %s of %s." % (link.text(), len(continuations)))
                item['content'] += self.get_content(item)
        
        return item
            
    def get_content(self, item):
        elm = pq(url=item['link']).find(self.sel_content)
        content = self.filter(elm.html())
        return content
            
    def get_context(self, items):
        template_values = {
            'name': self.name,
            'name_verbose': self.name_verbose,
            'items': items,
            'today': datetime.date.today()
        }
        return context
        
    def __unicode__(self):
    	return self.name_verbose
        
    class Meta:
        verbose_name = 'Source'
        verbose_name_plural = 'Sources'
        
