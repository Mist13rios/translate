from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
import lxml.html as html
import re
from grab import Grab
from parse.forms import DayHistoryForm
from parse.models import DayHistory
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

url1='https://www.investing.com/currencies/btc-usd-historical-data'
r = Grab()

def parse(url1):
    r.go(url1)
    current = r.xpath('//span[@id="last_last"]').text_content()
    #//div[@class="inlineblock"]/span[@class="last_last"]')
    cells = r.xpath_list('//*[@id="results_box"]//tbody//tr//td')
    #cells = r.xpath_list('//*[@id="results_box"]//tbody//tr')
    array = []
    current_cell = 1
    error = []
    for i in range(0, len(cells), 6):
        #cells.xpath('.//table//th')
        form = DayHistoryForm()
        form.data['date'] = cells[current_cell].text_content()
        form.data['price'] = cells[current_cell+1].text_content()
        form.data['open'] = cells[current_cell+1].text_content()
        form.data['high'] = cells[current_cell+1].text_content()
        form.data['low'] = cells[current_cell+1].text_content()
        form.data['change'] = cells[current_cell+1].text_content()
        if form.is_valid():
            form.save()
        else:
            error += form.errors.keys()
    if error != []:
        return {'error': error}
    else:
        return {'success': current}


@method_decorator(csrf_exempt, name='dispatch')
class main(View):

    def get(self, request):
        template = 'tables.html'
        current = parse(url1)
        data = DayHistory.objects.all()
        return render(request, template, {
                'data': data ,
                'current': current,
            })

    def post(self, reuest):
        return parse(url1)