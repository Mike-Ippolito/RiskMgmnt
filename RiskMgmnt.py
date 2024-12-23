def calculate_shares_and_stops(stock_price, account_value, stop_loss_percent):
    # Keep your existing calculate_shares_and_stops function unchanged
    max_risk_per_trade = account_value * 0.01
    
    position_sizes = {
        4: 0.25,   # 25% of account for 4% stop loss
        5: 0.20,   # 20% of account for 5% stop loss
        6.5: 0.15, # 15% of account for 6.5% stop loss
        8: 0.125   # 12.5% of account for 8% stop loss
    }
    
    position_size = position_sizes[stop_loss_percent]
    position_amount = account_value * position_size
    stop_loss_price = stock_price * (1 - stop_loss_percent/100)
    number_of_shares = position_amount / stock_price
    first_target = (stock_price * 1.08-stock_price)* number_of_shares
    
    return {
        'shares': round(number_of_shares),
        'stop_price': round(stop_loss_price, 2),
        'position_value': round(number_of_shares * stock_price, 2), 
        'first_target': round(first_target, 2),
        'account_percentage': position_size * 100
    }

def display_results(stock_price, account_value):
    print("\nResults:")
    print("-" * 60)
    print(f"Account Value: ${account_value:,.2f}")
    print(f"Stock Price: ${stock_price:.2f}")
    print(f"Risk per trade: ${account_value * 0.01:,.2f}")
    print("-" * 60)
    
    for stop_loss in [4, 5, 6.5, 8]:
        result = calculate_shares_and_stops(stock_price, account_value, stop_loss)
        print(f"\nStop Loss: {stop_loss}% (Account Percentage: {result['account_percentage']}%)")
        print(f"Stop Loss Price: ${result['stop_price']}")
        print(f"Number of shares: {result['shares']}")
        print(f"Position value: ${result['position_value']:,.2f}")
        print(f"8% First target profit: ${result['first_target']}")

def main():
    account_value = 102000
    while True:
        try:
            stock_price = float(input("\nEnter stock price (or press Ctrl+C to exit): $"))
            display_results(stock_price, account_value)
        except ValueError:
            print("Please enter valid numerical values.")
        except KeyboardInterrupt:
            print("\nExiting program...")
            break

if __name__ == "__main__":
    main()
