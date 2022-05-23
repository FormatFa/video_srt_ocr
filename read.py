# 读取视频，识别字幕
import cv2
import numpy as np
from cnocr import CnOcr
from skimage.metrics import structural_similarity as ssim
import json
import os

ocr = CnOcr()


def process(videopath):

    cap = cv2.VideoCapture(videopath)
    frames_num = cap.get(7)
    print("process:{},framecount={}".format(videopath,frames_num))

    success, image = cap.read()
    if np.shape(image) == ():
            return
    img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    last = img
    count=0
    result = []
    while success:
        success, image = cap.read()
        count+=1
        # 空的
        if np.shape(image) == ():
            continue
        
        img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # 查看图片相似度
        mssimfloat = ssim(last,img)
        last = img
        # 98%相似的就跳过
        if mssimfloat>=0.98:
            continue
        if mssimfloat>=0.9:
            continue        
        now = cap.get(cv2.CAP_PROP_POS_MSEC)
        ocrresult = ocr.ocr(img)
        print(now/1000,mssimfloat,count)
        print(ocrresult)
        result.append({
            "ocr":ocrresult,
            "time":now
        })
    with open(videopath+".json","w",encoding='utf-8') as f:
        f.write(json.dumps(result,ensure_ascii=False))
# process('/media/indigo6a/TOSHIBA EXT/迅雷下载/[§极度空间原创§][国产][神探狄仁杰]1,2,3部合集/神探狄仁杰第二部/crop/神探狄仁杰第二部02.rmvb_crop.mp4')        

# p = "/media/indigo6a/TOSHIBA EXT/迅雷下载/[§极度空间原创§][国产][神探狄仁杰]1,2,3部合集/神探狄仁杰第二部/crop"
# p = "/media/indigo6a/TOSHIBA EXT/迅雷下载/[§极度空间原创§][国产][神探狄仁杰]1,2,3部合集/神探狄仁杰第三部/crop"
p = "/media/indigo6a/TOSHIBA EXT/迅雷下载/[§极度空间原创§][国产][神探狄仁杰]1,2,3部合集/神探狄仁杰第一部/crop"

files = os.listdir(p)
for file in files:
    abs = os.path.join(p,file)
    if abs.endswith(".mp4"):
        process(abs)