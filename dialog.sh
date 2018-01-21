#!/bin/bash
listfolder='/home/pi/.attract/romlists/'

menu=$(dialog --stdout --menu "Convert which romlists?" 10 30 4 \
    1 "Convert all" \
    2 "Select lists manually")

cmd=(dialog --stdout --no-items \
        --separate-output \
        --ok-label "Convert" \
        --checklist "Select romlists to convert:" 22 76 16)

if (($menu == 1))
then
files=$(find $listfolder -maxdepth 1 -name '*.txt' -printf '%f\n')
python RomlistConverter.py $files
elif (($menu == 2))
then
options=$(find $listfolder -maxdepth 1 -name '*.txt' -printf '%f\n' | awk '{print $1, "off"}')
choices=$("${cmd[@]}" ${options})
python RomlistConverter.py $choices
fi
