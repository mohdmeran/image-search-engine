from colordescriptor import ColorDescriptors
from searcher import Searcher
import cv2

# Code Source : https://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/

class search:
    def doSearch(queryPath, resultPath):
        # contruct the argument parser and parse the arguments
        indexPath = "./index.csv"

        # initialize the image descriptor
        cd = ColorDescriptors((8, 12, 3))

        # load the query image and describe it
        print(queryPath)
        query = cv2.imread(queryPath)
        features = cd.describe(query)

        # perform the search
        searcher = Searcher(indexPath)
        results = searcher.search(features)

        final = []

        # loop over the results
        for (score, resultID) in results:
            # load the result image and store it inside final
            final.append(resultPath + "/" + resultID)

        return final
