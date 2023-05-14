class Band:
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
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return "My name is {}".format(self.name)

    def __repr__(self):
        return "Name = {}".format(self.name)



class Guitarist(Musician):

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
