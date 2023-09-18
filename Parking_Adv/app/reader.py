import cv2
import easyocr

reader = easyocr.Reader(["es"], gpu = False)
cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if cam.isOpened():
    cap, placa = cam.read()
    cv2.imshow("Placa", placa)
    resultado = reader.readtext(placa)
else: print("Algo salió mal")

for r in resultado:
    print("Texto:", r[0][5])

cv2.imwrite("Placa.jpg", placa)
cv2.waitKey(0)
cv2.destroyAllWindows()
