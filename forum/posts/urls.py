from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from posts.views import PostSelfListView,PostDetailCommentView,PostCreateView


urlpatterns = [
    url(r'^$',PostSelfListView.as_view(),name="my_posts"),
    url(r'^create/$',PostCreateView.as_view(),name="create"),
    url(r'^(?P<slug>[\w-]+)/$',PostDetailCommentView.as_view(),name="details"),
    
 ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
