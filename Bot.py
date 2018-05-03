import json

class Bot:

    def __init__(self, filename_in):
        self.filename = filename_in
        self.json = json.load(open(self.filename))
        print self.json
