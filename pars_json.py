import json

class pars_json():
	def __init__(self,main_dict):
		self.main_dict = main_dict
		pass

	def return_buy(self,birza):
		try:
			json_ = json.dumps(self.main_dict[0][birza][0])
			json__ = json.loads(json_)
			print(type(json__['bids']))
			return json__['bids']
		except:
			return None

	def return_sell(self,birza):
		try:
			json_ = json.dumps(self.main_dict[0][birza][0])
			json__ = json.loads(json_)
			print(type(json__['asks']))
			return json__['asks']
		except:
			return None

	def DeleteNone(self,mas):
		mas[:] = [elem for elem in mas if elem != None]
		return mas

	def ReturnAllMasBuy(self):
		return self.DeleteNone([self.return_buy(name) for name in self.main_dict[1]])

	def ReturnAllMasSell(self):
		return self.DeleteNone([self.return_sell(name) for name in self.main_dict[1]])
	
	def ReturnMarketBuy(self,birza):
		return self.main_dict[0][birza][1][0]

	def ReturnMarketSell(self,birza):
		return self.main_dict[0][birza][1][1]

	def ReturnAllMarketBuy(self):
		return [self.ReturnMarketBuy(name) for name in self.main_dict[1]]

	def ReturnAllMarketSell(self):
		return [self.ReturnMarketSell(name) for name in self.main_dict[1]]



