stocks = [
    {"Ticker": "AAPL", "Current Price": 150.00, "Shares": 10, "Purchase Price": 120.00},
    {"Ticker": "GOOGL", "Current Price": 2500.00, "Shares": 5, "Purchase Price": 2000.00},
    {"Ticker": "MSFT", "Current Price": 300.00, "Shares": 20, "Purchase Price": 250.00},

]

def analyze_stock(ticker):
    for stock in stocks:
        if stock["Ticker"] == ticker:
            current_value = stock["Current Price"] * stock["Shares"]
            original_value = stock["Purchase Price"] * stock["Shares"]
            dollar_gain_loss = current_value - original_value
            percent_gain_loss = (current_value - original_value)/(original_value) * 100
            print(
            "Current Value:", current_value, 
            "Original Value:", original_value, 
            "Dollar Gain/Loss:", dollar_gain_loss, 
            "Percent Gain/Loss:", percent_gain_loss, 
            sep="\n"
            )
            break
    else: 
        print("Not in Portfolio")
        

ticker = input("Which stock would you like to look at?").upper() 
analyze_stock(ticker)

        
     


        


