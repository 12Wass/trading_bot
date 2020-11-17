def calculator(typeCalc, num1, num2):
    if typeCalc == "add":
        result = num1 + num2
        print(num1, " + ", num2, " = ", result)
    elif typeCalc == "sous":
        result = num1 - num2
        print(num1, " - ", num2, " = ", result)
    elif typeCalc == "mult":
        result = num1 * num2
        print(num1, " x ", num2, " = ", result)


calculator('mult', 2, 3)

# Permets de récupérer un OHLC pour une paire donnée. url = 'https://api.kraken.com/0/public/OHLC?pair=BCHUSD'
# headers = {'content-type': 'application/json', 'API-Key':
# '/pU2wuNopR2iph7i+f6es7jGkUXH64iL8hJehSuOtXstu83aygAEOthS'} pkey =
# loeN+f5loqQJPk3gwsS6wEmoW8eb/b9s666k5Q1It3PooTaNWzVfEem6QLUQQeU6wHY/vJ2Iq45E2UjF3liOD1w==

# r = requests.get(url, headers=headers)
# r.raise_for_status()
# jsonResponse = r.json()
# print(jsonResponse["result"])
