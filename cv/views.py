from django.shortcuts import render
from .models import CV
from .forms import CVForm
from django.shortcuts import redirect

def home_page(request):
	cv = first_or_create()
	return render(request, 'home.html', {'cv' : cv})

def edit_page(request):
	cv = first_or_create()
	if cv is None:
		cv = CV.objects.create()
	if request.method == "POST":
		form = CVForm(request.POST, instance=cv)
		if form.is_valid():
			cv = form.save(commit=False)
			cv.save()
			return redirect('cv_home')
	else:
		form = CVForm(instance=cv)
	return render(request, 'edit.html', {'form' : form})

def first_or_create():
	cv = CV.objects.first()
	if cv is None:
		cv = CV.objects.create()
	return cv