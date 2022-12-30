from cat import *



class CatMain:
    def __init__(self):
        print("initialized")
        self.run_main()

    def run_main(self):
        meow = Cat('Meow', 24)
        ceow = Cat('ceow', 2241)
        teow = Cat('teow', 244)
        self.find_oldest_cat(meow, ceow, teow)

    def find_oldest_cat(self, meow: Cat, ceow: Cat, teow: Cat):
        maxage = max(meow.age, ceow.age, teow.age)
        self.is_oldest_cat(meow, maxage)
        self.is_oldest_cat(ceow, maxage)
        self.is_oldest_cat(teow, maxage)


    # Given the below class:
    def is_oldest_cat(self, catname: Cat, maxage):
        if catname.age == maxage:
            print(f"{catname.name} is the oldest cat")
