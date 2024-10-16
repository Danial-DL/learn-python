import cv2
# import ast
chess = cv2.imread("chess.png")
gray = cv2.cvtColor(chess,cv2.COLOR_BGR2GRAY)
size_x = 100
size_x_x = 200
size_y = 100
size_y_y = 210
# print (str(top))
def FOR(Y,Y_Y,P):
    size_x = 100
    size_x_x = 200
    D = 0
    for i in range(8):
        top = gray[Y:Y_Y,size_x:size_x_x]
        #cv2.imshow("tp",top)
        if "128" in str(top) or "255" in str(top):
            cv2.imwrite(f"image{D}{P}.jpg",top)
            D += 1
        # print(f"test{i}/n")
        # print(top)
        # else :
        #     print("No")
        size_x += 120
        size_x_x += 130
for x in range(8):
    FOR(size_y,size_y_y,x)
    size_y += 120
    size_y_y += 130
# size_x = 100
# size_x_x = 200
# size_y += size_y
# size_y_y += size_y_y
cv2.waitKey(0)