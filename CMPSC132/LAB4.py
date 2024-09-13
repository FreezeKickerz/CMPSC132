# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


from platform import node


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.replicate()
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> -7.5 -> 1 -> 1 -> 1 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 5 -> 5 -> 5 -> 5 -> 5 -> 8.76 -> 8.76 -> 9.78 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        elif new_node.value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            if new_node.value <= temp.next.value:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        temp.next = new_node
        self.tail = new_node



    def replicate(self):
        if self.isEmpty():
            return None
        replicated_list = SortedLinkedList()
        temp = self.head
        while temp != None:
            if type(temp.value) == float or temp.value < 0:
                replicated_list.add(temp.value)
                replicated_list.add(temp.value)
            elif temp.value == 0:
                replicated_list.add(temp.value)
            else:
                for x in range(temp.value):
                    replicated_list.add(temp.value)
            temp = temp.next
        return replicated_list




    def removeDuplicates(self):
        # --- YOUR CODE STARTS HERE
        temp = self.head
        if self.isEmpty():
            return
        else:
            while temp != None and temp.next != None:
                if temp.next.value == temp.value:
                    if temp.next == None:
                        self.tail = temp
                else:
                    temp = temp.next        
        

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(SortedLinkedList, globals(), name='Course',verbose=True)