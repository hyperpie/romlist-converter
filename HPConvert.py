import sys, os


# Can be used stand alone but otherwise, run RomlistConverter.py instead!
class HPConvert():

    collections_dir = "/home/pi/.emulationstation/collections"

    def __init__(self):
        self.template = self.parse_template()
        self.path = "/home/pi/RetroPie/roms/"

    def convert(self, infile, path=None, colloutput=None):
        if not path:
            path = self.path
        if not colloutput:
            colloutput = self.collections_dir
        saved = 0
        failed = 0
        with open(infile, "r") as inputfile:
            with open("outputfile.cfg", "w+") as output:
                for line in inputfile:
                    rom, console = line.split(";")
                    console = console.split("\n")[0]
                    if self.template[console]:
                        output.write(path+self.template[console]["path"]+rom+self.template[console]["extension"])
                        saved = saved + 1
                    else:
                        print("Console '"+console+"' not found, rom: "+rom)
                        failed = failed + 1
        return saved

    def set_rom_folder(self, folder):
        self.path = folder

    def get_rom_path(self, rom, console):
        console = console.split("\n")[0]
        if self.template[console]:
            rom_no_ext = self.path+self.template[console]["path"]+rom
            return self.find_rom(rom_no_ext, self.template[console]["extension"])
        # KeyError = incorrect or missing console

    def find_rom(self, path_no_ext, extensions):
        extensions = extensions.replace("\n","")
        if "%" in extensions:
            extensions = extensions.split("%").insert(0, '.zip')
        else:
            extensions = [".zip", extensions]

        for extension in extensions:
            if os.path.isfile(path_no_ext+extension):
                return path_no_ext+extension
            elif os.path.isfile(path_no_ext+extension.upper()):
                return path_no_ext+extension.upper()
        return path_no_ext+" ERROR CHECK FILE EXTENSION"


    def parse_template(self):
        templates = {}
        with open("template.txt") as templatefile:
            for line in templatefile:
                console, path, extension = line.split(";")
                templates[console] = {}
                templates[console]["path"] = path
                templates[console]["extension"] = extension
        return templates

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: 'python cfg-convert.py <input file (AM romlist)>")
    else:
        print("Converting cfg to cfg... ")
        saved, failed = HPConvert().convert(sys.argv[1])
        print(saved+" rows converted, "+failed+"rows failed! Result in 'outputfile.cfg'")
