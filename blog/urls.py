
from django.urls import path
from  blog import views

#use the pk regex whenever a particular post/comment is to be accessed
urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'), #home page contains list of blogs
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/(?P<pk>\d+)',views.PostDetailView.as_view(),name='post_detail'), #learn this form of pk #see details of a post
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),#create new post
    path('post/(?P<pk>\d+)/edit',views.PostUpdateView.as_view(),name='post_edit'),#post/1/edit
    path('post/(?P<pk>\d+)/remove',views.PostDeleteView.as_view(),name='post_remove'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/(?P<pk>\d+)/comment',views.add_comment_to_post,name='add_comment_to_post'),
    path('comments/(?P<pk>\d+)/approve',views.comment_approve,name='comment_approve'),
    path('comment/(?P<pk>\d+)/remove',views.comment_remove,name='comment_remove'),
    path('post/(?P<pk>\d+)/publish',views.post_publish,name='post_publish'),
]
