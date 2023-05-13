from django.shortcuts import render
from manager.models import Component 
from manager.forms import BorrowForm
from manager.models import Borrower,BorrowList
import datetime
from datetime import timedelta
def home(request,id):
    component = Component.objects.get(id=id)
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            pieces = form.cleaned_data['pieces']
            borrower_id = form.cleaned_data['borrower_id']
            # check if borrower exists and if it doesn't then create new borrower
            borrower,created = Borrower.objects.get_or_create(barcode=borrower_id)
            component.stock -= pieces 
            component.save()

            borrow_list = BorrowList(borrower_id=borrower, component_id=component, pieces=pieces, due_date=datetime.datetime.today()+timedelta(days=30),returned=False)
            borrow_list.save()



    else:
        form = BorrowForm()

    return render(request,'component.html', {
        'component': component,
        'form' : form
    })
