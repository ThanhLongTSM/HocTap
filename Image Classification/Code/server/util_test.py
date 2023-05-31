import cv2
import joblib
import json
import numpy as np
import base64
from wavelet import w2d
import matplotlib.pyplot as plt

__class_name_to_number = {}
__class_number_to_name = {}
__model = None
def classify_image(image_base64,file_path = None):
    imgs = get_cropped_image_if_2_eyes(file_path,image_base64)
    #resize and using wavelet transform
    result = []
    for img in imgs:
        #resize
        scalled_raw_img=cv2.resize(img,(32,32))
        haar_raw_img = w2d(scalled_raw_img,'db1',5)
        scalled_haar_img = cv2.resize(haar_raw_img,(32,32))
        combined_img = np.vstack((scalled_raw_img.reshape(32*32*3,1),scalled_haar_img.reshape(32*32,1)))

        #combined_img = np.vstack((scalled_haar_img.reshape(32*32*1,1),scalled_raw_img.reshape(32*32*3,1)))
        len_image_array = 32*32*3 + 32*32
        final = combined_img.reshape(1,len_image_array).astype(float)
    result.append(
        {
            'class':class_number_to_name(__model.predict(final)[0]),
            'class probabitily': np.round(__model.predict_proba(final)*100,2).tolist()[0],
            'class dictionary': __class_name_to_number
        }
    )

    return result
def class_number_to_name(class_num):
    return __class_number_to_name[class_num]
def get_cropped_image_if_2_eyes(file_path,image_base64):
    #import haarcascade to detect face and eyes
    face_cascade = cv2.CascadeClassifier('./opencv/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./opencv/haarcascades/haarcascade_eye.xml')

    if file_path:
        img = cv2.imread(file_path)
    else:
        img = base64_to_image(image_base64)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    cropped_faces=[]
    for (x,y,w,h) in faces:
        roi_gray= gray[y:y+h,x:x+w]
        roi_img = img[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,1.3,5)
        if len(eyes)>=2:
            cropped_faces.append(roi_img)
    return cropped_faces



def base64_to_image(b64str):
    encoded_data = b64str.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def load_saved_artifacts():
    print('Load saved artifacts ... start')
    global __class_name_to_number
    global __class_number_to_name
    global __model
    with open('./artifacts/class_dictionary.json','r') as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {v:k for k,v in __class_name_to_number.items()}


    if __model is None:
        with open('./artifacts/saved_model.pkl','rb') as f:
            __model = joblib.load(f)
    print('Loading saved artifacts ...done')
# ------------------------------------------------------------------
def get_base64_test_for_olsen():
    with open('b64.txt') as f:
        return f.read()


if __name__ == '__main__':
    load_saved_artifacts()
    print(classify_image(None,'./test_pictures/e_olsen2.jpg'))
    print(classify_image(get_base64_test_for_olsen(),None))


