from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from cuniculture_app.forms.livestock_forms import LivestockForm, DeathsForm, SalesForm, SalesDetailsForm
from cuniculture_app.selectors.livestock_selectors import (
    get_livestocks, get_livestock, get_all_deaths, get_death_record,
    get_livestock_deaths, get_farm_deaths, get_sales, get_sale_record,
    get_sale_items, get_sale_item_record)

def index_page_view(request):
    return render(request, "index.html")

def manage_livestock_view(request):
    
    livestocks = get_livestocks()
    livestock_form = LivestockForm()

    if request.method == "POST":
        livestock_form = LivestockForm(request.POST, request.FILES)

        if livestock_form.is_valid():
            livestock_form.save()

            messages.success(request, 'Livestock record saved successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
        
        return HttpResponseRedirect(reverse(manage_livestock_view))
    
    context = {
        'livestocks': livestocks,
        'livestock_form': livestock_form
    }

    return render (request, 'livestock/manage_livestock.html', context)

def edit_livestock_view(request, livestock_id):

    livestock = get_livestock(livestock_id)
    livestock_form = LivestockForm(instance=livestock)

    if request.method == "POST":
        livestock_form = LivestockForm(request.POST, request.FILES)

        if livestock_form.is_valid():
            livestock_form.save()
            messages.success(request, 'Changes saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
        
        return HttpResponseRedirect(reverse(manage_livestock_view))

def delete_livestock_view(request, livestock_id):
    farm = get_livestock(livestock_id)

    farm.delete()
    messages.success(request, 'Livestock Deleted Successfull')
        
    return HttpResponseRedirect(reverse(manage_livestock_view))

def manage_sales_view(request):

    return render(request, "livestock/manage_sales.html")

def manage_deaths_view(request):
    deaths = get_all_deaths()
    death_form = DeathsForm()

    if request.method == "POST":
        death_form = DeathsForm(request.POST, request.FILES)

        if death_form.is_valid():
            death_form.save()

            livestock = request.POST.get('livestock')
            gender = request.POST.get('gender')
            quantity = request.POST.get('quantity')

            update_livestock_quantity(livestock, gender, quantity)
            messages.success(request, 'Death Record saved successfully!')

        else:
            messages.warning(request, 'Operation Failed, Check your inputs and try again')
        
        return HttpResponseRedirect(reverse(manage_deaths_view))

    context = {
        "deaths": deaths,
        "death_form": death_form,

    }
    return render(request, "livestock/manage_deaths.html", context)

def update_livestock_quantity(livestock_id, gender, quantity):
    livestock = get_livestock(livestock_id)
    if gender == 'Male':
        livestock.male -= int(quantity)
    elif gender == 'Female':
        livestock.female -= int(quantity)

    livestock.available_stock -= int(quantity)
    livestock.save()

    return 0


def edit_death_view(request, death_id):
    death = get_death_record(death_id)

    death_form = DeathsForm(instance = death)

    if request.method == "POST":
        death_form = DeathsForm(request.POST, request.FILES)

        if death_form.is_valid():
            death_form.save()
            messages.success(request, 'Changes saved successfully!')

        else:
            messages.warning(request, 'Operation Failed, Check your inputs and try again')
        
        return HttpResponseRedirect(reverse(manage_deaths_view))
    
def delete_death_view(request, death_id):
    death = get_death_record(death_id)

    death.delete()
    messages.success(request, 'Death record deleted successfully!')

    return HttpResponseRedirect(reverse(manage_deaths_view))

def manage_sales_view(request):
    sale_form = SalesForm()

    sales = get_sales()

    if request.method == "POST":
        sale_form = SalesForm(request.POST, request.FILES)
        
        if sale_form.is_valid():
            sale_form.save()
            messages.success(request, 'Sale Record saved successfully!')
        else:
            messages.warning(request, 'Operation Failed, Check your inputs and try again')
        
        return HttpResponseRedirect(reverse(manage_sales_view))

    context = {
        "sales": sales,
        "sale_form": sale_form
    }

    return render(request, "livestock/manage_sales.html", context)

def manage_sale_items_view(request, sale_id):
    sale = get_sale_record(sale_id)
    sale_item_form = SalesDetailsForm(initial={"sale":sale})

    sale_items = get_sale_items(sale_id)

    if request.method == "POST":
        sale_item_form = SalesDetailsForm(request.POST, request.FILES, initial={"sale":sale})
        
        if sale_item_form.is_valid():
            sale_item_form.save()

            livestock = get_livestock(request.POST.get('livestock'))
            male = request.POST.get('male')
            female = request.POST.get('female')
            amount = request.POST.get('amount')

            update_after_sale(sale, livestock,male,female,amount)
            messages.success(request, 'Sale Item Record saved successfully!')
        else:
            messages.warning(request, 'Operation Failed, Check your inputs and try again')
        
        return HttpResponseRedirect(reverse(manage_sale_items_view, args=[sale_id]))

    context = {
        "sale_items": sale_items,
        "sale_item_form": sale_item_form,
        "sale": sale,
    }
    
    return render(request, "livestock/manage_sales_details.html", context)

def update_after_sale(sale, livestock, male, female, amount):
    sale.total_quantity += (int(male)+int(female))
    sale.total_amount += int(amount)
    sale.save()

    livestock.female -= int(female)
    livestock.male -= int(male)
    livestock.available_stock -= (int(male)+int(female))
    livestock.save()
