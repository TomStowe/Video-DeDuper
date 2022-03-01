import cv2
import numpy as np
from src.args import parseArguments 
from src.progressBar import setProgressBar

# The output file to use
outputVideo = 'output.avi'

# Get the arguments
(inputVideo, permittedDifferenceThreshold, fps) = parseArguments()

# Check whether 2 of the frames are equal
def areFramesEqual(f1, f2):
    if (f1.shape == f2.shape):
        diff = f1.copy()
        cv2.absdiff(f1, f2, diff)
        
        return np.concatenate(diff).sum() <= permittedDifferenceThreshold
        
    return False

# Open the video
print("Opening Video")
originalVideo = cv2.VideoCapture(inputVideo)

# Check if video can be read
if (not originalVideo.isOpened()): 
  print("Can't open video")

# Get the resolution of the video
width = int(originalVideo.get(3))
height = int(originalVideo.get(4))

# Get the fps from the video if it has not been overridden
if (fps is None):
    fps = originalVideo.get(cv2.CAP_PROP_FPS)

# Setup the output file
out = cv2.VideoWriter(outputVideo, cv2.VideoWriter_fourcc('M','J','P','G'), fps, (width, height))

previousFrame = np.empty([0,0])

# Monitoring Information
currentFrameNumber = 0
totalFrames = originalVideo.get(cv2.CAP_PROP_FRAME_COUNT)
framesReducedBy = 0

print("De-Duping Video")

# Iterate over every frame
while(True):
    success, frame = originalVideo.read()

    if (not success):
        break

    # Deal with the progress bar
    currentFrameNumber += 1
    if (currentFrameNumber % 20 == 0):
        setProgressBar(currentFrameNumber, totalFrames, length = 40)

    # If this and the previous frame aren't equal, add this frame to the output
    if (not areFramesEqual(frame, previousFrame)):
        out.write(np.copy(frame))
    else:
        framesReducedBy += 1
    
    # Update the previous frame
    previousFrame = np.copy(frame)
    
# Release the input and output video
originalVideo.release()
out.release()
print("Video Successfully De-Duped! Reduced the video from " + str(round(totalFrames, 0)) + " to " + str(round(totalFrames - framesReducedBy, 0)) + " frames!")