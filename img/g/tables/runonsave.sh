#!/bin/bash
#fswatch -x -0 viztable05.py | xargs -0 -n 1 -I {} python viztable05.py
fswatch -0 *.py | xargs -0 -n 1 -I {} python '{}'
