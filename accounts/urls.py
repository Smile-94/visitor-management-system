from django.urls import path
from django.contrib.auth import views as auth_views

app_name='accounts'

#views
from accounts.views import SignupVisitor
from accounts.views import SignupEmployee
from accounts.views import UserLogoutView
from accounts.views import UserLoginView

urlpatterns = [
    path('signup-visitor/', SignupVisitor.as_view(), name='signup_visitor'),
    path('signup-employee/', SignupEmployee.as_view(), name='signup_employee'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
