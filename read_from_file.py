class ReadFromFile:
    def read_file(self):
        all_text = []
        with open('song_list.txt','r') as file:
            # title = file.readline()[0]
            for i in file.readlines():
                all_text.append(i)



            return all_text


if __name__ == '__main__':
    obj = ReadFromFile()
    print obj.read_file()