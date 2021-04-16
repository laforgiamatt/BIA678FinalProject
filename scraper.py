import os.path
import re

import twitterFunctions as twitfun

def checkDataParsed(filename):
    if os.path.exists(filename):
        return True
    else:
        return False


def run_twitter(dataFilename='twitter_data.txt', rebuildTraining=True, setSize=10000, scrapeMore=False):
    if checkDataParsed(dataFilename) and rebuildTraining==False and scrapeMore == False:
        return
    else:
        if checkDataParsed(dataFilename) and rebuildTraining == True and scapeMore == False:
            os.remove(dataFilename)
            twitfun.run(dataFilename, setSize)
        if checkDataParsed(dataFilename) and scrapeMore == True:
            twitfun.run(dataFilename, setSize)
    print('Done')
    return