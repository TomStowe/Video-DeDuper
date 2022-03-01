"""
    Set the progress bar
    currentProgress: The current progress
    totalProgress: The total progress to display
    length: The length of the progress bar in characters
"""
def setProgressBar(currentProgress, totalProgress, length = 100):
    percent = ("{0:.0f}").format(100 * (currentProgress / float(totalProgress)))
    filledLength = int(length * currentProgress // totalProgress)
    bar = '█' * filledLength + '-' * (length - filledLength)
    print(f'\r|{bar}| {percent}%', end = "\r")