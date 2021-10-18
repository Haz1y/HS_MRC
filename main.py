# encoding: UTF-8

import re
import pyautogui
import cv2
import numpy as np
import time

global LOGFILE, encoding, preImg
pyautogui.FAILSAFE = False
LOGFILE = "C:\\Program Files (x86)\\Hearthstone\\Logs\\Power.log"
encoding = "UTF-8"
preImg = [cv2.imread(f"./hs/{i}.png") for i in range(3)]


def screenshot(x=376, y=292 + 30, w=530, h=430 - 30):
    img = pyautogui.screenshot(region=[x, y, w, h])  # x,y,w,h
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    return img


def imgSave(i=9):
    img = screenshot()
    cv2.imwrite(f"./hs/{i}.png", img)
    cv2.imshow(str(i), img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def ORB_img_similarity(img1, img2):
    try:
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)
        good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
        similary = len(good) / len(matches)
        return similary
    except:
        return float(0)


def compare(img):
    result = 9
    p = 0.4
    for i in range(3):
        res = float(ORB_img_similarity(preImg[i][277:380, 0:530], img[277:380, 0:530]))
        if res > p:
            p = res
            result = i
    print(f"res = {result}, p = {p}")
    return result


def movClick(x, y, t=0.7):
    pyautogui.moveTo(x, y, duration=t, tween=pyautogui.easeInOutQuad)
    pyautogui.click()


def gaming():
    flagGameover = 0
    flagTimesleep = 0
    with open(LOGFILE, 'r', encoding=encoding) as log:
        while log.readline():
            pass
        while True:
            line = log.readline()
            if line:
                if re.findall(r"tag=STEP value=MAIN_ACTION", line):
                    flagTimesleep = 0
                    time.sleep(10)
                    logLine = log.readline()
                    while logLine:
                        if re.findall(r"tag=STEP value=FINAL_GAMEOVER", line):
                            flagGameover += 1
                        logLine = log.readline()
                    movClick(572, 501)
                    movClick(632, 436)
                    movClick(861, 506)
                    time.sleep(1)
                    movClick(861, 506)
                elif re.findall(r"tag=STEP value=FINAL_GAMEOVER", line):
                    flagTimesleep = 0
                    time.sleep(3)
                    logLine = log.readline()
                    while logLine:
                        if re.findall(r"tag=STEP value=FINAL_GAMEOVER", line):
                            flagGameover += 1
                        logLine = log.readline()
                    flagGameover += 1
            else:
                time.sleep(1)
                flagTimesleep += 1
                print(flagTimesleep)
            if flagTimesleep > 180:
                movClick(861, 506)
                movClick(828, 650)
            if flagGameover >= 1:
                print("game over")
                return


if __name__ == '__main__':
    while True:
        img = screenshot()
        res = compare(img)
        movClick(466, 460)
        movClick(828, 650)
        time.sleep(3)
        movClick(443, 453)
        movClick(828, 650)
        movClick(597, 553)
        movClick(828, 650)
        time.sleep(2)
        for _ in range(3):
            movClick(586, 512)
            movClick(511, 522)
            movClick(481, 514)
            movClick(455, 521)
            movClick(828, 650, 0.1)
            movClick(828, 650, 0.1)
            gaming()
            time.sleep(13)  # 1
            movClick(828, 650, 0.1)
            time.sleep(3)
            movClick(828, 650, 0.1)
            time.sleep(3)
            movClick(563, 514)
            movClick(708, 641)
            movClick(563, 514)
            movClick(708, 641)
            time.sleep(5)
        movClick(565, 400)
        movClick(828, 650, 0.5)
        movClick(828, 650, 0.1)
        gaming()
        time.sleep(13)
        movClick(828, 650, 0.1)
        time.sleep(3)
        movClick(828, 650, 0.1)
        time.sleep(13)
        movClick(828, 650, 0.1)
        movClick(510, 602, 0.2)
        movClick(650, 450, 0.2)
        movClick(782, 627, 0.2)
        movClick(510, 602, 0.2)
        movClick(650, 450, 0.2)
        movClick(782, 627, 0.2)
        time.sleep(2)
        movClick(654, 549)
        time.sleep(8)
        movClick(631, 647)
        time.sleep(5)
        print("done")