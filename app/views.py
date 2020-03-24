from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import requires_csrf_token


from .models import PostContent,get_media_sound_path
from .forms import *
import hashlib
from django.utils import timezone

# Create your views here.

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
                # return redirect('app:mypage',pk=new_user.pk)
                return redirect('app:mypage')
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form':form})





def index(request):
    postcontents = PostContent.objects.all().order_by('-post_date')
    return render(request, 'app/index.html', {'postcontents':postcontents})






@login_required
def mypage(request):
    myposts = PostContent.objects.filter(author=request.user)
    return render (request, 'app/mypage.html',{'myposts':myposts})





@login_required
def createpost(request):
    if request.method == 'POST':
        form = PostContentForm(request.POST, request.FILES)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.author = request.user

            post.post_date = timezone.now()
            post.save()
            form.save_m2m()
              
            return redirect('app:bosyuu_detail',post.id)
    else:
        form = PostContentForm()
    return render (request, 'app/createpost.html',{'form':form})

def bosyuu_detail(request,postcontent_id):
    postcontent = PostContent.objects.get(id=postcontent_id)
    
    name1 = str(request.user)
    name2 = str(postcontent.author)

    name_list = [name1,name2]
    name_list_sorted = sorted(name_list)

    data={
        'postcontent':postcontent,
        'get_media_sound_path':get_media_sound_path,
        'name1':name_list_sorted[0],
        'name2':name_list_sorted[1],
    }
    return render(request, 'app/bosyuu_detail.html',data)




@require_POST
def bosyuu_delete(request,postcontent_id):
    postcontent = get_object_or_404(PostContent,id=postcontent_id)
    postcontent.delete()
    return redirect('app:index')

def editpost(request,postcontent_id):
    postcontent = get_object_or_404(PostContent,id=postcontent_id)
    if request.method == "POST":
        # form = PostContentForm(request.POST,instance=postcontent)
        form = PostContentForm(request.POST, request.FILES, instance=postcontent)
        if form.is_valid():
            form.save()
            return redirect('app:bosyuu_detail',postcontent_id=postcontent_id)
    else:
        form = PostContentForm(instance=postcontent)
    return render(request, 'app/bosyuu_edit.html',{'form':form,'postcontent':postcontent})

