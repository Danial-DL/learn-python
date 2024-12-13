# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget,QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QImage,Qt
import cv2
class Face_detection(QWidget):
	def __init__(self):
		super(Face_detection,self).__init__()
		Loader = QUiLoader()
		self.ui = Loader.load("/home/danial/project/python_projects/class_work/session_21/facedetection_UI/form.ui")
		self.ui.PB_1.clicked.connect(self.load_image) 
		self.ui.PB_2.clicked.connect(self.face_detection)
		self.ui.show()
	def load_image(self):
		self.file_path,x = QFileDialog.getOpenFileName(self,"open image file",
									 "Image(*.png *.jpg *.jpeg *.bmp *.gif)")
		self.ui.textEdit.setText(str(self.file_path))
		if self.file_path :
			pixmap = QPixmap(self.file_path)
			self.ui.label.setPixmap(pixmap)
			self.ui.label.setScaledContents(True)
	def face_detection(self):
		cap = str(self.file_path)
		img = cv2.imread(cap)
		haar_cascade_path = "haarcascade_frontalface_alt.xml"
		haar_cascade_path_face = "haarcascade_frontalface_alt.xml"    
		face_detector = cv2.CascadeClassifier(haar_cascade_path)
		eye_detector = cv2.CascadeClassifier(haar_cascade_path_face)
		eyes = eye_detector.detectMultiScale(img, 1.1)
		faces = face_detector.detectMultiScale(img, 1.1)
		for face in faces:
			x, y, w, h = face
			cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
		for eye in eyes:
			x, y, w, h = eye
			# Error ----------------------------
			center_x = x + w // 2
            center_y = y + h // 2
            radius = int((w + h) // 4)  
            cv2.circle(img, (center_x, center_y), radius, (0, 255, 0), 2)
			# Errore ----------------------------

			
   		# تبدیل تصویر OpenCV به QImage
		height, width, channel = img.shape
		bytes_per_line = 3 * width
		q_img = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
    	#تبدیل QImage به QPixmap و نمایش آن در لیبل
		pixmap = QPixmap.fromImage(q_img)
		self.ui.label.setPixmap(pixmap)
		self.ui.label.setScaledContents(True)
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Face_detection()
	sys.exit(app.exec_())