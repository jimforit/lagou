from django.shortcuts import render
from django.views import View
from .forms import RegisterForm,LoginForm
from .models import User
from .models import Role
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from db.login_mixin import LoginRequiredMixin
# Create your views here.

class LoginView(View):
    '''用户登录'''
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.nick_name:
                return render(request, "profile.html", {"user": request.user})
            else:
                return render(request, "role.html", {"user": request.user})
        return render(request, 'login.html')

    def post(self,request):
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(username=email,password=password)
            if user is not None:
                login(request,user)
                if request.user.nick_name:
                    return render(request, 'profile.html',{"user":user})
                else:
                    return render(request, 'role.html')
            else:
                return render(request, 'login.html', {'message': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': form})


class RegisterView(View):
    '''用户注册'''
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=request.POST.get('email', ''))
            if user:
                message="邮箱已经注册"
                return render(request, 'register.html', {'message': message})
            else:
                new_user = User()
                new_user.email = form.cleaned_data["email"]
                new_user.password = make_password(form.cleaned_data["password"])
                new_user.username = new_user.email
                role = Role.objects.filter(name="user").first()
                if role is not None:
                    new_user.role_id = role
                else:
                    role = Role()
                    role.name = "user"
                    role.save()
                new_user.role_id = role.id
                new_user.save()
        else:
            msg ={}
            if "email" in form.errors.keys():
                msg={"message1":"请输入有效的电邮地址"}
            if "password" in form.errors.keys():
                msg.update({"message2":"密码不能为空"})
            print(msg)
            return render(request, 'register.html', {'register_form': msg})
        return render(request, 'login.html', {'message': "注册成功，请登录"})

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {"form": form})

class UserView(View):
    '''用户登录'''
    def get(self,request):
        return render(request, 'profile.html')

    def post(self,request):
        return render(request,'register.html')

class LagouView(View):
    '''用户登录'''
    def get(self,request):
        return render(request, 'lagou.html')

class LogoutView(View):
    '''用户登录'''
    def get(self,request):
        logout(request)
        return render(request, 'login.html')

class PofileView(LoginRequiredMixin,View):
    '''个人信息'''
    def get(self,request):
        return render(request, 'profile.html')

class RoleView(LoginRequiredMixin,View):
    '''角色选择'''

    def get(self,request):
        return render(request,"role.html")


