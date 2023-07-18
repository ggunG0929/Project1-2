from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from greenbooks import views

urlpatterns = [
    path('admin/', admin.site.urls),    # 관리자 페이지
    path('', views.index, name='index'),    # 인덱스

    path('price/', include('checkbookprice.urls')),     # 바코드 가격조회
    path('community/', include('community.urls')),      # 커뮤니티
    path('custom/', include('custom.urls')),            # 고객센터
    path("goods/", include("goods.urls")),              # 구매하기
    path("gbook/mypage", views.mypage, name='mypage'),
    path('mypage/', include('mypage.urls')),
    path('shopcart/', include('shopcart.urls')),        # 장바구니
    path('tradebook/', include('tradebook.urls')),      # 직거래
    path('common/', include('common.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),  # 편집기
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
