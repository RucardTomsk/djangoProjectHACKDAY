import eel
import main

@eel.expose
def buy(cal,t1,t2):
	return main.logicbuy(cal,t1,t2)


@eel.expose
def sell(cal,t1,t2):
	return main.logicsall(cal,t1,t2)


def StartWeb():
	eel.init("web")
	eel.start("index.html", size=(880,750))

def main2():
	StartWeb()
	pass

main2()