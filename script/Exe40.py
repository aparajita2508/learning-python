class MyStuff:

    def __init__(self):
        self.tangerine = "Instance variable"

    def apple1(self):
        print("I am a classy instance apple")
        self.tangerine = "I am a tangerine apple"

    @staticmethod
    def apple():
        print("I am a classy class apple")

if __name__ == "__main__":
    print "Inside main method"
    my_stuff_obj = MyStuff()
    my_stuff_obj.apple1()
    MyStuff.apple()