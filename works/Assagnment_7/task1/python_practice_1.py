import cv2
from colorama import Fore
path_health_board = "board_health.jpg"
origin = cv2.imread(path_health_board)
path_test_board = "board_test.jpg"
test = cv2.imread(path_test_board)
if str(origin) == str(test):
    print(Fore.BLUE,"board test is Health :]")
else :
    print(Fore.RED , "Board test is not Health :[")