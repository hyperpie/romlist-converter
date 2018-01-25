#!/bin/bash
listfolder='/home/pi/.attract/romlists/'

regex='\(.*cave.*\|.*pgm.*\|.*psikyo.*\|.*technos.*\|.*visco.*\|.*wwf.*\|.*classics.*\|.*collection.*\|.*hacks.*\|.*shmup.*\|.*hacks.*\).*.txt'

menu=$(dialog --stdout --menu "Convert which romlists?" 10 50 20 \
    1 "Convert all collections" \
    2 "Select manually from collections" \
    3 "Select from all rom lists")

cmd=(dialog --stdout --no-items \
        --separate-output \
        --ok-label "Convert" \
        --checklist "Select romlists to convert (SPACE selects):" 22 76 16)

if (($menu == 1))
then
files=$(find $listfolder -maxdepth 1 -iregex $regex -printf '%f\n')
python RomlistConverter.py "$files"
elif (($menu == 2))
then
options=$(find $listfolder -maxdepth 1 -iregex $regex -printf "%f\n" | sed 's/ /+/g' | awk '{print $0, "off"}')

choices=$("${cmd[@]}" ${options} | sed 's/+/ /g')
python RomlistConverter.py "$choices"
elif (($menu == 3))
then
options=$(find $listfolder -maxdepth 1 -iregex '.*.txt' -printf "%f\n" | sed 's/ /+/g' | awk '{print $0, "off"}')

choices=$("${cmd[@]}" ${options} | sed 's/+/ /g')
python RomlistConverter.py "$choices"
fi
