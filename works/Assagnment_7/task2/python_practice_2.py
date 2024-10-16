import cv2
path_monalisa = "monalisa.jpg"
image_last = cv2.imread(path_monalisa)
output = cv2.convertScaleAbs(image_last,alpha=2,beta=0)
cv2.imshow("Previous image",image_last)
cv2.imshow("New image",output)
cv2.imwrite("output.jpg",output)
cv2.waitKey(0)
cv2.destroyAllWindows()