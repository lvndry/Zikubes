#!/bin/bash

lxterminal -e python3 gui/gui.py
lxterminal -e python3 sound/sound.py
lxterminal -e `./wifi.sh > result.txt`

