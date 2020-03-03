from chat.models import *
from app.models import *
from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
import json
import hashlib
from django.http import HttpResponseForbidden

# Create your views here.
def index(request):
    return render(request, 'chat/index.html',{})

# def create_chatroom(request, name1, name2):
#     name_hash1 = hashlib.md5(name1)
#     name_hash2 = hashlib.md5(name2)
#     hashlist_beforesort = [name_hash1,name_hash2]
#     hashlist_aftersort = sorted(hashlist_beforesort)

#     return redirect('chat:room',hashlist_aftersort)



# ↓素直にユーザー名を文字列でURLにはめ込む場合のview関数です。
# ハッシュ関数をもう一度試してみて、ダメだったらこちらをコメントインする。
# def room(request, name1, name2):

#     ChatLog.room_name = name1 + '_' + name2
#     room_name = ChatLog.room_name
#     chatlogs = ChatLog.objects.filter(room_name = room_name)
    

#     data = {
#         'room_name_json': mark_safe(json.dumps(room_name)),
#         'chatlogs':chatlogs,
#         'name1':name1,
#         'name2':name2,
#     }

#     if str(request.user) == name1 or str(request.user) == name2:
#         return render(request, 'chat/room.html',data)
#     else:
#         return HttpResponseForbidden('Access Denied')



def room(request, name1, name2):

    ChatLog.room_name = name1 + '_' + name2
    room_name = ChatLog.room_name
    chatlogs = ChatLog.objects.filter(room_name = room_name)
    
    # myname = hashlib.md5(str(request.user))
    # myname = hashlib.md5(request.user)

    # myname = hashlib.md5(str(request.user).encode())
    # myname = str(myname)
    myname = str(request.user)

    data = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'chatlogs':chatlogs,
        'name1':name1,
        'name2':name2,
    }

    # if str(request.user) == name1 or str(request.user) == name2:
    if myname == name1 or myname == name2:
    # if myname == name2:
        return render(request, 'chat/room.html',data)
    else:
        return HttpResponseForbidden('Access Denied',data)
