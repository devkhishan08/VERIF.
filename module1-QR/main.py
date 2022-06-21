import qrcode
import cv2
img = qrcode.make('Hello World')
img.save('hello.png')

img = cv2.imread("hello.png")
det=cv2.QRCodeDetector()
val,pts,st_code=det.detectAndDecode(img)
print(val)
