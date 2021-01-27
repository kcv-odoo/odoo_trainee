from Inheritancee import Superhero
class Bat:

    species = 'Baty'

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # This class also has a say method
    def say(self, msg):
        msg = '... ... ...'
        return msg

    # And its own method as well
    def sonar(self):
        return '))) ... ((('

if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.fly)


class Batman(Superhero, Bat):
    # species = 'Batman'
    def __init__(self, *args, **kwargs):
        Superhero.__init__(self, 'anonymous', movie=True, superpowers=['Wealthy'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # override the value for the name attribute
        self.name = 'Sad Affleck'


    def sing(self):
        return 'nan nan nan nan nan batman!'


if __name__ == '__main__':
    sup = Batman()
    print(Batman.__mro__)
    print(sup.get_species())
    print(sup.sing()) 
    sup.say('I agree')
    print(sup.sonar())
    sup.age = 100
    print(sup.age)        
    print('Can I fly? ' + str(sup.fly)) 