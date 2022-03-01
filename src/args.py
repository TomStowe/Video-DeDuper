import argparse

"""
    Parse the arguments for the video de-duper.
    Returns: A tuple of the options (inputVideoPath, frameDifference, fpsOverride)
"""
def parseArguments():
    parser = argparse.ArgumentParser(description='A simple application to de-dupe the frames in a video')
    parser.add_argument("-i", "--inputVideo", help="The input video to be de-duped", type=str, required=True)
    parser.add_argument("-d", "--frameDifference", help="A threshold used for comparing how similar frames are. A higher number means more frames removed", type=int, default=50)
    parser.add_argument("-f", "--fpsOverride", help="Set the fps of the video. If not specified, will use the fps of the input video", type=int)
    arguments = parser.parse_args()
    
    return (arguments.inputVideo, arguments.frameDifference, arguments.fpsOverride)