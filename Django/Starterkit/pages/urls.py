from django.urls import path
from pages.views import (
    
    # pricing
    pricing_basic_view,
    pricing_table_view,
    
    # invoices
    invoices_list_view,
    invoices_detail_view,
    
    # timeline
    timeline_center_view,
    timeline_left_view,
    
    # authentication
        # basic
    basic_signin_view,
    basic_signup_view,
    basic_signout_view,
    basic_lockscreen_view,
    basic_forgotpassword_view,
    basic_resetpassword_view,
    basic_emailverification_view,
    basic_twostep_view,
    basic_thankyou_view,
    
        # cover
    cover_signin_view,
    cover_signup_view,
    cover_signout_view,
    cover_lockscreen_view,
    cover_forgotpassword_view,
    cover_resetpassword_view,
    cover_emailverification_view,
    cover_twostep_view,
    cover_thankyou_view,
    
    # error
        # 404
    error_404basic_view,
    error_404cover_view,
    
        # 500
    error_500basic_view,
    error_500cover_view,

    # utilities
    utilities_starter_view,
    utilities_profile_view,
    utilities_maintenance_view,
    utilities_comingsoon_view,
    utilities_faqs_view,
    
    utilities_layout_vertical_view,
)

app_name = 'pages'

urlpatterns = [
    
    path('pricing/pricing_basic',view=pricing_basic_view,name='pricing.pricing_basic'),
    path('pricing/pricing_table',view=pricing_table_view,name='pricing.pricing_table'),
    
    # invoices
    path('invoices/invoices_list',view=invoices_list_view,name='invoices.invoices_list'),
    path('invoices/invoices_detail',view=invoices_detail_view,name='invoices.invoices_detail'),
    
    # timeline
    path('timeline/center_view',view=timeline_center_view,name='timeline.center_view'),
    path('timeline/left_view',view=timeline_left_view,name='timeline.left_view'),
    
    # authentication
        # basic
    path('authentication/basic/signin',view=basic_signin_view,name='authentication.basic.signin'),
    path('authentication/basic/signup',view=basic_signup_view,name='authentication.basic.signup'),
    path('authentication/basic/signout',view=basic_signout_view,name='authentication.basic.signout'),
    path('authentication/basic/lockscreen',view=basic_lockscreen_view,name='authentication.basic.lockscreen'),
    path('authentication/basic/forgotpassword',view=basic_forgotpassword_view,name='authentication.basic.forgotpassword'),
    path('authentication/basic/resetpassword',view=basic_resetpassword_view,name='authentication.basic.resetpassword'),
    path('authentication/basic/emailverification',view=basic_emailverification_view,name='authentication.basic.emailverification'),
    path('authentication/basic/twostep',view=basic_twostep_view,name='authentication.basic.twostep'),
    path('authentication/basic/thankyou',view=basic_thankyou_view,name='authentication.basic.thankyou'),
        
        # cover
    path('authentication/cover/signin',view=cover_signin_view,name='authentication.cover.signin'),
    path('authentication/cover/signup',view=cover_signup_view,name='authentication.cover.signup'),
    path('authentication/cover/signout',view=cover_signout_view,name='authentication.cover.signout'),
    path('authentication/cover/lockscreen',view=cover_lockscreen_view,name='authentication.cover.lockscreen'),
    path('authentication/cover/forgotpassword',view=cover_forgotpassword_view,name='authentication.cover.forgotpassword'),
    path('authentication/cover/resetpassword',view=cover_resetpassword_view,name='authentication.cover.resetpassword'),
    path('authentication/cover/emailverification',view=cover_emailverification_view,name='authentication.cover.emailverification'),
    path('authentication/cover/twostep',view=cover_twostep_view,name='authentication.cover.twostep'),
    path('authentication/cover/thankyou',view=cover_thankyou_view,name='authentication.cover.thankyou'),
    
    # error
        # 404
    path('error-pages/404/basic',view=error_404basic_view,name='error-pages.404.basic'),
    path('error-pages/404/cover',view=error_404cover_view,name='error-pages.404.cover'),
    
        # 500
    path('error-pages/500/basic',view=error_500basic_view,name='error-pages.500.basic'),
    path('error-pages/500/cover',view=error_500cover_view,name='error-pages.500.cover'),

    # utilities
    path('utilities/starter',view=utilities_starter_view,name='utilities.starter'),
    path('utilities/profile',view=utilities_profile_view,name='utilities.profile'),
    path('utilities/maintenance',view=utilities_maintenance_view,name='utilities.maintenance'),
    path('utilities/comingsoon',view=utilities_comingsoon_view,name='utilities.comingsoon'),
    path('utilities/faqs',view=utilities_faqs_view,name='utilities.faqs'),
    
    path('utilities/layout_vertical',view=utilities_layout_vertical_view,name='utilities.layout_vertical'),
        
        
]