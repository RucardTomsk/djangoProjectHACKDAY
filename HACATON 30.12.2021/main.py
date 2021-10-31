import binanceAPI
import pars_json
import MAT


def logicbuy(col,t1,t2):
	parser = pars_json.pars_json(binanceAPI.GetAllInformatinExchange(t1,t2))
	logic = MAT.MATlog(parser.ReturnAllMasBuy(),parser.ReturnAllMarketBuy(),float(col))
	return logic.bay()

def logicsall(col,t1,t2):
	parser = pars_json.pars_json(binanceAPI.GetAllInformatinExchange(t1,t2))
	logic = MAT.MATlog(parser.ReturnAllMasSell(),parser.ReturnAllMarketSell(),float(col))
	return logic.sell()