import os

name = os.environ.get("INPUT_NAME")
repo = os.environ.get("INPUT_REPO")

print("Hello " + name + ", greetings from " + repo)