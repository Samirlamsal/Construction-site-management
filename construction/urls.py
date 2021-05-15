from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from .forms import CustomAuthForm

urlpatterns = [
    path('', views.UltimateHomeView),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html',
                                                         authentication_form=CustomAuthForm), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('transaction_home/', views.transactionHomeView, name='transaction_home'),
    path('construction_home/', views.constructionHomeView,
         name='construction_home'),
    path('xls_download', views.export_users_xls, name='xls_download'),




]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
