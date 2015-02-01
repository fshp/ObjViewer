import numpy

class OBJ:
    def __init__(self, filename):
        self.vertices = []
        self.faces = []
        for line in open(filename, "r"):
            if line.startswith('#'):
                continue
            values = line.split()
            if not values:
                continue
            if values[0] == 'v':
                v = list(map(float, values[1:4]))
                a, b, c = v
                self.vertices.append([a, b, c])
            elif values[0] == 'f':
                for x in values[1:4]:
                    self.faces += [int(x.split('/')[0]) - 1, ]

        # tmp = []
        # for i in self.faces:
        # tmp += self.vertices[i]

        self.vertices = numpy.array(self.vertices, dtype=numpy.float32)
        self.faces = numpy.array(self.faces, dtype=numpy.uint32)

    def getArray(self):
        return list([[self.vertices[a - 1], self.vertices[b - 1], self.vertices[c - 1]] for a, b, c in self.faces])