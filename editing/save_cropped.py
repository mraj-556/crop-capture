import cv2


def crop_area(p):
    x1,y1 = p[0] , p[1]
    x2,y2 = p[2] , p[3]
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,250,0),2)
    cropped_img = img[y1:y2,x1:x2]
    cv2.imshow('crop',img)
    cv2.imshow('cropped',cropped_img)
    

global select_mode,pos
pos = []
select_mode = True

def clear():
    global pos,select_mode
    select_mode = True
    pos = []

def mouse_pos(event, x, y, p1, p2):
    global select_mode , pos
    # print(len(pos))
    if event == cv2.EVENT_LBUTTONDOWN and select_mode:
        # print(len(pos))
        pos.append([x,y])
        cv2.circle(img,(x,y),2,(0,0,250),cv2.FILLED)
        cv2.imshow('crop',img)
    if len(pos) == 2 and select_mode:
        select_mode = False
        if  (pos[0][0]!=pos[1][0] and pos[0][1]!=pos[1][1]):
            print('area found')
            p = [pos[0][0],pos[0][1] , pos[1][0] , pos[1][1]]
            crop_area(p)
        

flag = True
while flag:
    img = cv2.imread('images/human.png')
    cv2.imshow('crop',img)
    cv2.setMouseCallback('crop',mouse_pos)
    
    while True:
        # cv2.putText(img,str(select_mode),(60,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 250, 0),2)
        cv2.imshow('crop',img)
        k = cv2.waitKey(1)
        if k== ord('q'):
            flag = False
            break
        # if k== ord('n'):
        #     if select_mode == False:
        #         select_mode = True
        #     else:
        #         select_mode = False
        #     print('mode : ',select_mode)
        if k == ord('c'):
            clear()
            break