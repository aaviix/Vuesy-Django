from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ElementsView(LoginRequiredMixin,TemplateView):
    pass

# elements 
elements_alerts_view = ElementsView.as_view(template_name = "elements/ui-alerts.html")
elements_buttons_view = ElementsView.as_view(template_name = "elements/ui-buttons.html")
elements_cards_view = ElementsView.as_view(template_name = "elements/ui-cards.html")
elements_carousel_view = ElementsView.as_view(template_name = "elements/ui-carousel.html")
elements_dropdown_view = ElementsView.as_view(template_name = "elements/ui-dropdown.html")
elements_grid_view = ElementsView.as_view(template_name = "elements/ui-grid.html")
elements_images_view = ElementsView.as_view(template_name = "elements/ui-images.html")
elements_modals_view = ElementsView.as_view(template_name = "elements/ui-modals.html")
elements_offcanvas_view = ElementsView.as_view(template_name = "elements/ui-offcanvas.html")
elements_placeholders_view = ElementsView.as_view(template_name = "elements/ui-placeholders.html")
elements_progressbars_view = ElementsView.as_view(template_name = "elements/ui-progressbars.html")
elements_tabs_view = ElementsView.as_view(template_name = "elements/ui-tabs.html")
elements_typography_view = ElementsView.as_view(template_name = "elements/ui-typography.html")
elements_video_view = ElementsView.as_view(template_name = "elements/ui-video.html")
elements_general_view = ElementsView.as_view(template_name = "elements/ui-general.html")
elements_colors_view = ElementsView.as_view(template_name = "elements/ui-colors.html")
elements_utilities_view = ElementsView.as_view(template_name = "elements/ui-utilities.html")

# extended
extended_lightbox_view = ElementsView.as_view(template_name = "elements/extended/extended-lightbox.html")
extended_rangeslider_view = ElementsView.as_view(template_name = "elements/extended/extended-rangeslider.html")
extended_sweetalert_view = ElementsView.as_view(template_name = "elements/extended/extended-sweet-alert.html")
extended_rating_view = ElementsView.as_view(template_name = "elements/extended/extended-rating.html")
extended_notifications_view = ElementsView.as_view(template_name = "elements/extended/extended-notifications.html")
extended_swiperslider_view = ElementsView.as_view(template_name = "elements/extended/extended-swiperslider.html")

