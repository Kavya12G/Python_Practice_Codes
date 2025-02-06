from abc import ABC, abstractmethod
class Demo(ABC):
    @abstractmethod
    def sisp1(self):
        pass
    @abstractmethod
    def dips2(self):
        pass

class Demo2(Demo):
    def disp2(self):
        print('Inside disp2')
    def disp1(self):
        print('Inside disp2')
d2 = Demo2()

