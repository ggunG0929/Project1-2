import json
import os

import cv2
import requests
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from pyzbar.pyzbar import decode

from checkbookprice.form import PhotoForm


def barcode_reader(request):
    if request.method == 'POST':    # 1단계) 폼방식이 post일 때만
        form = PhotoForm(request.POST, request.FILES)  # 이미지를 업로드할 폼
        if form.is_valid():         # 2단계) 폼이 유효할 때(else X)
            myfile = request.FILES['image']     # 업로드된 이미지를 받아 myfile로 지정
            fs = FileSystemStorage()  # 장고의 모듈에서 제공해주는 파일 저장소
            filename = fs.save(myfile.name, myfile)     # filename: myfile를 fs에 저장한 이름
            img = cv2.imread(f'media/{filename}')   # img: filename을 cv2로 읽어냄
            detected_barcodes = decode(img)  # 인식된바코드: img를 디코드한 결과값
            if not detected_barcodes:   # 3단계) 인식된바코드가 없는 경우
                print("바코드 인식 실패.")
                return redirect('price:barcodereader')
            else:                       # 3단계) 인식된바코드가 있는 경우
                for barcode in detected_barcodes:
                    if barcode.data != "":  # 4단계) 바코드에 해당하는 data가 있을 때(else X)
                        isbn = int(barcode.data)    # 바코드data를 int형으로 isbn에 저장
                        # 알라딘api와 연결
                        key = "ttbhbh53530957001"
                        url = f"http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey={key}&itemIdType=ISBN&ItemId={isbn}&output=js&Version=20131101&OptResult=c2binfo&Cover=Big"
                        response = requests.get(url)    # 알라딘api 결과 받아오기
                        response_json = json.loads(response.text)   # 받은 response를 json 타입으로 읽어오기
                        datas = response_json['item'][0]
                        title = datas['title']
                        link = datas['link']
                        author = datas['author']
                        description = datas['description']
                        isbn13 = datas['isbn13']
                        priceSales = datas['priceSales']        # 판매가
                        priceStandard = datas['priceStandard']  # 정가
                        cover = datas['cover']
                        os.remove(f'media/{filename}')  # 파일저장소에서 filename인 파일 삭제
                        context = {'title': title, 'link': link, 'author': author, 'description': description,
                                   'isbn13': isbn13, 'price': priceSales, 'pricestandard': priceStandard,
                                   'cover': cover, }
                        return render(request, 'checkbookprice/barcodereader.html', context)
    else:       # 1단계) 폼방식이 get일 경우
        form = PhotoForm()  # 빈 폼 생성
        context = {'form': form}
        return render(request, 'checkbookprice/barcodereader.html', context)
