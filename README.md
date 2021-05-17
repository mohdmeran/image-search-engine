=================== IMAGE SEARCHER ========================

requirement:
- Python (latest version)
- dataset (.png image type only)

==== INITIALIZE ===
package required:
- opencv-python
- numpy
- PySimpleGUI
- imutils

`pip install opencv-python numpy PySimpleGUI imutils` or `python -m pip install opencv-python numpy PySimpleGUI imutils`

==== Run Apps ===
run `python main.py`


==== Functionalities ===
1. index an images first before query an image by going clicking `Go Index` button. (Browse the directory first before doing this)
2. wait until indexing is done. A text will appear showing how much image has been indexed when it is done

3. Do an image query by clicking `Load Query Image` (Browse image first before doing this)
4. Wait until it is done. A list of image will appear at the right side (first image is the top similar image)

`Warning:` when doing indexing or query image, it might take a while depending by the size of dataset. please wait for a while (program might crash if click the program while it is still in process)
