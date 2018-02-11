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
* Install BS4 (sudo pip install bs4)
* add the following to es_systems.cfg

``` xml	
  <system>
    <name>Romlist Converter</name>
    <fullname>Romlist Converter</fullname>
    <path>/home/pi/RetroPie/roms/romlist-converter</path>
    <extension>.sh .SH</extension>
    <command>bash %ROM%</command>
    <platform>Romlist Converter</platform>
    <theme>romlist-converter</theme>
  </system>
```

* mkdir /home/pi/RetroPie/roms/romlist-converter
* transfer the files to the above location and chmod 777
* upload and unzip the themes to the /home/pi/.emulationstation/themes/HP2_NoMeta/ and /home/pi/.emulationstation/themes/HP2_Meta/ folders theme name needs to be romlist-converter

### TODO
* You tell me!
