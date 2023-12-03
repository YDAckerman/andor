#!/bin/bash
DATE=$(/usr/bin/date)
USR=$(whoami)

/home/USR/andor/venv/bin/python3 /home/USR/andor/src/wordbefore/get_wordles.py

if [[ $? -eq 0 ]]; then 
    echo "wordles updated on $DATE"
else
    echo "wordles update failed on $DATE"
fi

