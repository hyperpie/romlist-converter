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

### Adding to HP2
* Install BS4
* add the following to es_systems.cfg
	
  <system>
    <name>Romlist Convertor</name>
    <fullname>Romlist Convertor</fullname>
    <path>/home/pi/RetroPie/roms/romlist-convertor</path>
    <extension>.sh .SH</extension>
    <command>bash %ROM%</command>
    <platform>Romlist Convertor</platform>
    <theme>romlist-convertor</theme>
  </system>

* Add the new theme to ES
* mkdir /home/pi/RetroPie/roms/romlist-convertor
* transfer the files to the above location and chmod 777

### TODO
* You tell me!
