class Samsung:
    def __init__(self):
        print("i am samsung")

    def Screen(self):
        print("Screen")


class Iphone(Samsung):
    def __init__(self):
        print("i am iphone")
        super().__init__()

    def a3Chip(self):
        print("chip is OK")


user = Iphone()

user.a3Chip()
user.Screen()