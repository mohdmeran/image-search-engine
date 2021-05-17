# img_viewer.py

import PySimpleGUI as sg
import os
import io
from PIL import Image
from search import search
from index import index

#only support PNG filetype
file_types = [("PNG", "*.png")]

file_list_column = [
    [sg.Image(key="-SELECTED_IMAGE-")],
    [
        sg.Text("Image File"),
        sg.Input(size=(25, 1), key="-FILE-"),
        sg.FileBrowse(file_types=file_types),
        sg.Button("Load Query Image"),
    ],
]

image_result_column = [
        sg.Image(key="-RESULT_IMAGE_1-"),
        sg.Image(key="-RESULT_IMAGE_2-"),
        sg.Image(key="-RESULT_IMAGE_3-"),
        sg.Image(key="-RESULT_IMAGE_4-"),
        sg.Image(key="-RESULT_IMAGE_5-")
    ]

result_viewer_column = [
    [sg.Text("Query result:")],
    [sg.Text(size=(50, 2), key="-TERROR-", text_color="orange")],
    image_result_column,
]

index_column = [
    [
        sg.Text("Indexing Image File"),
        sg.Input(size=(25, 1), key="-INDEX_FOLDER-"),
        sg.FolderBrowse(),
        sg.Button("Go Indexing")
    ],
    [
        sg.Text(size=(40, 1), key="-TINDEX-")
    ]
]

# ----- Full layout -----
layout = [
    [
        sg.Text("Warning: when doing indexing or query image, the program will freeze, due to heavy processing, please wait for a while. Time taken depend on the size of dataset")
    ],
    [
        sg.Column(index_column)
    ],
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(result_viewer_column),
    ]
]

window = sg.Window("Image Search", layout)


#g variables
folder = ""

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Detect an event an do an action accordingly
    if event == "Load Query Image":
        filename = values["-FILE-"]
        if os.path.exists(filename) and os.path.exists("./index.csv") and os.path.exists(folder):
            image = Image.open(filename)
            image.thumbnail((400, 400))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["-SELECTED_IMAGE-"].update(data=bio.getvalue())
            
            result = search.doSearch(filename, folder)
            for (index, resultPath) in enumerate(result, start=1):
                image = Image.open(resultPath)
                image.thumbnail((200,200))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                id = "-RESULT_IMAGE_%s-" % index
                window[id].update(data=bio.getvalue())
        else:
            window["-TERROR-"].update("Missing index.csv or dataset folder!, please do indexing first before proceed to query")

    elif event == "Go Indexing":
        folder = values["-INDEX_FOLDER-"]
        if os.path.exists(folder):
            total = index.goIndex(folder)
            window["-TINDEX-"].update("total image indexed = %d" % total)
        


window.close()
