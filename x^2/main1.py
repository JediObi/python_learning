import cv2


def on_mouse(event, x, y, flags, param):
    global point1, point2
    if event == cv2.EVENT_LBUTTONDOWN:
        point1 = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        point2 = (x, y)
        cv2.rectangle(img, point1, point2, (0, 0, 255), 1)
        cv2.imshow('Image', img)
        min_y = point1[1]
        min_x = point1[0]
        height = point2[1] - point1[1]
        width = point2[0] - point1[0]
        cut_img = img[min_y:min_y + height, min_x:min_x + width]
        cv2.imshow('Image', cut_img)


img_path = '/home/hm70/Pictures/girl_240_320.jpg'
img = cv2.imread(img_path)
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', on_mouse)
cv2.imshow('Image', img)
cv2.waitKey(0)
