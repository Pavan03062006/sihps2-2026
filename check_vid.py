import cv2
cap = cv2.VideoCapture('src/sigid/web/static/bg-video.mp4')
print('Opened:', cap.isOpened())
ret, frame = cap.read()
if ret:
    cv2.imwrite('src/sigid/web/static/frame0.jpg', frame)
    print('Saved frame0.jpg, shape:', frame.shape)
cap.release()
