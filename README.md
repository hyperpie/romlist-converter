# romlist-converter
Converts AM romlist into a ES collection list.

## dialog.sh
Bash + dialog based frontend to select romlists for conversion.

## RomlistConverter.py
RomlistConverter can find available romlists and list them and have the user select one to convert.
It can also instead convert a list of files if the *sys.argv* contains any.

### Prerequisites
* BeautifulSoup (for parsing the *es_systems.cfg*)

### Usage
* _/bin/bash dialog.sh_ (or make file executable with *chmod +x*)
* _python RomlistConverter.py_ 

### TODO
* Testing?
