from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from agents.views import 
from leads.views import landing_page, LandingPageView, SignupView
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView,
    LoginView, LogoutView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'), 
    # path('', landing_page, name='landing-page'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('leads/', include('leads.urls', namespace='leads')),
    path('agents/', include('agents.urls', namespace='agents')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

