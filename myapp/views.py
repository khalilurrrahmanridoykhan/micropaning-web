from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Form, UserFormSubmission

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def map_view(request):
    return render(request, 'map.html')



def form_list(request):
    forms = Form.objects.all()
    return render(request, 'form_list.html', {'forms': forms})

def form_detail(request, form_id):
    form = get_object_or_404(Form, pk=form_id)
    if request.method == 'POST':
        data = {field.label: request.POST.get(field.label) for field in form.field_set.all()}
        UserFormSubmission.objects.create(form=form, data=data)
        return redirect('form_list')
    return render(request, 'form_detail.html', {'form': form})

def submission_list(request, form_id):
    form = get_object_or_404(Form, pk=form_id)
    submissions = UserFormSubmission.objects.filter(form=form)
    return render(request, 'submission_list.html', {'form': form, 'submissions': submissions})
