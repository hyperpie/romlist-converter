import os, sys
from HPConvert import HPConvert

class RomlistConverter():

    romlist_dir = "/home/pi/.attract/romlists/"
    file_ending = ".txt"
    collections_dir = "/home/pi/.emulationstation/collections/"

    hp_converter = HPConvert()

    def run(self, amlist=None, romdir=None):
        if romdir:
            self.hp_converter.set_rom_folder(romdir)
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
            self.parse_romlist(self.romlist_dir+romlists[romlist], romlists[romlist])
        else:
            print("Headless mode currently disabled! File: "+self.romlist_dir+amlist)

    def parse_romlist(self, infile, romlist):
        collname = "custom-"+romlist.split(".txt")[0]+".cfg"
        dest = self.collections_dir+collname
        print("Writing to: "+dest)
        with open(infile, "r") as txtlist:
            with open(dest, "w+") as destination:
                for line in txtlist:
                    if line[0] != "#": # Skip comment lines
                        rom = line.split(";")[0]
                        console = line.split(";")[2]
                        destination.write(self.hp_converter.get_rom_path(rom, console)+"\n")
        print("Write finished!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        RomlistConverter().run(romdir=sys.argv[1])
    else:
        RomlistConverter().run()
