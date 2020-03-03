from django.shortcuts import render
from django.db.models import Q
from .forms import *
from app.models import PostContent
from app.forms import PostContentForm

# Create your views here.
def search(request):
    if request.method == "POST":
        search_form = SearchForm(request.POST) #テキスト入力形式フィールドを検索する用のフォーム(A)
        searchword = request.POST.get('search')
        searchword_list = searchword.split() #入力された値が複数の場合リスト形式にする
        
        #次のfor~in でQオブジェクトを代入するための変数を予め定義しておかなければエラーになる（searchword_listの０番目のみ取得）
        Q_obj_searchword_list_for_title = Q(title__icontains = searchword_list[0])
        Q_obj_searchword_list_for_text = Q(text__icontains = searchword_list[0])
        Q_obj_searchword_list_for_favorite = Q(favorite__icontains = searchword_list[0])

        for get_searchword in searchword_list[1:]:#リストの各項目であいまい検索（+OR検索）するためのQオブジェクト作成
            Q_obj_searchword_list_for_title |= Q(title__icontains = get_searchword)
            Q_obj_searchword_list_for_text |= Q(text__icontains = get_searchword)
            Q_obj_searchword_list_for_favorite |= Q(favorite__icontains = get_searchword)
        
        form = PostContentForm(request.POST)#M2Mフィールドのフォーム(B)
        m2m_search_active_area = request.POST.getlist('active_area')
        m2m_search_mypart = request.POST.getlist('mypart')
        m2m_search_recruite_part = request.POST.getlist('recruite_part')
        m2m_search_genre = request.POST.getlist('genre')

        # if A が空 and B が空:
            # フィルタリングしない（全ての記事を取得）
        if (searchword_list == [] and m2m_search_active_area == [] and m2m_search_mypart == [] 
            and m2m_search_recruite_part == [] and m2m_search_genre == []):
            postcontents = PostContent.objects.all()
        
        # if A が空 :
            # Bフォームのみでフィルター
        elif searchword_list == [] :
            postcontents = PostContent.objects.filter(Q(active_area__in = m2m_search_active_area) |Q(mypart__in = m2m_search_mypart) \
            |Q(recruite_part__in = m2m_search_recruite_part) |Q(genre__in = m2m_search_genre)).distinct()

        # elif Bが空:
            # Aのみでフィルター
        elif (m2m_search_active_area == [] and m2m_search_mypart == [] 
            and m2m_search_recruite_part == [] and m2m_search_genre == []):
            postcontents = PostContent.objects.filter(Q_obj_searchword_list_for_title \
                |Q_obj_searchword_list_for_text |Q_obj_searchword_list_for_favorite)

        # else:
            # AとBでAND検索
        else:
            postcontents = PostContent.objects.filter(Q(active_area__in = m2m_search_active_area) |Q(mypart__in = m2m_search_mypart) \
                |Q(recruite_part__in = m2m_search_recruite_part) |Q(genre__in = m2m_search_genre))\
                .filter(Q_obj_searchword_list_for_title |Q_obj_searchword_list_for_text |Q_obj_searchword_list_for_favorite).distinct()
         
        result_count = postcontents.count()
    else:
        m2m_search_active_area = request.POST.getlist('active_area') #console上でデバッグするために渡すだけ
        m2m_search_mypart = request.POST.getlist('mypart')#console上でデバッグするために渡すだけ
        m2m_search_recruite_part = request.POST.getlist('recruite_part')#console上でデバッグするために渡すだけ
        m2m_search_genre = request.POST.getlist('genre')#console上でデバッグするために渡すだけ
        searchword_list = request.POST.get('search')#console上でデバッグするために渡すだけ

        search_form = SearchForm()
        form = PostContentForm()
        postcontents = PostContent.objects.all()
        result_count = postcontents.count()
    params = {
        'search_form':search_form,
        'm2m_search_active_area':m2m_search_active_area, #javascriptでconsole.log して、データがきちんと格納されているのかテスト。
        'm2m_search_mypart':m2m_search_mypart, #javascriptでconsole.log して、データがきちんと格納されているのかテスト。
        'm2m_search_recruite_part':m2m_search_recruite_part, #javascriptでconsole.log して、データがきちんと格納されているのかテスト。
        'm2m_search_genre':m2m_search_genre, #javascriptでconsole.log して、データがきちんと格納されているのかテスト。
        'searchword_list':searchword_list, #javascriptでconsole.log して、データがきちんと格納されているのかテスト。
        'form':form,
        'postcontents':postcontents,
        'result_count':result_count,
    }
    return render(request,'search/bosyuu_article.html',params)