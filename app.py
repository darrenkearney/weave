import link_parser
from pathlib import Path
import sys
from datetime import date


class Weave:

    def __init__(self):
        # Set up working directoty and file naming defaults
        home = str(Path.home())
        self.default_wd = Path(home+'/Weave/data')
        self.file_ext = ".md"
        
        # Create today's journal node.
        today = date.today()
        name = today.strftime("%B %d, %Y")
        self.create_node( name )

    def run(self):
        

        if Path.exists(self.default_wd) and Path.is_dir(self.default_wd):
            pass
        else:
            Path.mkdir(self.default_wd)
        
        try:
            text = sys.argv[1]
        except IndexError:
            text = "Here's a string with a [[Reference Name]] in it. And here's [[Another Reference Name]]"
            print(f"Example string: {text}")

        links = link_parser.link_parser(text)
        print(f"Links: {links}")
        for link in links:
            self.create_node(link)

    def create_node(self, name):
        # create new file if no reference file found.
        # flat file structure
        filename = f"/{name}{self.file_ext}"
        filepath = str(self.default_wd)+filename
        if not Path(filepath).exists():
            with open(filepath, 'w') as writer:
                writer.write(f"{name}\n")

    def generate_filename(self):
        pass

    def get_node_data(self, filepath):
        try:
            with open(filepath, 'r') as reader:
                name = reader.readline()
                tags = reader.readline()
                data = reader.readlines()
        except FileNotFoundError:
            return False

        node = {}
        node.name = name
        node.tags = tags.split(',')
        node.data = data
        #f"<Node name:{name} tags:{tags} >"
        return node

if __name__ == "__main__":
    weave = Weave()
    weave.run()