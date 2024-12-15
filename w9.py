class lineseg:
    #TODO (以下撰寫程式)

    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    
    def sumsq(self):
        return (self.x2 - self.x1)**2 + (self.y2 - self.y1)**2

    def length(self):
        return (self.sumsq())**0.5
    
    def __mul__(self, num):
        self.x2 *= num
        self.y2 *= num
        return self

    #(以上撰寫程式)


class lineseg3(lineseg):
    #TODO (以下撰寫程式)

    def __init__(self,x1,y1,z1,x2,y2,z2):
        super().__init__(x1,y1,x2,y2)
        self.z1 = z1
        self.z2 = z2
    
    def sumsq(self):
        return super().sumsq() + (self.z2 - self.z1)**2

    def length(self):
        return (self.sumsq())**0.5

    def __mul__(self, num):
        super().__mul__(num)
        self.z2 *= num
        return self
    #(以上撰寫程式)



line = lineseg(1., 2., 4., 6.)
print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length())
line *= 2.0
print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length())

line = lineseg3(1., 2., 3., -1., -2., -3.)
print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length())
line *= 2.0
print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length())
