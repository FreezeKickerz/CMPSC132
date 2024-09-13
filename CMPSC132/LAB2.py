# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

import random

class Fibonacci:
    """
        >>> fib_seq = Fibonacci()
        >>> fib_seq
        <Fibonacci object>, value = 0
        >>> fib_seq.next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next().next()
        <Fibonacci object>, value = 3
        >>> fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
        >>> other_fib_seq = Fibonacci()
        >>> other_fib_seq
        <Fibonacci object>, value = 0
        >>> other_fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
    """

    def __init__(self):
        self.start = 0


    def next(self):
        #--- YOUR CODE STARTS HERE
        x = Fibonacci()
        if self.start == 0:
            self.value = 1
        x.start = self.value
        x.value = self.start + self.value
        return x


    def __repr__(self):
        return f"<Fibonacci object>, value = {self.start}"


class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects
        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock()
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked()
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock()
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock()
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock()
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked()
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock()
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock()
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10'
        >>> east_machine.cancelTransaction()
        'Take your $10 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''

    def __init__(self):
        #--- YOUR CODE STARTS HERE
        self.balance = 0
        self.goods = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}




    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE
        if item not in self.goods:
            return "Invalid item"
        if not self.isStocked():
            return "Machine out of stock"
        if self.goods[item][1] == 0:
            return "Item out of stock"
        

        if self.goods[item][1] < qty:
            return "Current " + str(item) + " stock: " + str(self.goods[item][1]) + ", try again"
        
        cost = qty * self.goods[item][0]
        
        if cost == self.balance:
            self.goods[item][1] -= qty
            self.balance = 0
            return "Item dispensed"
        elif cost > self.balance:
            return "Please deposit $" + str(cost - self.balance)
        elif cost < self.balance:
            self.goods[item][1] -= qty
            temp = self.balance-cost
            self.balance = 0
            return "Item dispensed, take your $"+ str(temp)+" back"
            
        


    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        if not self.isStocked():
            self.balance = 0
            return "Machine out of stock. Take your $" + str(amount) + " back"
        else: 
            self.balance += amount
            return "Balance: $" + str(self.balance)


    def _restock(self, item, stock):
        #--- YOUR CODE STARTS HERE
        if item not in self.goods:
            return "Invalid item"
        self.goods[item][1] += stock
        return "Current item stock: " + str(self.goods[item][1])


    #--- YOUR CODE STARTS HERE
    def isStocked(self):
        for key, x in self.goods.items():
            if x[1] > 0:
                return True
        return False
        

    #--- YOUR CODE STARTS HERE
    def getStock(self):
        return print(str(self.goods))


    def cancelTransaction(self):
        #--- YOUR CODE STARTS HERE
        if self.balance > 0:
            temp = self.balance
            self.balance = 0
            return "Take your $" + str(temp) + " back"

       


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self,point):
        return self.x == point.x and self.y == point.y


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance()
        16.648
        >>> line1.getSlope()
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance()
        66.592
        >>> line2.getSlope()
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = 4*line1
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance()
        3.0
        >>> line6.getSlope()
        inf
        >>> isinstance(line6.getSlope(), float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope()
        0.0
        >>> line7
        y = 5.0
    '''
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self.point1 = point1
        self.point2 = point2

    #--- YOUR CODE STARTS HERE
    def getDistance(self):
        x_1 = self.point1.x
        y_1 = self.point1.y
        x_2 = self.point2.x
        y_2 = self.point2.y
        distance = (((x_2-x_1)**2)+((y_2-y_1)**2))**(1/2)
        distance = round(distance,3)
        return distance
       
    
    #--- YOUR CODE STARTS HERE
    def getSlope(self):
        x_1 = self.point1.x
        y_1 = self.point1.y
        x_2 = self.point2.x
        y_2 = self.point2.y
        if self.point2.x-self.point1.x == 0:
            return float("inf")
        slope = (y_2-y_1)/(x_2-x_1)
        slope = round(slope,3)
        return slope


    #--- YOUR CODE CONTINUES HERE

    def __repr__(self):
        slope = self.getSlope()
        b = self.point1.y - (slope * self.point1.x)
        b = round(b,3)
        if slope == float("inf"):
            return "Undefined"
        if slope == 0:
            return "y = " + str(b)
        return "y = " + str(slope)+"x + " + str(b)

    def __mul__(self,num):
        if isinstance(num,int):
            x_1 = self.point1.x*num
            x_2 = self.point2.x*num
            y_1 = self.point1.y*num
            y_2 = self.point2.y*num
            p1 = Point2D(x_1,y_1)    
            p2 = Point2D(x_2,y_2)
            return Line(p1,p2)
        else:
            return None
    def __rmul__(self,num):
        if isinstance(num,int):
            x_1 = self.point1.x*num
            x_2 = self.point2.x*num
            y_1 = self.point1.y*num
            y_2 = self.point2.y*num
            p1 = Point2D(x_1,y_1)    
            p2 = Point2D(x_2,y_2)
            return Line(p1,p2)
        else:
            return None
    def __eq__(self,line):
        if isinstance(line,Line):
            if self.point1==line.point1 and self.point2==line.point2:
                return True
            else:
             return False
        else:
            return False




if __name__=='__main__':
    import doctest
    #doctest.testmod()  # OR
    doctest.run_docstring_examples(Line, globals(), name='LAB2',verbose=True) # replace Fibonacci for the class name you want to test