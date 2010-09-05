from BeautifulSoup import BeautifulSoup, NavigableString

from kindlenews.settings import ALLOWED_TAGS, ALLOWED_ATTRIBUTES

def clean(fragment):
    soup = BeautifulSoup(fragment.strip())
    def cleanup(soup):
        for tag in soup:
            if not isinstance(tag, NavigableString):
                if tag.name not in ALLOWED_TAGS:
                    tag.extract()
                else:
                    for attr in tag._getAttrMap().keys():
                        if attr not in ALLOWED_ATTRIBUTES:
                            del tag[attr]
                    cleanup(tag)
    cleanup(soup)
    return unicode(soup) 
