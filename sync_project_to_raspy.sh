#!/bin/bash

ssh -t raspy "mkdir -p glorious-sunrise/scripts glorious-sunrise/media"
scp -r ~/raspberrypi-code/glorious-sunrise/scripts raspy:/home/pi/glorious-sunrise/
