from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def mypage(request,pk):
    user = get_object_or_404(User, pk=pk)
    return render (request, 'app/mypage.html',{'user': user})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #Userインスタンスを作成
        if form.is_valid():
            new_user = form.save() #Userインスタンスを保存 
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1'] 
            
            #usernameとpasswordを引数に取り、その組み合わせで認証できればユーザーオブジェクトを返す。認証出来なければNoneを返す。
            new_user = authenticate(username=input_username,password=input_password)
            #認証成功時のみ、ユーザーをログインさせる
            if new_user is not None:
                #loginメソッドは、認証が出来ていなくてもログインさせることができる。（上の authenticate で認証を実行する）
                login(request, new_user)
                return redirect('app:mypage',pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form':form})
