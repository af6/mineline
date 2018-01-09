# mineline
Terminal/text-based Minecraft Clone. Written in Python 3, no extra packages required. 
# controls
Up                - W

Down              - S

Left              - A

Right             - D

Build             - B

Break             - R

Save              - X

Back in Blocks    - C

Forward in Blocks - V

Inventory         - I

# license
NONE. LITERALLY NONE. 

# load and save
When loading, specify Python3, then mineline.py, then a save. To generate a save:

`python3 [PLACE_TO_GENWORLD.PY] [SIZE_OF_WORLD] [PLACE]`

Example:

`python3 /bla/path/genWorld.py 64 /home/bla/SAVEFILE`

Creates a 64x64 world. 

Press X while in-game to save. 

To load the game, and a save:

`python3 [PLACE_TO_MINELINE.PY] [SAVEFILE]`

Example:

`python3 /path/bla/mineline.py /home/bla/SAVEFILE`

