from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,PasswordResetView,LogoutView
from posts.views import HomeView,PostSelfListView,PostDetailCommentView,PostCreateView
from profiles.views import ProfileFollowToggle

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(),name="home"),
   	url(r'^posts/',include("posts.urls",namespace="posts")),
   	url(r'^profiles/',include("profiles.urls",namespace="profiles")),
   	url(r'^follow/',ProfileFollowToggle.as_view(),name="follow"),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    url(r'^password_reset/$',PasswordResetView.as_view(),name='password_reset'),    


 ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
