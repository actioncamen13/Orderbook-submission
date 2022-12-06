class OrderList(object):
    def __init__(self):
        self.head_order = None 
        self.tail_order = None 
        self.length = 0 
        self.volume = 0 
        self.last = None 

    def __len__(self):
        return self.length

    def __iter__(self):
        self.last = self.head_order
        return self

    def next(self):
        if self.last == None:
            raise StopIteration
        else:
            return_value = self.last
            self.last = self.last.next_order
            return return_value

    __next__ = next 

    def get_head_order(self):
        return self.head_order

    def append_order(self, order):
        if len(self) == 0:
            order.next_order = None
            order.prev_order = None
            self.head_order = order
            self.tail_order = order
        else:
            order.prev_order = self.tail_order
            order.next_order = None
            self.tail_order.next_order = order
            self.tail_order = order
        self.length +=1
        self.volume += order.quantity

    def remove_order(self, order):
        self.volume -= order.quantity
        self.length -= 1
        if len(self) == 0: 
            return

        next_order = order.next_order
        prev_order = order.prev_order
        if next_order != None and prev_order != None:
            next_order.prev_order = prev_order
            prev_order.next_order = next_order
        elif next_order != None:
            next_order.prev_order = None
            self.head_order = next_order 
        elif prev_order != None:
            prev_order.next_order = None
            self.tail_order = prev_order 

    def move_to_tail(self, order):
        if order.prev_order != None:
            order.prev_order.next_order = order.next_order 
        else: 
            self.head_order = order.next_order 

        order.next_order.prev_order = order.prev_order

        order.prev_order = self.tail_order
        order.next_order = None

        self.tail_order.next_order = order
        self.tail_order = order

    def __str__(self):
        from six.moves import cStringIO as StringIO
        temp_file = StringIO()
        for order in self:
            temp_file.write("%s\n" % str(order))
        return temp_file.getvalue()