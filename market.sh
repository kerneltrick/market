#!/bin/bash

if [ "$#" -eq 2 ]; then
    /home/mark/.virtualenvs/market/bin/python /home/mark/projects/market/market.py $1 $2
fi
if [ "$#" -eq 3 ]; then
    /home/mark/.virtualenvs/market/bin/python /home/mark/projects/market/market.py $1 $2 $3
fi
