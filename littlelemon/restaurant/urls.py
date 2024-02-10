from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name="home"),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/', views.BookingViewSet.as_view({'get': 'list'})),
    path('api-token-auth/', obtain_auth_token),
    path('login',views.login_view, name = 'login '),
]