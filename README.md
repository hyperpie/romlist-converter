# romlist-converter
Converts AM romlist into a ES collection list.

## dialog.sh
Bash + dialog based frontend to select romlists for conversion.

## RomlistConverter.py
RomlistConverter can find available romlists and list them and have the user select one to convert.
It can also instead convert a list of files if the *sys.argv* contains any.

## template.txt
Contains some game console metadata needed to verify that roms exists in their corresponding folders.

### Prerequisites
* BeautifulSoup (for parsing the *es_systems.cfg*) - _sudo pip install bs4_
* dialog (for displaying the menu) - _sudo apt-get install dialog_

### Usage
* _/bin/bash dialog.sh_ (or make file executable with *chmod +x*)
* _python RomlistConverter.py_

### TODO
* You tell me!
