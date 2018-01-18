# romlist-converter
Converts AM romlist into a ES collection list.

## HPConvert.py
Originally used to take an input file (AM romlist) and convert it to a ES Collection which is output in the current working folder.
Also has methods for finding the path of a ROM based on game name, system etc.

## template.txt
Used by HPConvert to convert AM romlist, the template contains information regarding system names, their respective folder names and file extensions.

## RomlistConverter.py
Romlist Converter finds all AM romlists and displays them, and asks the user to specify one.
It then converts that file into a ES collection which is written to the correct folder.

### TODO
* Fix sys.argv parsing to allow headless mode, editing paths etc
* Clean up code?
