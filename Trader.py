class Trader:
    def __init__(self, tid, ttype, start_time):
        self.tid: int = tid
        self.ttype: str = ttype
        self.balance: float = 0
        self.start_time: int = start_time
        self.n_trades: int = 0
        self.log = []
        self.orders = []

    def get_order(self):
        return None

    def respond(self):
        return None