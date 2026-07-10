def main():
    ticker = input("Select Stock").upper()
    stock = find_stock(ticker)
    
    if stock is None: 
        print(f"Error: {ticker} not found in portfolio")
    else:
        value = (value_stock(stock))
        profit = (profit_stock(stock))
        gain = (percent_gain(stock))

        print("-" * 20,)
        print(f"Stock: {ticker}", end="\n")
        print(f"Current value: {value:.2f}")
        print(f"Profit: {profit:.2f}")  
        print(f"Percent Gain: {gain:.2f}% ")        
        print("-" * 20)

def find_stock(ticker):
    for stock in stocks:
        if ticker == stock["Ticker"]:
            return stock
    return None

def value_stock(stock):
    current_value = stock["Price"] * stock["Shares"]
    return current_value
           
def profit_stock(stock):
    profit = (stock["Price"] * stock["Shares"]) - (stock["Original Price"] * stock["Shares"])  
    return profit


def percent_gain(stock):
    percent_gain =  profit_stock(stock) / (stock["Original Price"] * stock["Shares"]) * 100 
    return percent_gain  
        

stocks = [
    {"Ticker": "AAPL", "Price": 150, "Original Price": 112, "Shares": 3,},
    {"Ticker": "MSFT", "Price": 200, "Original Price": 145, "Shares": 7,},
    {"Ticker": "TSLA", "Price": 443, "Original Price": 565, "Shares": 14,},
    {"Ticker": "NVDA", "Price": 1009, "Original Price": 1245, "Shares": 5,},
    {"Ticker": "GOOGL", "Price": 341, "Original Price": 109, "Shares": 10,}
]

main()
