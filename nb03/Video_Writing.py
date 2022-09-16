# import the library
import cv2

source = 0
cap = cv2.VideoCapture(source)

# Default resolutions of the frame are obtained.
# Convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

size = (frame_width, frame_height)

'''result = cv2.VideoWriter('/home/nilo/computer-vision/nb03/output.mp4',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)'''

# Define the codec and create VideoWriter object.
out_avi = cv2.VideoWriter('../computer-vision/nb03/output.avi',cv2.VideoWriter_fourcc(*'MJPG'), 10, (frame_width,frame_height))
out_mp4 = cv2.VideoWriter('../computer-vision/nb03/output.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 10.0, (frame_width,frame_height))

while(True):
    ret, frame = cap.read()

    if ret == True:
            # Write the frame to the output files
        out_avi.write(frame)
        out_mp4.write(frame)
        
        # Display the frame
        # saved in the file
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

# Closes all the frames
cv2.destroyAllWindows()

print("The video was successfully saved")