import cv2


global select_mode,pos

pos = []
select_mode = True
def mouse_pos(event, x, y, p1, p2):
    global select_mode , pos
    if event == cv2.EVENT_LBUTTONDOWN and select_mode:
        pos.append([x,y])
        cv2.circle(img,(x,y),2,(0,0,250),cv2.FILLED)
        for i in range(1,len(pos)):
            cv2.line(img,(pos[i][0],pos[i][1]),(pos[i-1][0],pos[i-1][1]),(0,250,0),2)
        cv2.imshow('crop',img)
        print('clicked : ',x,y)

flag = True
while flag:
    img = cv2.imread('images/human.png')
    cv2.imshow('crop',img)
    cv2.setMouseCallback('crop',mouse_pos)

    while True:
        k = cv2.waitKey(1)
        if k== ord('q'):
            flag = False
            break
        if k== ord('n'):
            if select_mode == True:
                select_mode = False
                print('new')
            elif select_mode == False:
                select_mode = True
        if k== ord('c'):
            pos = []
            break
            print('Cleared')