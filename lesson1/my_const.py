class Cat:
    # name = "Barsik"
    def __init__(self, name): # "Barsik"
        self.name = name # "Barsik"

    tail = 1
    paws = 4

    def say(self):
        print("Meow")


class Tiger(Cat):
    color = "striped"

    def say(self):
        print("Arrr")


class WhiteTiger(Tiger):
    color = "white"


gatsby = WhiteTiger("Great Gatsby")
gatsby.say()
print(gatsby.color)
#
barsik = Cat("Barsik")
barsik.say()
# print(barsik.tail)
print(barsik.name)
#
m = Cat("Murzik")
print(m.paws)
# m.say()