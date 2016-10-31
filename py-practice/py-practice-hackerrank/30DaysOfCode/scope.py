class Difference:

    def __init__(self, elements):
        self.elements = elements

    def computeDifference(self):
        self.maximumDifference = abs(max(self.elements) - min(self.elements))
