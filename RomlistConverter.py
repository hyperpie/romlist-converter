import os, sys
from bs4 import BeautifulSoup

class RomlistConverter():

    romlist_dir = "/home/pi/.attract/romlists/"
    file_ending = ".txt"
    collections_dir = "/home/pi/.emulationstation/collections/"

    def __init__(self, es_systems_path="/etc/emulationstation/es_systems.cfg"):
        with open(es_systems_path) as systems:
            self.soup = BeautifulSoup(systems, "html5lib")

    def run_menu(self, amlist=None):
        print("HyperPie Romlist Converter v0.3 by Gubbjefvel")
        print("=================")
        if not amlist:
            print("WARNING! Any .cfg file corresponding to your choice below will be overwritten!")
            romlists = [x for x in os.listdir(self.romlist_dir) if self.file_ending in x]
            print("Available Romlists:")
            i = 0
            for l in romlists:
                print (str(i) + " : " + l)
                i = i + 1
            if (sys.version_info > (3, 0)):
                romlist = int(input("Specify romlist number: "))
            else:
                romlist = int(raw_input("Specify romlist number: "))
            self.parse_romlist(romlists[romlist])
        else:
            print("Headless mode currently disabled! File: "+self.romlist_dir+amlist)

    def parse_romlist(self, romlist):
        collname = "custom-"+romlist.split(".txt")[0]+".cfg"
        dest = self.collections_dir+collname
        print("Writing to: "+dest)
        infile = self.romlist_dir+romlist
        with open(infile, "r") as txtlist:
            with open(dest, "w+") as destination:
                for line in txtlist:
                    if line[0] != "#": # Skip comment lines
                        rom = line.split(";")[0]
                        console = line.split(";")[2]
                        path = self.get_rom_path(rom, console)
                        if "ERROR" in path:
                            with open(romlist+".error", "a+") as log:
                                log.write(path+"\n")
                        else:
                            destination.write(path+"\n")
        print("Write finished!")

    def get_rom_path(self, rom, console):
        console = console.split("\n")[0]
        systems = self.soup.find_all("system")
        for system in systems:
            if console in system.find("fullname"):
                extensions = system.find("extension").text.split(" ")
                path = system.find("path").text+"/"
                #print("ext: "+str(extensions)+"\n\tpath: "+str(path))
                for extension in extensions:
                    if os.path.isfile(path+rom+extension):
                        return path+rom+extension
        path = "./"
        return "Console: "+console+ ", path: "+path+rom+" - ERROR CHECK FILE EXTENSION"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        RomlistConverter().run_menu()
    else:
        for romlistfile in sys.argv[1:]:
            print(romlistfile)
            RomlistConverter().parse_romlist(romlistfile)
