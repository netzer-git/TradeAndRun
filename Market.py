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
