import string
from random import choice

from django.db import models


# photo의 이미지 파일 저장방식(이왕이면 충돌,중복,보안,관리 측면에서 해주는 것이 좋음)
def user_path(instance, filename):  # 파라미터 instance는 Photo모델을 의미, filename은 업로드 된 파일의 이름
    arr = [choice(string.ascii_letters) for _ in range(8)]  # string.ascii_letters에서 랜덤추출해서 리스트에 저장 * 8
    random_string = ''.join(arr)  # 8개 값을 가진 리스트에서 모든 값을 이어 8자리 임의의 문자 만들기
    ext = filename.split('.')[-1]       # filename의 확장자 추출
    return f'{random_string}.{ext}'     # 이미지파일의 저장명: random_string.ext


class Photo(models.Model):
    image = models.ImageField(upload_to=user_path)  # 이미지를 user_path로 업로드. 위에서 먼저 만들어줘야 함
