from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import welcome, LoginInterfaceView, SignupView

urlpatterns = [
    path('', welcome, name='welcome'),
    path('login/', LoginInterfaceView.as_view(), name='login'),

    # ✅ LOGOUT
    path(
        'logout/',
        LogoutView.as_view(template_name='home/logout.html'),
        name='logout'
    ),

    # ✅ SIGNUP
    path('signup/', SignupView.as_view(), name='signup'),
]
