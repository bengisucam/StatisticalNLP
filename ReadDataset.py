from io import open
from conllu import parse_incr

class Reader:
    def __init__(self, path):
        self.data_path = path

    def readDataset(self):
        sentences = []
        data_file = open("data/" + self.data_path, "r", encoding="utf-8")
        s = ""
        for tokenlist in parse_incr(data_file):
            sentences.append(tokenlist.metadata["text"])
            s += str(tokenlist.metadata["text"] + " ")
        return sentences