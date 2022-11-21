from django.shortcuts import render
from botb.gifts import get_botb_data

def widget(request):
	botb_data = get_botb_data()
	return render(request, 'widget/widget.html', botb_data)