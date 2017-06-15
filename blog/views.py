# _*_ encoding:utf-8 _*_
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from blog import models
from django.shortcuts import render


def loading(request, pid=None):
    template = get_template('loading.html')

    html = template.render(Context(locals()))
    return HttpResponse(html)


def index(request, pid=None):
    template = get_template('fashare.html')
    
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:3]
    try:
        user_id = request.GET['user_id']
        user_email = request.GET['user_email']
        post_title = request.GET['post_title']
        user_post = request.GET['user_post']
       
    except:
        user_id = None
        message = 'NOTICE：每一個欄位皆為必填'
    if user_id != None:
        post = models.Post.objects.create(nickname=user_id, email=user_email, title=post_title, message=user_post)
        post.save()
        message='留言成功！我們已收到您的訊息！'

    html = template.render(Context(locals()))

    return HttpResponse(html)

def english(request, pid=None):
    template = get_template('fashare_e.html')
    
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:3]
    try:
        user_id_e = request.GET['user_id_e']
        user_email_e = request.GET['user_email_e']
        post_title_e = request.GET['post_title_e']
        user_post_e = request.GET['user_post_e']
       
    except:
        user_id_e = None
        message = 'NOTICE：Every fields are required.'
    if user_id_e != None:
        post = models.Post.objects.create(nickname=user_id_e, email=user_email_e, title=post_title_e, message=user_post_e)
        post.save()
        message='Leave messages successfully! We have got your messages.'

    html = template.render(Context(locals()))

    return HttpResponse(html)
