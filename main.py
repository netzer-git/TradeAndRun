# 1. init Market (with cycle num)
# 2. (in Market) init traders
# 3. (in Market) init orders
# 4. Run market for cycle num:
#   4.1 Roll random trader
#   4.2 Ask trader for order (give him all the data it needs)
#   4.3 either:
#       4.3.1 match new order with existing order (log it to traders, remove from LOB +)
#       4.3.2 Add to LOB (associate with trader +)
#   4.4 for t in traders: t.respond()
#   4.5 (future) remove expired, add new orders
# 5. close market - publish results and logs

def main():
    return

if __name__ == "__main__":
    main()
