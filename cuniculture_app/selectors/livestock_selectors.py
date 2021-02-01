from cuniculture_app.models.livestocks import Livestock, Deaths, Sales, SalesDetails

def get_livestocks():
    return Livestock.objects.all()

def get_livestock(livestock_id):
    return Livestock.objects.get(pk=livestock_id)

def get_all_deaths():
    return Deaths.objects.all()

def get_death_record(death_id):
    return Deaths.objects.get(pk=death_id)

def get_livestock_deaths(livestock_id):
    return Deaths.objects.filter(livestock_id=livestock_id)

def get_farm_deaths(farm_id):
    return Deaths.objects.filter(farm_id=farm_id)

def get_sales():
    return Sales.objects.all()

def get_sale_record(sale_id):
    return Sales.objects.get(pk=sale_id)

def get_sale_items(sale_id):
    return SalesDetails.objects.filter(sale_id=sale_id)

def get_sale_item_record(sale_item_id):
    return SalesDetails.objects.get(pk=sale_item_id)
