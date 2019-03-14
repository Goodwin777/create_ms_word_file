import os

class ReadFromFile:
    def read_file(self):
        with open('song_list.txt','r') as file:
            line = file.readline()

            return line
