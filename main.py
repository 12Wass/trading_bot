import kraken_api as k

while 1:
    print("Welcome to KrakenBot by Silvers")
    print('1 : Save tickers to tickers.json')
    print('2 : Get your private balance')
    print('3 : Get server time')
    print('4 : Launch bot')
    print('0 : Exit bot')
    option = input("What do you want to do? ")

    if option == '1':
        k.kraken_save_tickers()
        print('Tickers saved in tickers.json')
    elif option == '2':
        print(k.kraken_get_something(k.kraken_headers, '/0/private/Balance', {}))
    elif option == '3':
        print(k.kraken_parse_result(k.kraken_get_something(k.kraken_headers, '/0/public/Time', {})))
    elif option == '4':
        k.kraken_trading_bot()
    elif option == '0':
        exit()
    else:
        print('What do you mean ? ')