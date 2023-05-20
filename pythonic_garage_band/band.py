class Band:
    """
    this class is a band class it contain all type of Musician class and call for the funcion i provided to it 
    ex:
    str(band): will print a string with the str for all type of Musician class int this class
    repr(band): will print a repr with the repr for all type of Musician class int this class
    play_solos: will return the outcomes of play_solo for every member in this band
    to_list: will return all the instances of class band
    """

    instances = []


    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.instances.append(self)
        
    def __str__(self):
        band_str = "this is {} band and the member are :\n".format(self.name)
        for musician in self.members:
            band_str+=str(musician)+"\n"
        return band_str

    def __repr__(self):
        band_instance = "band instance. Name = {}\nand the member instance are :\n".format(self.name)
        for musician in self.members:
            band_instance+=repr(musician)+"\n"
        return band_instance

    def play_solos(self):
        return [musician.play_solo() for musician in self.members]

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician:
    """
    this class is a Musician class it contain name and call for the funcion i provided to it and it is the superclass for Guitarist,Bassist,Drummer
    ex:
    str(band): will print a string that contain the name of the Musician
    repr(band): will print a string that contain the name of the Musician
    """
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return "My name is {}".format(self.name)

    def __repr__(self):
        return "Name = {}".format(self.name)



class Guitarist(Musician):
    """
    this class is a Guitarist class and it is a child for Musician it contain instrument and call for the funcion i provided to it
    ex:
    str(band): will print a string that contain the name of the Musician and what instrument he/she play
    repr(band): will print a string that contain the name of the Musician and from what class he/she is made of.
    get_instrument: just return instrument
    play_solo: return a string 
    """
    def __init__(self, name):
        super().__init__(name)
        self.instrument = "guitar"

    def __str__(self):
        musician_str = super().__str__()
        return "{} and I play {}".format(musician_str,self.instrument)
    
    def __repr__(self):
        musician_repr = super().__repr__()
        return "Guitarist instance. {}".format(musician_repr)
    
    def get_instrument(self):
        return self.instrument
    
    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    """
    this class is a Bassist class and it is a child for Musician it contain instrument and call for the funcion i provided to it
    ex:
    str(band): will print a string that contain the name of the Musician and what instrument he/she play
    repr(band): will print a string that contain the name of the Musician and from what class he/she is made of.
    get_instrument: just return instrument
    play_solo: return a string 
    """
    def __init__(self, name):
        super().__init__(name)
        self.instrument = "bass"

    def __str__(self):
        musician_str = super().__str__()
        return "{} and I play {}".format(musician_str,self.instrument)
    
    def __repr__(self):
        musician_repr = super().__repr__()
        return "Bassist instance. {}".format(musician_repr)
    
    def get_instrument(self):
        return self.instrument
    
    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    """
    this class is a Drummer class and it is a child for Musician it contain instrument and call for the funcion i provided to it
    ex:
    str(band): will print a string that contain the name of the Musician and what instrument he/she play
    repr(band): will print a string that contain the name of the Musician and from what class he/she is made of.
    get_instrument: just return instrument
    play_solo: return a string 
    """

    def __init__(self, name):
        super().__init__(name)
        self.instrument = "drums"

    def __str__(self):
        musician_str = super().__str__()
        return "{} and I play {}".format(musician_str,self.instrument)
    
    def __repr__(self):
        musician_repr = super().__repr__()
        return "Drummer instance. {}".format(musician_repr)
    
    def get_instrument(self):
        return self.instrument
    
    def play_solo(self):
        return "rattle boom crash"
    
if __name__ == "__main__":
    members = [
    Guitarist("Kurt Cobain"),
    Bassist("Krist Novoselic"),
    Drummer("Dave Grohl"),
]

    some_band = Band("Nirvana", members)

    print(str(some_band))
    print(repr(some_band))
