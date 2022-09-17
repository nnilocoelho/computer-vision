# import the library
import cv2
import matplotlib.pyplot as plt



source = 0
cap = cv2.VideoCapture(source)

if (cap.isOpened()== False): 
  print("Error opening video stream or file")
  
# Default resolutions of the frame are obtained.
# Convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.
out_avi = cv2.VideoWriter('../computer-vision/nb03/video-saved-v2.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
out_mp4 = cv2.VideoWriter('../computer-vision/nb03/video-saved-v2.mp4',cv2.VideoWriter_fourcc(*'XVID'), 10, (frame_width,frame_height))

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
    
  if ret == True:
    
    # Write the frame to the output files
    out_avi.write(frame)
    out_mp4.write(frame)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
  # Break the loop
  else: 
    break
# When everything done, release the VideoCapture and VideoWriter objects
cap.release()
out_avi.release()
out_mp4.release()
