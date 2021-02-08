import cv2 as cv
import numpy as np
import math
class Normal():
    def __init__(self, image):
        self.image = image
        self.height = len(image)
        self.width = len(image[0])
        self.img_out = np.zeros_like(image)

    def change_picture(self, x, y):
        x_normal = float((2*x - self.height)/self.height)
        y_normal = float((2*y - self.width)/self.width)
        rd = math.sqrt(x_normal ** 2 + y_normal ** 2)
        if (rd < 1):
            rd = (rd + (1 - math.sqrt(1 - rd ** 2))) / 2
            theta = math.atan2(y_normal , x_normal)
            Xdu = rd * math.cos(theta)
            Ydu = rd * math.sin(theta)
            Xu = int(((Xdu + 1) * self.height) / 2)
            Yu = int(((Ydu + 1) * self.width) / 2)
            if Xu < self.height:
                if Yu < self.width:
                    self.img_out[Xu][Yu] = self.image[x][y]
    def normalize(self):
        for x in range(0, self.height):
            for y in range(0, self.width):
                self.change_picture(x, y)
        return self.img_out

file_name = "nasa"
file_type = ".jpg"
image = cv.imread(file_name + file_type, 1)
normal = Normal(image)
out = normal.normalize()
cv.imwrite('nasa_normal.png', out)
