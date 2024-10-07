from django.shortcuts import render
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
 
class PagesView(LoginRequiredMixin,TemplateView):
    pass

# pricing
pricing_basic_view = PagesView.as_view(template_name = "pages/pricing/pricing-basic.html")
pricing_table_view = PagesView.as_view(template_name = "pages/pricing/pricing-table.html")

# invoices
invoices_list_view = PagesView.as_view(template_name = "pages/invoices/invoices-list.html")
invoices_detail_view = PagesView.as_view(template_name = "pages/invoices/invoices-detail.html")

# timeline
timeline_center_view = PagesView.as_view(template_name = "pages/timeline/timeline-center.html")
timeline_left_view = PagesView.as_view(template_name = "pages/timeline/timeline-left.html")

# authentication
    # basic 
basic_signin_view = PagesView.as_view(template_name = "pages/authentication/basic/auth-signin-basic.html")
basic_signup_view = PagesView.as_view(template_name = "pages/authentication/basic/auth-signup-basic.html")
basic_signout_view = PagesView.as_view(template_name = "pages/authentication/basic/auth-signout-basic.html")
basic_lockscreen_view = PagesView.as_view(template_name = "pages/authentication/basic/auth-lockscreen-basic.html")
basic_forgotpassword_view = PagesView.as_view(template_name = "pages/authentication/basic/auth-forgotpassword-basic.html")
basic_resetpassword_view = PagesView.as_view(template_name = "pages/authentication/basic/auth-resetpassword-basic.html")
basic_emailverification_view = PagesView.as_view(template_name = "pages/authentication/basic/auth-emailverification-basic.html")
basic_twostep_view = PagesView.as_view(template_name = "pages/authentication/basic/auth-2step-basic.html")
basic_thankyou_view = PagesView.as_view(template_name = "pages/authentication/basic/auth-thankyou-basic.html")

    # cover
cover_signin_view = PagesView.as_view(template_name = "pages/authentication/cover/auth-signin-cover.html")
cover_signup_view = PagesView.as_view(template_name = "pages/authentication/cover/auth-signup-cover.html")
cover_signout_view = PagesView.as_view(template_name = "pages/authentication/cover/auth-signout-cover.html")
cover_lockscreen_view = PagesView.as_view(template_name = "pages/authentication/cover/auth-lockscreen-cover.html")
cover_forgotpassword_view = PagesView.as_view(template_name = "pages/authentication/cover/auth-forgotpassword-cover.html")
cover_resetpassword_view = PagesView.as_view(template_name = "pages/authentication/cover/auth-resetpassword-cover.html")
cover_emailverification_view = PagesView.as_view(template_name = "pages/authentication/cover/auth-emailverification-cover.html")
cover_twostep_view = PagesView.as_view(template_name = "pages/authentication/cover/auth-2step-cover.html")
cover_thankyou_view = PagesView.as_view(template_name = "pages/authentication/cover/auth-thankyou-cover.html")


# error
    # 404
error_404basic_view = PagesView.as_view(template_name = "pages/error-pages/404/error-404-basic.html")
error_404cover_view = PagesView.as_view(template_name = "pages/error-pages/404/error-404-cover.html")

    # 500
error_500basic_view = PagesView.as_view(template_name = "pages/error-pages/500/error-500-basic.html")
error_500cover_view = PagesView.as_view(template_name = "pages/error-pages/500/error-500-cover.html")
    
# utilities
utilities_starter_view = PagesView.as_view(template_name = "pages/utilities/pages-starter.html")
utilities_profile_view = PagesView.as_view(template_name = "pages/utilities/pages-profile.html")
utilities_maintenance_view = PagesView.as_view(template_name = "pages/utilities/pages-maintenance.html")
utilities_comingsoon_view = PagesView.as_view(template_name = "pages/utilities/pages-comingsoon.html")
utilities_faqs_view = PagesView.as_view(template_name = "pages/utilities/pages-faqs.html")

utilities_layout_vertical_view = PagesView.as_view(template_name = "pages/utilities/layout-vertical.html")
