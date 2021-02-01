from django.urls import path, reverse

import cuniculture_app.views.livestock_views as livestock_views
import cuniculture_app.views.farm_views as farm_views

# livestock_urls = [
    

# ]

farms_urls = [
    path('farms/', farm_views.manage_farms, name='manage_farm'),
    path('edit_farm/<int:farm_id>/', farm_views.edit_farm_view, name='edit_farm'),
    path('delete_farm/<int:farm_id>/', farm_views.delete_farm_view, name='delete_farm'),

]

livestock_urls = [
    path('livestock/', livestock_views.manage_livestock_view, name='manage_livestock'),
    path('edit_livestock/<int:livestock_id>/', livestock_views.edit_livestock_view, name='edit_livestock'),
    path('delete_livestock/<int:livestock_id>/', livestock_views.delete_livestock_view, name='delete_livestock'),
    path('death/', livestock_views.manage_deaths_view, name='manage_deaths'),
    path('edit_death/<int:death_id>/', livestock_views.edit_death_view, name='edit_death'),
    path('delete_death/<int:death_id>/', livestock_views.delete_death_view, name='delete_death'),
    path('manage_sales/', livestock_views.manage_sales_view, name='manage_sales'),
    path('manage_sale_items/<int:sale_id>/', livestock_views.manage_sale_items_view, name='manage_sale_items'),

]

urlpatterns = [
    path('', livestock_views.index_page_view, name='index_page'),
] + farms_urls + livestock_urls
