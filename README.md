# 🎥 Video De-Duper 🎥
A simple application for de-duplicating the frames in a video (ignores audio). Useful for somewhat fixing laggy videos

## ⚙️ Setup
1. Download the latest build from the releases section on the GitHub page
2. Unzip the files
3. Using the cmd or terminal of your machine, navigate to the folder and run `videoDeduper.exe` with the arguments as described below
    * E.g. `videoDeduper.exe -i myVideo.mp4`

## ✅ Arguments
When calling the video de-duper, the following arguments can be used
|         Argument          	|                   Description                             	                                                                                  |   Type  	| Required 	| Default 	    |
|:---------------------------:	|:----------------------------------------------------------------------------------------------------------------------------------------------: |:-------:	|:--------:	|:-------:	    |
| `--inputVideo` (`-i`)      	|      The input video to be de-duped                          	                                                                                  |  String 	|     Y    	|   N/A   	    |
| `--outputVideo` (`-o`)      	|      The output video file                                 	                                                                                  |  String 	|     N    	|`output.avi` 	|
| `--frameDifference` (`-d`)  	| A threshold used for comparing how similar frames are. A higher number means more frames removed                                                |   Int   	|     N    	|   50   	    |
|  `--fpsOverride` (`-f`)  	    |Set the fps of the video. If not specified, will use the fps of the input video                                                                  |   Int    	|     N    	|   N/A  	    |
|  `--crop` (`-c`)       	    |The bounds to crop the image by in the format `leftCrop, topCrop, rightCrop, bottomCrop` in pixels                                               |   Int[]  	|     N    	| `0 0 0 0`     |
|  `--preview` (`-p`)  	        |Preview the frames as they are being generated. (Note this preview is indicative of the cropping, but not the framerate or de-duping properties) |   Bool    	|     N    	|   False  	    |
|  `--videoCodec` (`-v`)  	    |The FourCC abbreviation video codec to use                                                                                                       |  String    	|     N    	|   `MJPG` 	    |

## Local Dev
1. Install the python dependencies in `requirements.txt`
2. Run the CI runner using `python3 main.py -i <videoLocation>` replacing the field between `<>`

## Building
1. Setup you [local dev environment](#local-dev)
2. Run the `build.cmd`
## 🎓 Licence
This software is released under the [GNU AGPLv3](LICENSE) licence

## 👨 The Author
[Please click here to see more of my work!](https://tomstowe.co.uk)
