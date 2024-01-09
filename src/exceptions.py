class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "_Файл item.csv поврежден_"