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
                v = tuple(map(float, values[1:4]))
                self.vertices.append(v)
            elif values[0] == 'f':
                self.faces.append(tuple(map(lambda x: int(x), values[1:4])))