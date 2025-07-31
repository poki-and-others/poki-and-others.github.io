# imports
import tkinter as tk
from tkinter import filedialog
import os

IMAGE_FILE_TYPES = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
VIDEO_FILE_TYPES = ("mp4")

# select working directory
    # this is where the program will start
    # and also where the .txt file will be left
    # image directories must be subdirectories
root = tk.Tk()
root.withdraw()
print("Select destination directory for HTML text file.")
destination_file_path = filedialog.askdirectory()
os.chdir(destination_file_path)
#print(destination_file_path)

# create empty notepad (override)
text_file = open("preppedHTML.txt", "w")

# select image directory
print("Select folder with the image folders.")
image_file_path = filedialog.askdirectory()
#print(image_file_path)

project_list = os.listdir(image_file_path)
project_list = [image_file_path + "/" + project for project in project_list]
project_list.sort(key=os.path.getctime)
project_list = [project.removeprefix(image_file_path + "/")  for project in project_list]

    # has directories with one folder per element to be made
        # A) folders with singular image --> img for HTML
        # B) folders with multiple image --> scrolling image for HTML and JSS
        # C) folders with video --> video for HTML

# iterate through image directory
# for each image folder
for project in project_list:
    print(image_file_path.removeprefix(destination_file_path))
    project_path = image_file_path.removeprefix(destination_file_path + "/") + "/" + project
    items = os.listdir(project_path)

    print(items)
    text_file.write("<!-- " + project + " -->\n")
    text_file.write("\t\t<h3>" + project + "</h3>\n")
    text_file.write("\t\t<div class=\"imageBlock\">\n")


    # determine case A, B, C based on number of items
    # if one file
    if len(items) == 1:
        item = items[0]
        # if image
        if item.lower().endswith(IMAGE_FILE_TYPES):
            # createSingleImage()
            itemHTML = "\t\t\t<img src=\"" + project_path + "/" + item + "\">\n"
            text_file.write(itemHTML + "\n")

        # if video
        elif item.lower().endswith(VIDEO_FILE_TYPES):
            # createSingleVideo()
            itemHTML = "\t\t\t<video src=\"" + project_path + "/" + item + "\" autoplay loop muted></video>\n"
            text_file.write(itemHTML + "\n")
        else:
            text_file.write("<-- SKIP -->\n")

    # if multiple files
    else:
        # if all images
        if all(item.lower().endswith(IMAGE_FILE_TYPES) for item in items):
            num_image = len(items)
            path_list = [project_path + "/" + item for item in items]
            image_list = str(path_list).replace("'", "").replace("[","").replace("]", "")

            # set 1st image
            itemHTML = "\t\t\t<img src=\"" + project_path + "/" + items[0] + "\""
            itemHTML = itemHTML + " data-num_image=\"" + str(num_image) + "\" data-curr_image=\"0\" data-image_set=\"" + image_list + "\">\n"
            text_file.write(itemHTML)
            text_file.write("\t\t\t<br>\n\t\t\t<button onclick=\"previousImage(this)\"><<</button>\n\t\t\t<button onclick=\"nextImage(this)\">>></button>\n")
        else:
            text_file.write("<-- SKIP -->\n")

    text_file.write("\t\t</div>\n\n")
    # else
        # skip, list as error