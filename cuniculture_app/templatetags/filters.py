from django import template

from cuniculture_app.models.livestocks import SalesDetails

register = template.Library()

@register.filter
def total_sale_qty_filter(sale_item_id):
    sale_item = SalesDetails.objects.get(pk=sale_item_id)

    quantity = (sale_item.male+sale_item.female)

    return quantity
