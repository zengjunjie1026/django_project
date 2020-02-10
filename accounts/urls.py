from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [path('register/',views.registerPage,name='register'),
               path('login/',views.loginPage,name='login'),
               path('logout/',views.logoutUser,name='logout'),


               path('user/',views.user),
               path('', views.home, name="home"),
               path('about/', views.contact),
               path('admin/', views.admin),
               path('products/', views.products, name='products'),


               path('customers/<str:pk>/', views.customers, name='customers'),
               path('order_form/<str:pk>/', views.createOrder, name='create_form'),
               path('update_form/<str:pk>/', views.updateOrder, name='update_form'),
               path('delete_form/<str:pk>/', views.deleteOrder, name='delete_form'),

               path('account_setting/',views.accountSetting, name='account_setting'),

               ]

urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
