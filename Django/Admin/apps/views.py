from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AppsView(LoginRequiredMixin,TemplateView):
    pass

calendar_view = AppsView.as_view(template_name ="apps/apps-calendar.html") 
chat_view = AppsView.as_view(template_name ="apps/apps-chat.html") 
kanban_board_view = AppsView.as_view(template_name ="apps/apps-kanban-board.html") 
file_manager_view = AppsView.as_view(template_name ="apps/apps-file-manager.html") 
gallery_view = AppsView.as_view(template_name ="apps/apps-gallery.html") 

# ecommerce
ecommerce_products_view = AppsView.as_view(template_name ="apps/ecommerce/ecommerce-products.html") 
ecommerce_product_detail_view = AppsView.as_view(template_name ="apps/ecommerce/ecommerce-product-detail.html") 
ecommerce_orders_view = AppsView.as_view(template_name ="apps/ecommerce/ecommerce-orders.html") 
ecommerce_customers_view = AppsView.as_view(template_name ="apps/ecommerce/ecommerce-customers.html") 
ecommerce_cart_view = AppsView.as_view(template_name ="apps/ecommerce/ecommerce-cart.html") 
ecommerce_checkout_view = AppsView.as_view(template_name ="apps/ecommerce/ecommerce-checkout.html") 
ecommerce_shops_view = AppsView.as_view(template_name ="apps/ecommerce/ecommerce-shops.html") 
ecommerce_add_product_view = AppsView.as_view(template_name ="apps/ecommerce/ecommerce-add-product.html") 

# email
email_inbox_view = AppsView.as_view(template_name ="apps/email/email-inbox.html") 
email_read_view = AppsView.as_view(template_name ="apps/email/email-read.html") 

# contacts
contacts_user_grid_view = AppsView.as_view(template_name ="apps/contacts/contacts-grid.html") 
contacts_user_list_view = AppsView.as_view(template_name ="apps/contacts/contacts-list.html") 
contacts_settings_view = AppsView.as_view(template_name ="apps/contacts/contacts-settings.html") 

# projects
projects_grid_view = AppsView.as_view(template_name ="apps/projects/projects-grid.html") 
projects_list_view = AppsView.as_view(template_name ="apps/projects/projects-list.html") 
projects_overview_view = AppsView.as_view(template_name ="apps/projects/projects-overview.html") 
projects_create_new_view = AppsView.as_view(template_name ="apps/projects/projects-create.html") 
