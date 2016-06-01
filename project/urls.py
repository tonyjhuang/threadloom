"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from forum import views
from rest_framework.authtoken import views as authtoken_views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'topics', views.TopicViewSet)
router.register(r'threads', views.ThreadViewSet)
router.register(r'replies', views.ReplyViewSet)
router.register(r'users', views.UserViewSet)

register_user = views.CreateUserViewSet.as_view({
    'post': 'create'
})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', register_user),
    url(r'^', include(router.urls)),
]

# Login/logout views for API.
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', authtoken_views.obtain_auth_token),
]
