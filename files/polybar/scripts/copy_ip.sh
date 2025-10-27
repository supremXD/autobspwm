#!/bin/bash
IP=$(~/.config/polybar/scripts/ip.sh)
export DISPLAY=:0
echo -n "$IP" | xclip -selection clipboard