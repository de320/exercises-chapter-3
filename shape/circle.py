

class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def __contains__(self, point):
        xcoord = self.centre[0]
        ycoord = self.centre[1]
        pointx = point[0]
        pointy = point[1]
        if (pointx - xcoord)**2 + (pointy - ycoord)**2 < self.radius**2:
            return True
        else:
            return False
