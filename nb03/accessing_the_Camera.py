import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("Video da Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.imwrite("../computer-vision/nb03/Output_Picture.png", frame)

webcam.release()
cv2.destroyAllWindows()