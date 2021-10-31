
class MATlog:
	def __init__(self,mas,market_price,CountToken):
		self.AllMAS = mas
		self.market_price = market_price
		self.CountToken = CountToken
		self.StartCoinTocket =CountToken

	def __return_SVB__(self,mas):
		s = sum(a[0]*a[1] for a in mas)/sum(a[1] for a in mas)
		print('SVB ' + str(s))
		return s

	def __return_SVAB__(self):
		s = sum(self.__return_SVB__(mas) for mas in self.AllMAS)/len(self.AllMAS)
		print('SVAB ' + str(s))
		return s

	def __return_RV__(self,f):
		self.market_price =sorted(self.market_price,key = lambda g: [self.__return_SVB__(mas) for mas in self.AllMAS])
		if f:
			self.market_price.reverse()
		
		self.AllMAS=sorted(self.AllMAS,key = lambda g: self.__return_SVAB__())
		if f:
			self.AllMAS.reverse()
		SUM = 0
		i=0
		for ex in self.AllMAS:
			praim_offer = None
			for offer in ex:
				if offer[0] < self.market_price[i]:
					continue
				else:
					if praim_offer == None:
						praim_offer = offer
					else:
						if offer[1] > praim_offer[1]:
							praim_offer = offer
			SUM += praim_offer[0]*praim_offer[1]
			
			self.CountToken -= praim_offer[1]
			i+=1
			if self.CountToken == 0:
				break

		return SUM



	def __return_BP__(self):
		return self.__return_SVAB__()*(self.StartCoinTocket-self.CountToken)

	def __return_D__(self,f):
		SSS = self.__return_RV__(f)
		print(SSS)
		print(self.__return_BP__())
		return [((SSS-self.__return_BP__())/SSS)*100,SSS]

	def bay(self):
		D = self.__return_D__(True)
		return str("D: " + str(D[0]) + " " + 'i: ' + str((1+D[0])*D[1]))

	def sell(self):
		D = self.__return_D__(False)
		return str("D: " + str(D[0]) + " " + 'i: ' + str((1-D[0])*D[1]))