import cv2


img = cv2.imread('CV2/mario.jpeg')

pixelated_img = cv2.resize(
                            img,
                           (100, 100),
                           interpolation=cv2.INTER_NEAREST
                           )

pixelated_img = cv2.resize(
                            pixelated_img,
                            (696, 664),
                            interpolation=cv2.INTER_NEAREST
                            )

cv2.imshow('img Pixelizada', pixelated_img)
cv2.waitKey(0)
#cv2.destroyAllWindows()