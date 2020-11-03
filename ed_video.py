import cv2 as cv
import numpy as np

# if one wanted to use a recording add the file inplace of the 0
camera = cv.VideoCapture(0)

while True:
    _, frame = camera.read()
    cv.imshow('Camera', frame)

    # applies laplacian filter to video stream
    laplacian = cv.Laplacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow('Laplacian', laplacian)

    # applies canny filter to video stream
    # can change the two values in Canny() to adjust the noise
    # lower values = more noise     high values = less noise
    edges = cv.Canny(frame, 90, 90)
    cv.imshow('Canny', edges)

    if cv.waitKey(5) == ord('x'):
        break

camera.release()
cv.destroyAllWindows()
