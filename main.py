import os
import glob

name = os.environ.get("INPUT_NAME")
repo = os.environ.get("INPUT_REPO")
ext = os.environ.get("INPUT_EXT")

print("Hello " + name + ", greetings from " + repo)


files = glob.glob("." + '/**/*' + ext, recursive=True)

print("Wow! There are " + str(len(files)) + " files with the extension " + ext + " in this repo!")