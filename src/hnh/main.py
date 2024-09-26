from fastapi import FastAPI, File, UploadFile
import os
import random
from transformers import pipeline
import io
from fastapi import Request
from fastapi.templating import Jinja2Templates
from hnh.util import get_max_label, get_score, get_max_label2

app = FastAPI()

html = Jinja2Templates(directory="public")

@app.get("/hello")
def read_root():
    return {"Hello": "hotdog"} 

def predict():
    dog_list = ["hotdog","not hotdog"]

    return dog_list[random.randint(0,1)]

@app.get("/predict")
def hotdog():
    dog = predict()
    return dog

@app.get("/")
async def home(request: Request):
    hotdog = "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQweb_7o7OrtlTP75oX2Q_keaoVYgAhMsYVp1sCafoNEdtSSaHps3n7NtNZwT_ufZGPyH7_9MFcao_r8QWr3Fdz17RitvZXLTU4dNsxr73m6V1scsH3_ZZHRw&usqp=CAE"
    dog = "https://hearingsense.com.au/wp-content/uploads/2022/01/8-Fun-Facts-About-Your-Dog-s-Ears-1024x512.webp"
    image_url = random.choice([hotdog, dog])
    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # 파일 저장
    img = await file.read()
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")

    from PIL import Image
    img = Image.open(io.BytesIO(img)) # 이미지를 바이트로 PIL 이미지로 변환
    p = model(img)
    

    if get_max_label2(p) >= 0.8:
        label = "hot dog"
    else:
        label = "not hot dog"

    #label = get_max_label(p)
    #label = get_max_label2(p)
    
    

    # 의존성 모듈 설치해서 오류 없이 서버 가동
    # if p 값이 배열과 같이 나오면 높은 확률의 값을 추출해서 리턴하기

    return {"label": label, "Hello": p}


