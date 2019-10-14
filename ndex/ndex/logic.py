from . import banks
from . import alphavantagewrapper

BANKS = banks.BANKS

def get_current_prices():
	for k,v in BANKS.items():
