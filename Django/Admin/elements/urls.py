from django.urls import path
from elements.views import ( 
                            
    # elements
    elements_alerts_view,
    elements_buttons_view,
    elements_cards_view,
    elements_carousel_view,
    elements_dropdown_view,
    elements_grid_view,
    elements_images_view,
    elements_modals_view,
    elements_offcanvas_view,
    elements_placeholders_view,
    elements_progressbars_view,
    elements_tabs_view,
    elements_typography_view,
    elements_video_view,
    elements_general_view,
    elements_colors_view,
    elements_utilities_view,
    
    # extended
    extended_lightbox_view,
    extended_rangeslider_view,
    extended_sweetalert_view,
    extended_rating_view,
    extended_notifications_view,
    extended_swiperslider_view,
    
)

app_name = 'elements'

urlpatterns = [  
                 
    # elements
    path('alerts_view',view=elements_alerts_view,name='alerts_view'),    
    path('buttons_view',view=elements_buttons_view,name='buttons_view'),    
    path('cards_view',view=elements_cards_view,name='cards_view'),    
    path('carousel_view',view=elements_carousel_view,name='carousel_view'),    
    path('dropdown_view',view=elements_dropdown_view,name='dropdown_view'),    
    path('grid_view',view=elements_grid_view,name='grid_view'),    
    path('images_view',view=elements_images_view,name='images_view'),    
    path('modals_view',view=elements_modals_view,name='modals_view'),    
    path('offcanvas_view',view=elements_offcanvas_view,name='offcanvas_view'),    
    path('placeholders_view',view=elements_placeholders_view,name='placeholders_view'),    
    path('progressbars_view',view=elements_progressbars_view,name='progressbars_view'),    
    path('tabs_view',view=elements_tabs_view,name='tabs_view'),    
    path('typography_view',view=elements_typography_view,name='typography_view'),    
    path('video_view',view=elements_video_view,name='video_view'),    
    path('general_view',view=elements_general_view,name='general_view'),    
    path('colors_view',view=elements_colors_view,name='colors_view'),    
    path('utilities_view',view=elements_utilities_view,name='utilities_view'),    
    
    # extended
    path('extended/lightbox_view',view=extended_lightbox_view,name='extended.lightbox_view'),    
    path('extended/rangeslider_view',view=extended_rangeslider_view,name='extended.rangeslider_view'),    
    path('extended/sweetalert_view',view=extended_sweetalert_view,name='extended.sweetalert_view'),    
    path('extended/rating_view',view=extended_rating_view,name='extended.rating_view'),    
    path('extended/notifications_view',view=extended_notifications_view,name='extended.notifications_view'),    
    path('extended/swiperslider_view',view=extended_swiperslider_view,name='extended.swiperslider_view'),    
    
]