from django.shortcuts import redirect, render
from .models import PersonalData, Files
from django.views.decorators.csrf import csrf_exempt
from .forms import FileForm
import pandas as pd
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.


def ChooseTemplate(request):
    return render(request, 'index.html')


@csrf_exempt
def second(request):
    newuser = PersonalData()
    newuser.Name = request.POST['Name']
    newuser.Address = request.POST['Address']
    newuser.City = request.POST['City']
    newuser.Country = request.POST['Country']
    newuser.Zipcode = request.POST['Zipcode']
    newuser.Email = request.POST['Email']
    newuser.Phone = request.POST['Phone']
    newuser.save()
    form = FileForm()
    return render(request, 'second.html', {'form': form})


def third(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        data_list = []
        f = form.save()
        html_output = f.Html.read()
        html_files = f.Html.name
        html_files = html_files.split('/')
        body = html_output.decode()
        excel_file = request.FILES['Excel']
        Subject = request.POST['Subject']
        ExcelData = pd.read_excel(excel_file, usecols=['Email'])
        emails = ExcelData.iloc[:, 0].tolist()
        name_data = pd.read_excel(excel_file, usecols=['Name'])
        name = name_data.iloc[:, 0].tolist()
        sample_list = ['xyz']
        i = 0
        for x in name:
            new_body = render_to_string(html_files[1], {'Name': x})
            sample_list[0] = emails[i]
            msg = EmailMessage(
                Subject, new_body, '500068749@stu.upes.ac.in', sample_list)
            msg.content_subtype = "html"
            msg.send()
            i = i+1
        return render(request, 'third.html')
    else:
        form = FileForm()
    return render(request, 'second.html', {'form': form})
