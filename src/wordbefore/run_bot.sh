
DATE=/usr/bin/date

cd ~/andor
source venv/bin/activate
cd ./src/wordbefore/

python3 get_wordles.py

if [[ $? -eq 0 ]]; then 
    echo "wordles updated on ${DATE}"
else
    echo "wordles update failed on ${DATE}"
fi

deactivate


