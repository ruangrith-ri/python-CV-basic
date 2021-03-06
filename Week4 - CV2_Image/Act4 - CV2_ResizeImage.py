# importing cv2
import cv2

# path
path = r'C:\Users\admin\Desktop\MDT425\Week2 - BasicCapture\geeksforgeeks.png'

# Using cv2.imread() method
img = cv2.imread(path)


width, height = img.shape[0:2]

#Resize
resizeImg = cv2.resize(img,(0,0),fx = 0.75,fy = 0.5)

# Displaying the image
cv2.imshow('Resize image', resizeImg)
cv2.waitKey()