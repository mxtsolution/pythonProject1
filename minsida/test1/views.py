from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import NameForm, Update, UpdateForm, SigneraForm, Signera
from .models import Namnlista
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView



def hem(request) :

    return render (request, 'test.html')

def bla(request) :

    return render (request, 'bla.html')

def planera(request) :
    context = Namnlista.objects.all()

    return render (request, 'planera.html', {'context' : context})

def skapa(request) :
    last = Namnlista.objects.last()
    last_ao = int(last.ao)
    ny_ao = int(last_ao) + 1
    form = NameForm(initial={'ao': ny_ao})
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid() :
            namn = Namnlista(
                ao=form.cleaned_data["ao"],
                direktiv =form.cleaned_data["direktiv"],
                objektid=form.cleaned_data["objektid"],
                avd=form.cleaned_data["avd"],
                las_lista=form.cleaned_data["las_lista"],
            )
            namn.save()
        return redirect('show')
    return render (request, 'skapa.html', {'form': form})


def uppdatera(request, item_id):
    bla = Namnlista.objects.get(pk=item_id)
    request.session['sista'] = bla.ao
    avstallt_varde = bla.avstallt
    operator_varde = bla.operator
    laslista = bla.las_lista
    formular = UpdateForm(initial={'avstallt': avstallt_varde,'operator': operator_varde,'las_lista': laslista})
    context = Namnlista.objects.filter(id=item_id).distinct()
    if request.method == 'POST':
        form = Update(request.POST, instance=bla)
        if form.is_valid() :
            form.save()
        return redirect('show')
    return render(request, 'uppdatera.html', {'form' : formular, 'context' : context})

def signering(request, item_id, stats):

    bla = Namnlista.objects.get(pk=item_id)
    request.session['sista'] = bla.ao
    utforare = bla.utforare
    status = stats
    formular = SigneraForm(initial={'utforare': utforare,'status': status})
    context = Namnlista.objects.filter(id=item_id).distinct()
    if request.method == 'POST':
        form = Signera(request.POST,instance=bla)
        if form.is_valid() :
            form.save()
        return redirect('show')
    return render(request, 'signera.html', {'form' : formular, 'context' : context, 'stat':status})

def show(request):
    query = request.GET.get('sok')

    if query is not None :
        context = Namnlista.objects.filter(ao=query).distinct()

    form = NameForm()
    if not query :
        blabla = request.session['sista']
        context = context = Namnlista.objects.filter(ao=blabla).distinct()


    return render (request, 'test.html', {'form': form, 'context': context})

def remove(request, item_id) :
    item = Namnlista.objects.get(id=item_id)
    item.delete()
    previous_page = request.META['HTTP_REFERER']
    return redirect(previous_page)



