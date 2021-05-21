#!/usr/bin/bash
grim -g "$(slurp -p)" -t ppm - | convert - -format '%[pixel:p{0,0}]' txt:- | awk 'NR==2{print $3}'
