#from django.core.urlresolvers import reverse
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,PasswordResetView,LogoutView
from posts.views import HomeView,PostSelfListView,PostDetailCommentView,PostCreateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(),name="home"),
    url(r'^posts/$',PostSelfListView.as_view(),name="my_posts"),
    url(r'^posts/create/$',PostCreateView.as_view(),name="create"),
    url(r'^posts/(?P<slug>[\w-]+)/$',PostDetailCommentView.as_view(),name="details"),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    url(r'^password_reset/$',PasswordResetView.as_view(),name='password_reset'),    


 ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
