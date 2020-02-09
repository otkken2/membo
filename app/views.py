from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import PostContent,get_media_sound_path
from .forms import PostContentForm

# Create your views here.

def index(request):
    postcontents = PostContent.objects.all()
    return render(request, 'app/index.html', {'postcontents':postcontents})






@login_required
def mypage(request):
    # user = get_object_or_404(User, pk=pk)
    return render (request, 'app/mypage.html')





@login_required
def createpost(request):
    if request.method == 'POST':
        form = PostContentForm(request.POST, request.FILES)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.author = request.user

            # post.post_date = timezone.now()
            # post.update_date = timezone.now()
            post.save()
            #追々、ここに「確認画面」へのリダイレクト処理を実装する。とりあえずは、ワンクリックで即、DBへ保存させてしまおう。  
            return redirect('app:bosyuu_detail')
    else:
        form = PostContentForm()
    return render (request, 'app/createpost.html',{'form':form})

def bosyuu_detail(request):
    postcontents = PostContent.objects.all()#本当は投稿記事のIDを指定して１記事のモデルインスタンスのみを取得する。
    data={
        'postcontents':postcontents,
        'get_media_sound_path':get_media_sound_path,
    }
    return render(request, 'app/bosyuu_detail.html',data)






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
