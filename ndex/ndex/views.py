from django.http import HttpResponse
from . import banks
from django.template import loader
from . import alphavantagewrapper as avw


def index(request):
	template = loader.get_template('ndex/index.html')
	current_prices = {}
	for k,v in banks.BANKS.items():
		current_prices[k] = avw.get_current_price(k)['Global Quote']['05. price'][0:-2]
	context = {
		'banks':banks.BANKS,
		'current_prices':current_prices
	}
	return HttpResponse(template.render(context, request))