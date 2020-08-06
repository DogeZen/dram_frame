import cv2
import numpy as np


fname = 'test.jpg'
img = cv2.imread(fname)

list_frames = [  {"x":"0.152083","y":"0.712963","w":"0.104167","h":"0.096296"} ,{
      "x": "0.379167",
      "y": "0.740741",
      "w": "0.090625",
      "h": "0.248148"
     } ]


for dict in list_frames:
    print(img.shape[0])
    width = float(img.shape[1])*float(dict['w'])
    height = float(img.shape[0])*float(dict['h'])

    dict_ = {"x1":int(float(img.shape[1])*float(dict['x']))
        , "x2":int(float(img.shape[1])*float(dict['x'])+width)
        ,"y1":int(float(img.shape[0])*float(dict['y']))
        ,"y2":int(float(img.shape[0])*float(dict['y'])+height )    }
    print(dict_)
    cv2.rectangle(img, (dict_['x1'], dict_['y1']),(dict_['x2'], dict_['y2']), (0, 255, 0), 2)

# cv2.imwrite("123.jpg",img)
cv2.imshow("123",img)

key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):  #它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值
    cv2.imwrite("123.jpg",img)
    cv2.destroyAllWindows()

