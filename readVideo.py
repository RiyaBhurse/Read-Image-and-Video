# what is cv2 in python?
# cv2 is a library in python used for computer vision, machine learning, and image processing. 
# It is used to perform various operations on images and videos like image capturing, image processing, image editing, and many more.
import cv2 as cv

# what is cv.VideoCapture()?
# cv.VideoCapture() is a function in OpenCV used to capture video from the camera or a video file.
capture = cv.VideoCapture("Videos/dog.mp4")

# images, videos, live videos
def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# only for live video
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)



while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# what is capture.release()?
# It releases the video capture object. 
# It releases the video file or the capturing device.
# It is used to close the video file or the capturing device. 
# It is used to release the video file or capturing device after the job is done.

# what do you mean by release() in OpenCV?
# The release() function in OpenCV is used to release the video file or capturing device. It is used to release the video file or capturing device after the job is done.
# release where?
# It releases the video capture object. It releases the video file or the capturing device.
capture.release()

# what is cv.destroyAllWindows()?
# It is used to destroy all the windows that are created. 
cv.destroyAllWindows()

