import random
import time
import threading

order_book = [[] for _ in range(1024)]

def addOrder(order_type, ticker_symbol, quantity, price):
    ticker_index = int(ticker_symbol[6:]) - 1
    order = (order_type, quantity, price)
    order_book[ticker_index].append(order)
    print(f"Added Order: {order_type} {quantity} shares of {ticker_symbol} at ${price:.2f}")
    matchOrder(ticker_index)

def matchOrder(ticker_index):
    buy_orders = [order for order in order_book[ticker_index] if order[0] == 'Buy']
    sell_orders = [order for order in order_book[ticker_index] if order[0] == 'Sell']
    

    buy_orders.sort(key=lambda x: x[2], reverse=True)

    sell_orders.sort(key=lambda x: x[2])
    
    i, j = 0, 0
    while i < len(buy_orders) and j < len(sell_orders):
        buy_order = buy_orders[i]
        sell_order = sell_orders[j]
        
        if buy_order[2] >= sell_order[2]:
            matched_quantity = min(buy_order[1], sell_order[1])
            print(f"Matched {matched_quantity} shares of TICKER{ticker_index+1:04} at ${sell_order[2]:.2f} ")

            buy_order = (buy_order[0], buy_order[1] - matched_quantity, buy_order[2])
            sell_order = (sell_order[0], sell_order[1] - matched_quantity, sell_order[2])
            
            if buy_order[1] == 0:
                i += 1
            else:
                buy_orders[i] = buy_order
            
            if sell_order[1] == 0:
                j += 1
            else:
                sell_orders[j] = sell_order
        else:
            break
    
    order_book[ticker_index] = buy_orders[i:] + sell_orders[j:]

def simulate_transactions():
    order_types = ['Buy', 'Sell']
    ticker_symbols = [f'TICKER{i:04}' for i in range(1, 1024)]
    while True:
        order_type = random.choice(order_types)
        ticker_symbol = random.choice(ticker_symbols)
        quantity = random.randint(1, 1000)
        price = round(random.uniform(10, 1000), 2)
        addOrder(order_type, ticker_symbol, quantity, price)
        time.sleep(random.uniform(0.1, 1.0))

if __name__ == "__main__":
    threads = []
    for _ in range(100):
        thread = threading.Thread(target=simulate_transactions)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()