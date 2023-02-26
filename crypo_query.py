# Program to get prices of cryptocurrencies from CoinMarketCap

import requests as request
 # type: ignore

def get_price(coin):
    # Get the price of a cryptocurrency
    key='0B5ABB70-18F2-4E84-84F8-380E5CBAF966'
    #url = 'https://api.coinmarketcap.com/v1/ticker/' + coin + '/?apikey=' + key
    url = 'https://rest.coinapi.io/v1/exchangerate/' + coin + '/USD/'
    headers = {'X-CoinAPI-Key' : key }
    #print(url)
    response = request.get(url, headers=headers)
    #print(response)
    response_json = response.json()
    #print(response_json['rate'])
    return float(response_json['rate'])

def main():
    #print("Welcome to the Cryptocurrency Price Query Program")
    # Get the price of Bitcoin and Ethereum
    coin = 'BTC'
    print('The price of {} is ${}'.format(coin, get_price(coin)))
    coin = 'ETH'
    print('The price of {} is ${}'.format(coin, get_price(coin)))

    
    
if __name__ == "__main__":
    main()

    