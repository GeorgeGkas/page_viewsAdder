"""
AUTHOR: George G. Gkasdrogkas
LICENSE: MIT
VERSION: 1.0 (stable)

Usage:
python views_bot.py <url> <Number>

"""

from selenium import webdriver
from time import sleep
import sys
import os

def printProgress (iteration, total, prefix = '', suffix = '', decimals = 2, barLength = 100):
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '=' * filledLength + ' ' * (barLength - filledLength)
    sys.stdout.write('%s [%s] %s%s %s\r' % (prefix, bar, percents, '%', suffix)),
    sys.stdout.flush()
    if iteration == total:
        print("\n")

def getProfile():
    profile = webdriver.FirefoxProfile()
    profile.set_preference('browser.privatebrowsing.autostart', True)
    return profile

def main():
    URL = str(sys.argv[1]);
    VIEWS_TO_GENERATE = int(sys.argv[2]);

    print '''
 Views Bot 1.0 - (C) 2016 George G. Gkasdrogkas
 https://github.com/georgegks
    \n'''

    current_views = 0
    PAGE_TITLE = str()

    printProgress(0, VIEWS_TO_GENERATE, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

    for i in xrange(0, VIEWS_TO_GENERATE):
        browser = webdriver.Firefox(firefox_profile=getProfile())
        browser.get(URL)
        PAGE_TITLE = browser.title
        current_views += 1
        sleep(2)
        printProgress(current_views, VIEWS_TO_GENERATE, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
        browser.quit()

    print '\n[*] Program finished.'
    print 'You have add ', current_views, ' total views in "', PAGE_TITLE, '"'

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print '\n\n[KeyboardInterrupt] Closing program...'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
