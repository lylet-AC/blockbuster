# Pynesthesia

Pynesthesia is a map generation tool that allows a user to draw a simple tile-based game map by importing a sample image.  The sample image should contain basic colors which Pynesthesia will draw textures to.  The user will need to know the RGB colors of each pixel for the input image and input them into Pynesthesia for the program to know which textures to draw per color.

## Installation

Pynesthesia is a program written in Python 3.  Pip3 is the default package installer that comes with python and therefore, it is required to install other dependencies for this program.  For a step-by-step guide on installing pip3, there is a link [here](https://pip.pypa.io/en/stable/installing/).

If you do not have tkinter installed on your computer, use the following command for ubuntu to set it up:
`sudo apt-get install python-tk`

If you are on windows and need to install python3/tkinter, [download](https://www.python.org/downloads/windows/) the python3 installation file.  Ensure upon installing you check the td/tk and IDLE box for installing tkinter with python.

After installing pip3, run the following command in the root directory of this project:
`pip3 install --upgrade pip
pip3 install --user -r requirements.txt`.

Afterwards, run the program using the following line:
`python3 Pynesthesia.py`
