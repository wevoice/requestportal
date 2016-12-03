from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
# from _compact import JsonResponse
from django import forms
import django_excel as excel
from . import models
from . import forms as portalforms


### Transpose csv columns to rows
# import csv
# from itertools import izip
# a = izip(*csv.reader(open("input.csv", "rU")))
# csv.writer(open("output.csv", "wb")).writerows(a)


def import_sheet(request):
    if request.method == "POST":
        form = portalforms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=0,
                model=models.Client,
                mapdict=['name'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = portalforms.UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {'form': form})


def import_data(request):
    if request.method == "POST":
        form = portalforms.UploadFileForm(request.POST, request.FILES)

        def choice_func(row):
            q = models.Request.objects.filter(slug=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[models.Request, models.PDFAsset],
                initializers=[None, choice_func],
                mapdicts=[
                    ['name', 'client', 'new_account'],
                    ['name', 'ts_request', 'editable_pdf_source_available']]
            )
            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()
    else:
        form = portalforms.UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })
