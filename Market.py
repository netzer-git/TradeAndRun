import random as rnd
import LOB


class Market:

    def __init__(self, length, traders, supply_n_demand):
        self.traders = traders
        self.supply_n_demand = supply_n_demand
        self.current_cycle: int = 1
        self.last_cycle = self.current_cycle + length
        self.lob = LOB.LOB()

    def cancel_expired_orders(self):
        pass

    def ask_for_order(self, tid):
        new_order = self.traders[tid].get_order()

        if not new_order:
            return

        # checks if the order is bidding and if the worst\cheapest ask is willing to pay more
        if new_order.otype == 'bid' and self.lob.get_edge_asks()[0] <= new_order.price:
            for a in self.lob.asks:
                # go through the asks and find the best ask that works for the bid
                pass
        elif new_order.otype == "ask" and self.lob.get_edge_bids()[-1] >= new_order.price:
            for b in self.lob.bids:
                pass

    def run_market(self):
        while self.current_cycle <= self.last_cycle:
            self.run_day()
            self.current_cycle += 1

    def run_day(self):
        # cancel expired orders
        self.cancel_expired_orders()
        # ask trader to order
        tid: int = rnd.randint(0, len(self.traders) - 1)
        self.ask_for_order(tid)
        # check if order, if so -> process

        # traders response
        for t in self.traders:
            t.respond()
