class LOB:

    def __init__(self):
        self.asks = []
        self.bids = []

    def add_order(self, order):
        if order.otype == "bid":
            self.bids.append(order)
            self.bids.sort(key=lambda o: -o.price)
        if order.otype == "ask":
            self.asks.append(order)
            self.asks.sort(key=lambda o: o.price)

    def remove_from_bids(self, oid):
        pass

    def remove_from_asks(self, oid):
        pass

    def get_edge_bids(self):
        if len(self.bids) == 0:
            return []
        # [0] is the cheapest, [-1] is the most expensive
        return [self.bids[0], self.bids[-1]]

    def get_edge_asks(self):
        if len(self.asks) == 0:
            return []
        # [0] is the cheapest, [-1] is the most expensive
        return [self.asks[0], self.asks[-1]]
