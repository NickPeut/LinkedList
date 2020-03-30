class Node:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev__ = prev
        self.__next__ = next

    def get_data(self):
        return self.__data

    def __str__(self):
        if self.__prev__ is None:
            prev = None
        else:
            prev = self.__prev__.__data
        if self.__next__ is None:
            next_ = None
        else:
            next_ = self.__next__.__data
        return "data: {}, prev: {}, next: {}".format(self.__data, prev, next_)


class LinkedList:
    def __init__(self, first=None, last=None):
        if first == None and last != None:
            raise ValueError("invalid value for last")
        elif first != None and last == None:
            self.__first__ = Node(first, None, None)
            self.__last__ = Node(None, None, None)
            self.__length = 1
        elif first != None and last != None:
            self.__first__ = Node(first, None, None)
            self.__last__ = Node(last, None, None)
            self.__first__.__next__ = self.__last__
            self.__last__.__prev__ = self.__first__
            self.__length = 2
        else:
            self.__first__ = Node(None, None, None)
            self.__last__ = Node(None, None, None)
            self.__length = 0
        pass

    def __len__(self):
        return self.__length

    def append(self, element):
        if len(self) == 0:
            self.__first__ = Node(element, None, None)
            self.__last__ = Node(None, None, None)
            self.__length = 1

        elif self.__last__.get_data() == None:
            self.__last__ = Node(element, self.__first__, None)
            self.__first__.__next__ = self.__last__
            self.__length = 2
        else:
            self.__last__.__next__ = Node(element, self.__last__, None)
            self.__last__ = self.__last__.__next__
            self.__length += 1

    def __str__(self):
        if len(self) == 0:
            return "LinkedList[]"
        else:
            ans = "LinkedList[length = {}, [".format(len(self))
            k = self.__first__
            while k.__next__ != None:
                ans = "{}{}; ".format(ans, k)
                k = k.__next__
            ans = "{}{}]]".format(ans, k)
            return ans

    def pop(self):
        if self.__length == 0:
            raise IndexError("LinkedList is empty!")
        self.__last__ = self.__last__.__prev__
        self.__last__.__next__ = None
        self.__length -= 1

    def popitem(self, element):
        if len(self) == 0:
            raise KeyError("{} doesn't exist!".format(element))
        k = self.__first__
        while k.get_data() != element and k.__next__ != None:
            k = k.__next__
        if k.get_data() == element:
            if k.__prev__ != None:
                k.__prev__.__next__ = k.__next__
            else:
                self.__first__ = k.__next__
            if k.__next__ != None:
                k.__next__.__prev__ = k.__prev__
            else:
                self.__last__ = k.__prev__
            self.__length -= 1
        else:
            raise KeyError("{} doesn't exist!".format(element))

    def clear(self):
        self.__length = 0
