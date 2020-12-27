from django.shortcuts import render
from .forms import inputItem, ParagraphErrorList
import datetime

# Create your views here.
from .models import List, Item

def entryView(request):

    context={

    }
    return render(request, 'Organiapp/entry.html', context)


def indexView(request):
    if request.method == 'POST':
        typped = request.POST.get('add_task')
        delete = request.POST.get('delete_task')

        if typped != '':
            new_entry = List(
                name=typped,
            )
            new_entry.save()
        
        if delete != '' and typped == '':
            task = List.objects.filter(id=delete)
            task.delete()

    lists = List.objects.all()
    context = {
        'lists': lists,
    }
    return render(request, 'Organiapp/index.html', context)



def detailView(request, list_id):
    if request.method == 'POST':
        print(request.POST)

        typped = ''
        
        form = inputItem(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            typped = form.cleaned_data['name']
            date = form.cleaned_data['date_limit']
        valid = request.POST.get('valid_task')
        delete = request.POST.get('delete_task')

        if typped != '':
            new_entry = Item(
                name=typped,
                list_host_id=list_id,
                date_limit=date
            )
            new_entry.save()
        
        # valid and delete are the same: it delete the item in database.
        # in next version, a new database takes all the valid entry as archive

        if valid != '' and typped == '':
            task = Item.objects.filter(id=valid)
            task.delete()

        if delete != '' and typped == '':
            task = Item.objects.filter(id=delete)
            task.delete()

    items = Item.objects.filter(list_host_id=list_id).order_by('date_limit')
    listCurrent = List.objects.filter(id=list_id).first()
    form = inputItem()

    urgent_validate = []
    dateCurrent = datetime.date.today()
    for i in range(len(items)):
        if items[i].date_limit is not None:
            if items[i].date_limit < dateCurrent:
                urgent_validate.append(1)
            else:
                urgent_validate.append(0)
        else:
            urgent_validate.append(0)
    
    context = {
        'listCurrent': listCurrent,
        'items': items,
        'form': form,
        'urgent_validate': urgent_validate,
    }
    return render(request, 'Organiapp/detail.html', context)

