import logging
import sys
import os

from kindlenews.source import NewsSource
from kindlenews.settings import NEWS_SOURCES_LOOKUP

if __name__ == '__main__':
    if len(sys.argv) == 1:
    	sys.stderr.write('Usage: %s [SOURCE]\n' % os.path.basename(__file__))
    	sys.exit(1)


    config = NEWS_SOURCES_LOOKUP.get(sys.argv[1], None)
    if config is None:
	sys.stderr.write('Unknown source!\n\n')
    	sys.stderr.write('Usage: %s [SOURCE]\n' % os.path.basename(__file__))
    	sys.exit(1)
    	
    logging.basicConfig(level=logging.DEBUG)
    source = NewsSource(**config)
    items = source.get_items()
    source.render(items)
