import ccxt
import requests
import time

#mas_tocken = ['ZRX/USDT','BAT/USDT','SUSHI/USDT','DYDX/USDT','1INCH/USDT']
def GetAllInformatinExchange(t1,t2):
	mas_name_birzi = ['binance','ftx','gateio','kraken','huobi']
	mas_r_b = []
	#count_my_token = input()
	txt_tocken = t1
	text_USDT = t2
	mas_birzi = {'binance':ccxt.binance(), 'ftx': ccxt.ftx(), 'gateio':ccxt.gateio(), 'kraken': ccxt.kraken(), 'huobi':ccxt.huobi()}

	mas_json = []
	for name_birzhe in mas_name_birzi:
		start_time = time.time()
		try:
			mas = []
			mas.append(name_birzhe)
			orderbook = mas_birzi[name_birzhe].fetch_l2_order_book(txt_tocken+'/'+text_USDT)
			mas.append(orderbook)
			bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
			ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
			mas.append([bid,ask])
			mas_json.append(mas)
			mas_r_b.append(name_birzhe)
			print("--- %s seconds ---" % (time.time() - start_time))
		except:
			continue
	#print(mas_json)
	mas = []
	try:
		mas.append('dydx')

		orderbook = requests.get('https://api.dydx.exchange/v3/orderbook/'+txt_tocken+'-'+text_USDT)
		mas.append(orderbook)
		bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
		ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
		mas.append([bid,ask])
		mas_json.append(mas)
		mas_r_b.append('dydx')
	except:
		pass
	
	dict_fsom = {a[0]: [a[1],a[2]] for a in mas_json}
	return [dict_fsom,mas_r_b]
#print(mas_birzi['binance'])
#f = open('text2.json', 'w')

#r = json.dumps(mas_birzi['binance'].fetch_l2_order_book(txt_tocken))
#r = json.dumps(ccxt.exchanges)
#print(r)
#f.write(r)

#ZRX BAT USDT SUSHI DYDX 1INCH
#bids - Покупка
#asks - Продажа