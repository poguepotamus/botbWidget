from django.shortcuts import render

def widget(request):
	return render(request, 'widget/widget.html', {
		'items': [
			'$200',
			'Toothbrush',
			'Blob Seal',
			'Rocktopus',
			'Mouse Pad',
		],
		'people': {
			'': '',
			'matthew': '#f1beb0',
			'kayla': '#ff0000',
		}
	})