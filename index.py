from colordescriptor import ColorDescriptors
import glob
import cv2

class index:

    def goIndex(data_dir):
    
        # init the color descriptor
        cd = ColorDescriptors((8, 12, 3))

        # open the output index file for writing
        output = open("index.csv", "w")
        total = 0

        # use glob to grab the image paths and loop over them
        for imagePath in glob.glob(data_dir + "/*.png"):
            # extract the image ID (i.e. the unique filename) from the image path and load the image itself
            imageID = imagePath[imagePath.rfind("\\") + 1:]
            image = cv2.imread(imagePath)

            # describe the image
            features =  cd.describe(image)

            # write the features to file
            features = [str(f) for f in features]
            output.write("%s,%s\n" % (imageID, ",".join(features)))

            total += 1

        # close the index file
        output.close()

        return total



