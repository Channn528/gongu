from django.shortcuts import render, redirect
from .models import Content, Tag
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def home(request):
     return render(request, 'home.html')
     
def share_list(request):
     share_list=Content.objects.prefetch_related('tag_set').select_related('author_profile').all()
      
     return render(request, 'share/share_list.html',{'share_list':share_list,})   
     

#확대된 보드 보여줌
def board(request, id):
     contents=Content.objects.get(pk=id)
     return render(request, 'board.html',{'contents',contents})
     
     
# 기존 보드 및 추가보드에 쓰는거   
def detail(request):
     if request.method == "POST":
          image = request.POST.get('image')
          title = request.POST.get('title')
          relay = request.POST.get('relay')
          name = request.POST.get('name')
          content = request.POST.get('content')
          contents = Content(title =title, image = image, relay=relay, content = content)
          tag = Tag(name = name)
          

# 수정 후 업데이트
def update(request, id):
     if request.method == "POST":
          contents = Content.objects.get(pk=id)
          tags= Tag.objects.get(pk=id)
          
          title = request.POST.get('title')
          image = request.POST.get('image')
          relay = request.POST.get('relay')
          name = request.POST.get('name')
          content = request.POST.get('content')
          
          Content.title = title
          Content.image = image
          Content.relay = relay
          Content.content = content
          
          Tag.name = name
          
          contents.save()
          tags.save()
          return redirect ('#', Content.pk, Tag.pk)
          
          
# 수정 
def edit(request, id):
     contents = Content.objects.get(pk=id)
     tags = Tag.objects.get(pk=id)
     return render(request, '#', {'contents', contents}, {'tags',tags})          
     
     
#삭제
def delete(request, id):
     if request.method == "POST":
          contents = Content.objects.get(pk=id)
          tags = Tag.objects.get(pk=id)
          contents.delete()
          tags.delete()

# #좋아요 숫자세기
# @login_required
# @require_POST
# def like(request):
#    if request.method == 'POST':
#         user = request.user # 로그인한 유저를 가져온다.
#         memo_id = request.POST.get('pk', None)
#         memo = Memos.objects.get(pk = memo_id)
#         if memo.likes.filter(id = user.id).exists():
#              memo.likes.remove(user)
#              message = 'You disliked this'
#         else:
#             memo.likes.add(user)
#             message = 'You liked this'

#    context = {'likes_count' : memo.total_likes, 'message' : message}
#    return HttpResponse(json.dumps(context), content_type='application/json')        