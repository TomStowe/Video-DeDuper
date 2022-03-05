import argparse

"""
    Parse the arguments for the video de-duper.
    Returns: A tuple of the options (inputVideoPath, frameDifference, fpsOverride)
"""
def parseArguments():
    parser = argparse.ArgumentParser(description='A simple application to de-dupe the frames in a video')
    parser.add_argument("-i", "--inputVideo", help="The input video to be de-duped", type=str, required=True)
    parser.add_argument("-o", "--outputVideo", help="The output video file", type=str, default="output.avi")
    parser.add_argument("-d", "--frameDifference", help="A threshold used for comparing how similar frames are. A higher number means more frames removed", type=int, default=50)
    parser.add_argument("-f", "--fpsOverride", help="Set the fps of the video. If not specified, will use the fps of the input video", type=int)
    parser.add_argument("-c", "--crop", help="The bounds to crop the image by in the format [leftCrop, topCrop, rightCrop, bottomCrop] in pixels", type=int, nargs="*", default=[0,0,0,0])
    parser.add_argument("-p", "--preview", help="Preview the frames as they are being generated. (Note this preview is indicative of the cropping, but not the framerate or de-duping properties)", type=bool, default=False)
    parser.add_argument("-v", "--videoCodec", help="The FourCC abbreviation video codec to use", type=str, default="MJPG")
    arguments = parser.parse_args()
    
    return (arguments.inputVideo, arguments.frameDifference, arguments.fpsOverride, arguments.crop, arguments.preview, arguments.outputVideo, arguments.videoCodec)