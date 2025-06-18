# import the necessary packages
from imutils import paths
import argparse
import cv2
import os

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
    help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
    help="focus measures that fall below this value will be considered 'blurry'")
ap.add_argument("-o", "--output", required=False, default="output",
    help="path to output directory for labeled images")
args = vars(ap.parse_args())

# Create output folder if it doesn't exist
os.makedirs(args["output"], exist_ok=True)

# loop over the input images
for imagePath in paths.list_images(args["images"]):
    # load the image, convert it to grayscale, and compute the
    # focus measure of the image using the Variance of Laplacian
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    text = "Not Blurry"
    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"
    if fm < args["threshold"]:
        text = "Blurry"
    # show the image with label
    cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    # Save the image to output directory with the same filename
    outputPath = os.path.join(args["output"], os.path.basename(imagePath))
    cv2.imwrite(outputPath, image)
    # Optionally, show the image
    cv2.imshow("Image", image)
    key = cv2.waitKey(0)