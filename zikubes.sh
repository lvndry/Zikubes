#!/bin/bash

python3 sound/sound.py &
python3 gui/gui.py &
./wifi.sh > result.txt
