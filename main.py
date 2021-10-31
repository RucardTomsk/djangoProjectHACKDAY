import binanceAPI
import pars_json
import MAT

parser = pars_json.pars_json(binanceAPI.GetAllInformatinExchange())
logic = MAT.MATlog(parser.ReturnAllMasBuy(),parser.ReturnAllMarketBuy(),10000)
print(logic.a())