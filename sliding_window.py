import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread("test_images/test2.jpg")

def draw_boxes(img,bboxes):
    for boxes in bboxes:
        cv2.rectangle(img,boxes[0],boxes[1],(0,0,255),2)
    return img


def sliding_windows(image,window_size,overlap,start=None,stop=None):
    if start==None:
        start=(0,0)
    if stop==None:
        stop=(image.shape[1],image.shape[0])


    length_covered_in_overlap_x=window_size[0]-np.int(overlap[0]*window_size[0])
    length_covered_in_overlap_y=window_size[1]-np.int(overlap[1]*window_size[1])

    bboxes=[]

    span_x=(start[0],stop[0]-window_size[0])
    span_y=(start[1],stop[1]-window_size[1])

    current_x,current_y=start

    while(current_y <= span_y[1]):

        while(current_x <= span_x[1]):
            print("x",current_x)
            bboxes.append([(current_x,current_y),(current_x+window_size[0],current_y+window_size[1])])
            current_x=current_x+length_covered_in_overlap_x

        current_y = current_y + length_covered_in_overlap_y
        current_x = start[0]

    image=draw_boxes(image,bboxes)
    plt.imshow(image)
    plt.show()







sliding_windows(img,(64,64),(0.5,0.5),(0,400),(img.shape[1],656))


