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

if [[ ! $menu ]]
then
    exit 1
fi

if (($menu == 1))
then
    files=$(find $listfolder -maxdepth 1 -iregex $regex -printf '%f\n')
    python /home/pi/RetroPie/roms/romlist-convertor/RomlistConverter.py "$files"
    exit 1
elif (($menu == 2))
then
    options=$(find $listfolder -maxdepth 1 -iregex $regex -printf "%f\n" | sed 's/ /+/g' | awk '{print $0, "off"}' | sort)
elif (($menu == 3))
then
    options=$(find $listfolder -maxdepth 1 -iregex '.*.txt' -printf "%f\n" | sed 's/ /+/g' | awk '{print $0, "off"}' | sort)
fi

choices=$("${cmd[@]}" ${options} | sed 's/+/ /g')
clear

if [[ $choices ]]
then
    python /home/pi/RetroPie/roms/romlist-convertor/RomlistConverter.py "$choices"
else
    echo "Cancelled, or no files chosen. No conversion done."
fi
