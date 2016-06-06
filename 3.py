# Create a class that represents a cuboid:
# It should take it's three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid():
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def getSurface(self):
        cuboid_surface = 2 * (self.length * self.height + self.length * self.breadth + self.breadth * self.height)
        return cuboid_surface

    def getVolume(self):
        cuboid_volume = self.length * self.breadth * self.height
        return cuboid_volume


first_cuboid = Cuboid(5, 6, 2)
print (first_cuboid.getSurface())
print (first_cuboid.getVolume())
