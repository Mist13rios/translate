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
    current = r.xpath_text('//span[@id="last_last"]')
    #//div[@class="inlineblock"]/span[@class="last_last"]')
    cells = r.xpath_list('//*[@id="results_box"]//tbody//tr//td')
    #cells = r.xpath_list('//*[@id="results_box"]//tbody//tr')
    current_cell = 0
    DayHistory.objects.all().delete()
    for i in range(0, len(cells), 6):
        #cells.xpath('.//table//th')
        DayHistory.objects.create(
            date= cells[current_cell].text_content(),
            price = cells[current_cell + 1].text_content(),
            open = cells[current_cell + 2].text_content(),
            high = cells[current_cell + 3].text_content(),
            low = cells[current_cell + 4].text_content(),
            change = cells[current_cell + 5].text_content(),
        )
        current_cell =+ 6
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
                'weekly' : data
            })

    def post(self, reuest):
        r.go(url1)
        current = r.xpath_text('//span[@id="last_last"]')
        return JsonResponse({'success': current})