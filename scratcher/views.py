from django.shortcuts import render

# Create your views here.

def pruebas(request):
	return render(
		request,
		"test.html",
		{}
	)