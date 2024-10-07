from django.urls import path
from apps.views import (
    
    calendar_view,
    chat_view,
    kanban_board_view,
    file_manager_view,
    gallery_view,
    
    # ecommerce
    ecommerce_products_view,
    ecommerce_product_detail_view,
    ecommerce_orders_view,
    ecommerce_customers_view,
    ecommerce_cart_view,
    ecommerce_checkout_view,
    ecommerce_shops_view,
    ecommerce_add_product_view,
    
    # email
    email_inbox_view,
    email_read_view,
    
    # contacts
    contacts_user_grid_view,
    contacts_user_list_view,
    contacts_settings_view,
    
    # projects
    projects_grid_view,
    projects_list_view,
    projects_overview_view,
    projects_create_new_view,
)

app_name = 'apps'

urlpatterns = [
    
    path('calendar',view=calendar_view,name="calendar"),
    path('chat',view=chat_view,name="chat"),
    path('kanban_board',view=kanban_board_view,name="kanban_board"),
    path('file_manager',view=file_manager_view,name="file_manager"),
    path('gallery',view=gallery_view,name="gallery"),
    
    # ecommerce
    path('ecommerce/products',view=ecommerce_products_view,name="ecommerce.products"),
    path('ecommerce/product_detail',view=ecommerce_product_detail_view,name="ecommerce.product_detail"),
    path('ecommerce/orders',view=ecommerce_orders_view,name="ecommerce.orders"),
    path('ecommerce/customers',view=ecommerce_customers_view,name="ecommerce.customers"),
    path('ecommerce/cart',view=ecommerce_cart_view,name="ecommerce.cart"),
    path('ecommerce/checkout',view=ecommerce_checkout_view,name="ecommerce.checkout"),
    path('ecommerce/shops',view=ecommerce_shops_view,name="ecommerce.shops"),
    path('ecommerce/add_product',view=ecommerce_add_product_view,name="ecommerce.add_product"),
    
    # email
    path('email/inbox',view=email_inbox_view,name="email.inbox"),
    path('email/read',view=email_read_view,name="email.read"),
    
    # contacts
    path('contacts/user_grid',view=contacts_user_grid_view,name="contacts.user_grid"),
    path('contacts/user_list',view=contacts_user_list_view,name="contacts.user_list"),
    path('contacts/settings',view=contacts_settings_view,name="contacts.settings"),
    
    # projects
    path('projects/projects_grid',view=projects_grid_view,name="projects.projects_grid"),
    path('projects/projects_list',view=projects_list_view,name="projects.projects_list"),
    path('projects/projects_overview',view=projects_overview_view,name="projects.projects_overview"),
    path('projects/create_new',view=projects_create_new_view,name="projects.projects_create_new"),
    
    
]
