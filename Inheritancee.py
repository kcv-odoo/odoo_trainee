from classess import Human

class Superhero(Human):
    species = 'Superhuman'
    def __init__(self, name, movie=False,
        superpowers=["super strength", "bulletproofing"]):
        super().__init__(name)
        self.fictional = True
        self.movie = movie
        self.superpowers = superpowers
        
    
    def print_detail(self):
        return (print(f'{self.name}'))

    def sing(self):
        return 'Dun, dun, DUN!'

    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))


if __name__ == '__main__':
    sup = Superhero(name="Tick")
    sup.print_detail()

    if isinstance(sup, Human):
        print('i am human')

    if type(sup) is Superhero:
        print('I am a superhero')

    print(Superhero.__mro__)
    print(sup.get_species()) #call super class method but use its  own attribute

    # calls overridden method
    print(sup.sing())

    # Calls method from Human
    sup.say('Spoon')            # => Tick: Spoon

    # Call method that exists only in Superhero
    sup.boast()                 # => I wield the power of super strength!
                                # => I wield the power of bulletproofing!

    # Inherited class attribute
    sup.age = 31
    print(sup.age)              # => 31

    # Attribute that only exists within Superhero
    print('Am I Oscar eligible? ' + str(sup.movie))
