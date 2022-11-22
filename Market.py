import LOB


class Market:

    def __init__(self, length, traders, supply_n_demand):
        self.traders = traders
        self.supply_n_demand = supply_n_demand
        self.current_cycle: int = 1
        self.last_cycle = self.current_cycle + length
        self.lob = LOB.LOB()

    def run_market(self):
        while self.current_cycle <= self.last_cycle:
            self.run_day()
            self.current_cycle += 1

    def run_day(self):
        # cancel expired orders

        # ask trader to order

        # check if order, if so -> process

        # traders response

        pass