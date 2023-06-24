import cv2

img = cv2.imread("poster.jpg")
rocket=img[120:360,400:500]
img[0:240,500:600] = rocket

text_show = "Rocket"
cv2.putText(img,
            text_show,
            (200,200),
            fontScale=1,
            color=(0,0,255),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL)
cv2.imshow("output", img)
cv2.waitKey(0)