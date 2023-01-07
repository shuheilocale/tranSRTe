import srt

class SrtFile():

    def __init__(self, path) -> None:
        self.data = list(self.load(path))

    def load(self, path):
        with open(path, 'r') as f:
            subs = srt.parse(f.read())

        return subs

    def content(self, idx):
        if self.__len__() <= idx:
            raise IndexError

        return self.data[idx].content

    def set_content(self, idx, content):
        if self.__len__() <= idx:
            raise IndexError

        self.data[idx].content = content

    def save(self, path):
        with open(path, mode='w') as f:
            f.write(srt.compose(self.data))

    def __len__(self):
        return len(self.data)