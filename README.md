# BlockBuster
This repository contains code for the pygame game blockbuster.  BlockBuster is an Arkanoid clone that generates levels from image input.  BlockBuster gets its name from most of the levels being tile maps of popular movie screen shots the user gets to destroy with a ball and a paddle.

## Installation

BlockBuster is a program written in Python 3.  Pip3 is the default package installer that comes with python and therefore, it is required to install other dependencies for this program.  For a step-by-step guide on installing pip3, there is a link [here](https://pip.pypa.io/en/stable/installing/).

If you are on windows and need to install python3, [download](https://www.python.org/downloads/windows/) the python3 installation file.

If you are on ubuntu and need to install python3, it can be done with the command:
`sudo apt-get install python3`

After installing pip3, run the following command in the root directory of this project:
`pip3 install --upgrade pip`
`pip3 install --user -r requirements.txt`.


## Execution

After the dependencies have been properly installed, use the following command to run the game.

`python3 blockbuster.py`

Or, if you are a windows user and python3 is not a recognized bash command, try using:

`py -3 blockbuser.py`

## The Settings File

BlockBuster is a game that must be configured by editing the `settings.py` file located in the `src` directory.  Primarily the user will need to edit the `LEVEL` parameter.  This parameter is the image file that is converted into the level that the user plays.  BlockBuster searches for this image in the `input` directory, also located in the `src` directory.

Some other notable settings can adjust the default height and width of the paddle with `PADDLE_HEIGHT` and `PADDLE_WIDTH` respectively.  We can also edit the amount of lives the player starts with by adjusting the `BALLS` parameter.  Furthermore we can adjust speed and size of the ball with `BALL_SPEED` and `BALL_SIZE`.  We can also adjust the width and height of the window with the `WIDTH` and `HEIGHT`.

All of the values must be integer values and are measured in pixels, or if the variable is related to speed it is measured in pixels per frame.
