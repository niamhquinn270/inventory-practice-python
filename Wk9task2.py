class House:
    count = 0

    def __init__(self,address, floors, rooms, heating):
        self.address = address
        self.floors = floors
        self.rooms = rooms
        self.heating = heating

        house.count += 1

    def __str__(self):
        return f"Address:{self.address}\n" \
               f"Floors:{self.floors}\n"  \
               f"Rooms: {self.rooms}\n"  \
               f"Course:{self.heating}"

    @classmethod
    def noOfHouses(cls):
        return f"Total number of House objects created: {cls.count}"

