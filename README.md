# KTANE_maze
Code to run the physical KTANE homage maze module

This set of python3 files provides the software functionality for the physical maze module connecting to a KTANE homage server.

The physical maze is designed to run on a Raspberry Pi with a SenseHat.

Beyond that, the only configuration needed is to point the bomb_network object at the IP address of the homage server.

Description of files:

maze.py - primary executable. This is the file used to start the module.
blueprints.py - imported by maze.py. This file contains the maze blueprints and may be modified as needed to add/change/remove mazes.
interpreter.py - this is a standalone program, designed to be run on a device with a GUI. It is for testing maze blueprints. A working copy can be found here: https://repl.it/@jonathanihlein/KTANE-Maze-Interpreter
bomb_network.py - imported by maze.py. This file handles connectivity to and querying of the homage server.
