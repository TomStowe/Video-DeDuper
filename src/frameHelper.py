import cv2, numpy as np

def cropFrame(frame, crop, width, height):
    # If the crop is invalid, or there is no crop applied, return without cropping
    if (len(crop) != 4 or (crop[0] == 0 and crop[1] == 0 and crop[2] == 0 and crop[3] == 0)):
        return frame
    
    # Else crop the image and resize back to the correct frame size
    # Crop the frame [startRow: endRow, startColumn: endColumn]
    return cv2.resize(frame[crop[1]: height - crop[3], crop[0]: width - crop[2]], (width, height), interpolation=cv2.INTER_AREA)
    

# Check whether 2 of the frames are equal
def areFramesEqual(f1, f2, permittedDifferenceThreshold):
    if (f1.shape == f2.shape):
        diff = f1.copy()
        cv2.absdiff(f1, f2, diff)
        
        return np.concatenate(diff).sum() <= permittedDifferenceThreshold
        
    return False