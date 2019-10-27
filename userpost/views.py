from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication] #BasicAuthentication
    permission_classes = [IsAuthenticated] #IsAdminUser
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # SEARCH
    filter_backends = [SearchFilter]
    search_fields = ('title','body') # 어떤 칼럼으로 지정 할 것인지


    # FILTER
    def get_queryset(self):
        # 여기 내부에서 쿼리셋을 조정한 다음
        qs = super().get_queryset() #위에꺼를 가져옴
        #qs = qs.filter(author__id = 2) 

        # 지금 만약 로그인이 안되어 있다면 -> 비어있는 queryset을 return하기
        if self.request.user.is_authenticated:
            # 지금 만약 로그인이 되어 있다면 -> 로그인한 유저의 글만 필터링 하기
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()

        return qs

    
