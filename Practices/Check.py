# a = 10
# def Check():
#     global a
#     a+=10
#     print(a)
# Check()

# class M:
#     l = 9
# o = M()
# o1 = M()
# o.__class__.l = 10
# print(o.l)
# print(o1.l)

class M:
    def __init__(self,a):
        # print(self)
        self.a = a
    def ak(self):
        print(self.a)
    # @classmethod
    # def ak(self):
    #     print('this',self.a)
o = M('airy')
o1 = M('y')
o.ak()
o1.ak()