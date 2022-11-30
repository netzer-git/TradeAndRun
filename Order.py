class Order:

    def __init__(self, oid, tid, otype, price, qnt, start_time, length):
        self.oid: int = oid
        self.tid: int = tid
        self.otype: str = otype
        self.price: float = price
        self.qnt: int = qnt
        self.start_time: int = start_time
        self.end_time: int = start_time + length
