from decimal import * 
import time, random

class Order(object):
    def __init__(self, quote, order_list):
        self.timestamp = int(quote['timestamp'])
        self.quantity = Decimal(quote['quantity'])
        self.price = Decimal(quote['price'])
        self.order_id = int(quote['order_id'])
        self.trade_id = quote['trade_id']
        self.next_order = None
        self.prev_order = None
        self.order_list = order_list

    def next_order(self):
        return self.next_order

    def prev_order(self):
        return self.prev_order

    def update_quantity(self, new_quantity, new_timestamp):
        if new_quantity > self.quantity and self.order_list.tail_order != self:
            self.order_list.move_to_tail(self) # move to the end
        self.order_list.volume -= (self.quantity - new_quantity) # update volume
        self.timestamp = new_timestamp
        self.quantity = new_quantity

    def __str__(self):
        return "{}@{}/{} - {}".format(self.quantity, self.price,
                                      self.trade_id, self.timestamp)