from django.shortcuts import render

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
        typped = request.POST.get('add_task')
        valid = request.POST.get('valid_task')
        delete = request.POST.get('delete_task')

        if typped != '':
            new_entry = Item(
                name=typped,
                list_host_id=list_id,
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

    print(request.POST)
    items = Item.objects.filter(list_host_id=list_id)
    listCurrent = List.objects.filter(id=list_id).first()
    context = {
        'listCurrent': listCurrent,
        'items': items,
    }
    return render(request, 'Organiapp/detail.html', context)

