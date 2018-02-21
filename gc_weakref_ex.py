from weakref import WeakValueDictionary

class Counter:
    _instances = WeakValueDictionary()
    @property
    def Count(self):
        return len(self._instances)

    def __init__(self, name):
        self.name = name
        self._instances[id(self)] = self
        print(name, 'created')

    def __del__(self):
        print(self.name, 'deleted')
        if self.Count == 0:
            print('Last Counter object deleted')
        else:
            print(self.Count, 'Counter objects remaining')

x1 = Counter("First")
print("Instances: {}".format(x1.Count))

x2 = Counter("Second")
print("Instances: {}".format(x2.Count))

x3 = Counter("Third")
print("Instances: {}".format(x3.Count))



