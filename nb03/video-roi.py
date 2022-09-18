import cv2
from matplotlib import pyplot as plt

def sketch_transform(image):
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_grayscale_blurred = cv2.GaussianBlur(image_grayscale, (7,7), 0)
    image_canny = cv2.Canny(image_grayscale_blurred, 10, 80)
    _, mask = image_canny_inverted = cv2.threshold(image_canny, 30, 255, cv2.THRESH_BINARY_INV)
    return mask

cam_capture = cv2.VideoCapture(0)
cv2.destroyAllWindows()
upper_left = (150, 150)
bottom_right = (400, 400)
while True:
    _, image_frame = cam_capture.read()
    
    #Rectangle marker
    r = cv2.rectangle(image_frame, upper_left, bottom_right, (200, 100, 300), 5)
    rect_img = image_frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
    
    sketcher_rect = rect_img
    sketcher_rect = sketch_transform(sketcher_rect)
    
    #Conversion for 3 channels to put back on original image (streaming)
    sketcher_rect_rgb = cv2.cvtColor(sketcher_rect, cv2.COLOR_GRAY2RGB)
    
    #Replacing the sketched image on Region of Interest
    image_frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = sketcher_rect_rgb
    cv2.imshow("Sketcher ROI", image_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cam_capture.release()
cv2.destroyAllWindows()
