class Human:
    species = "H. sapiens" #attribut of class shared among all instances
    #special methods or dunder methods which have double leading and trailing underscores(__init__,__str__)they are predefined we can't make them
    def __init__(self, name):
        self.name = name  #assign arg to instance attribute
        self.age = 0 #initialize property
    
    #all instance methods takes "self" as explicit first arg
    def say(self, msg):
        return (f"{self.name}: { msg}")
        
    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'
    
    #a class method shared among all instance with explicit first arg "cls"
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    #a property is just like getter to get value
    @property
    def age(self):
        return self._age
    
    # this allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # this allow the properties to be delete
    @age.deleter
    def age(self):
        del self._age



# this __name__ variable check makes sure this code block is only executed when this module is the main program
if __name__=='__main__':
    # instantiate a class
    i = Human(name="kamlesh")
    i.say('hi')
    j = Human('Joel')
    j.say('whats up!')

    # i and j are instances of human or we can say they r human objects

    print(i.say(i.get_species()))
    #we can change attribute of class by classMethod
    Human.species = 'h. neanderthalensis'
    print(i.say(i.get_species()))
    print(j.say(j.get_species()))
    

    # call the static method
    print(Human.grunt())

    # static method can be called by instances too
    print(i.grunt())

    # upsate the property for instance
    i.age = 42
    i.say(i.age)
    j.say(j.age)
    # delete
    del i.age