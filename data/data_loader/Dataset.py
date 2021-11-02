import csv
import numpy

class Dataset:

    def __init__(self, fileName):

        self.fileName = fileName

    def set_file_name(self, fileName):

        self.fileName = fileName

    def load(self):

        print("Loading {} ...".format(self.fileName))

if __name__ == "__main__":

    dataset = Dataset("something.txt")
    dataset.load()
