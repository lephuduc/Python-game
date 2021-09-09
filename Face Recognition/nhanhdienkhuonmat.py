import cv2
import dlib

#đọc hình ảnh
img = cv2.imread("it_s_ok_2.png")

#convers img to black white (3D>2D)
gray=cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

#dlib
face_detector=dlib.get_frontal_face_detector()

#loat preditor
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#use detector 
faces=face_detector(gray)

#draw retagal
for face in faces:
    x1=face.left()
    y1=face.top()
    x2=face.right()
    y2=face.bottom()
    #vẽ hình chứ nhật:
    cv2.rectangle(img=img, pt1=(x1,y1), pt2=(x2,y2),color=(255,108,180),thickness=4)
    #tao list các điểm được vẽ
    face_features = predictor(image=gray, box=face)
    #vẽ 68 điểm:
    for n in range(0,68):
        x=face_features.part(n).x
        y=face_features.part(n).y
        # vẽ chấm
        cv2.circle(img=img,center=(x,y),radius=2,thickness=1,color=(255,108,180))

#show ảnh
cv2.imshow(winname="Face recognition App",mat=img)

#wait for key exit
cv2.waitKey(delay=0)

#clode window
cv2.destroyAllWindows()