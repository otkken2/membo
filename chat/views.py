from chat.models import *
from app.models import *
from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
import json
import hashlib
from django.http import HttpResponseForbidden
import re

# Create your views here.
def index(request):
    #【概要】自分とやりとりしている相手の名前を一覧表示し、好きなルームへ入れるようにするぺージとする

    # ①自分のユーザーIDを含むroom_nameフィールド達をリスト形式で取得
    my_room_name_list = ChatLog.objects.filter(room_name__contains = request.user ).values_list('room_name',flat=True).distinct()
    my_room_name_list = list(my_room_name_list)
    my_room_name_list_count = len(my_room_name_list)
    
    # ②ルーム名に含まれている、自分も含めたルーム参加者の名前をリストで取得しroom_members_name変数に格納。
    room_members_name = []
    for my_room_name in my_room_name_list:
        room_members_name += list(re.split(r'_', my_room_name))

    # （③相手の名前のみを表示する作業はhtmlファイル上のtemplateタグに任せる）
    params = {
        'my_room_name_list': my_room_name_list,
        'my_room_name_list_count':my_room_name_list_count,
        'room_members_name':room_members_name,
    }
    return render(request, 'chat/index.html',params)


def room(request, name1, name2):

    ChatLog.room_name = name1 + '_' + name2
    room_name = ChatLog.room_name
    chatlogs = ChatLog.objects.filter(room_name = room_name)
    
    
    myname = str(request.user)

    data = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'chatlogs':chatlogs,
        'name1':name1,
        'name2':name2,
    }

    
    if myname == name1 or myname == name2:
        return render(request, 'chat/room.html',data)
    else:
        return HttpResponseForbidden('Access Denied',data)
