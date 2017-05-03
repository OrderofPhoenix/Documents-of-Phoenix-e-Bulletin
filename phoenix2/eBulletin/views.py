from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.models import User 
from .models import Bulletin,Message,Comment
#from models import UserProfile


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
# Create your views here.
def userLogin(request):
    if request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        login_user = authenticate(username=user_name, password=pass_word)
        if login_user is not None:
            login(request, login_user)
            return redirect('userindex',login_user_id=login_user.pk)
        else:
            return render(request, "login.html" )

    elif request.method == "GET":
        return render(request, "login.html", {}) 

def userindex(request,login_user_id):
    if not request.user.is_authenticated():  
        return redirect('userlogin')
    login_user=User.objects.get(pk=login_user_id)
    created_bulletins=Bulletin.objects.filter(creator=login_user)
    followed_bulletins=Bulletin.objects.filter(follower=login_user)    
    
    return render(request,'base.html',{'created_bulletins':created_bulletins,'followed_bulletins':followed_bulletins,
                    'login_user':login_user})

#message_list with comment_list
def message_list(request, login_user_id, bulletin_id):
    if not request.user.is_authenticated():  
        return redirect('userlogin')
    login_user=User.objects.get(pk=login_user_id)
    created_bulletins=Bulletin.objects.filter(creator=login_user)
    followed_bulletins=Bulletin.objects.filter(follower=login_user)
    
    bulletin=Bulletin.objects.get(pk=bulletin_id)
    messages=Message.objects.filter(bulletin=bulletin)
    message_comments=[]
    for message in messages:
        comments=Comment.objects.filter(message=message)
        message_comments.append((message.id,comments))
    message_comments=dict(message_comments)

    return render(request,'message_list.html',{'created_bulletins':created_bulletins,'followed_bulletins':followed_bulletins,
                    'login_user':login_user,'messages':messages,'bulletin':bulletin,'message_comments':message_comments})

def message_detail(request,login_user_id, message_id):
    if not request.user.is_authenticated():  
        return redirect('userlogin')
    login_user=User.objects.get(pk=login_user_id)
    created_bulletins=Bulletin.objects.filter(creator=login_user)
    followed_bulletins=Bulletin.objects.filter(follower=login_user)

    message=Message.objects.get(pk=message_id)
    return render(request,'message_detail.html',{'created_bulletins':created_bulletins,'followed_bulletins':followed_bulletins,
                    'login_user':login_user,'message':message})
