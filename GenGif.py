# -*- coding:utf-8 -*-
"""
Dec: 结合使用Opencv和imageio包制作gif图像
Created on: 2018.06.03
Author: Iflier
"""
print(__doc__)

import time
import os.path
import argparse

import cv2
import imageio


# 要求gif记录的帧间距为 5 ~ 20 帧，默认帧间距为 10 帧
ap = argparse.ArgumentParser(description="A tools for generating gif.")
ap.add_argument('-i', '--interval', type=int, required=False, default=10,
                help="an interval between frames of gif.",
                choices=range(5, 21))
args = vars(ap.parse_args())

frameList = list()

cap = cv2.VideoCapture(os.path.join(os.getcwd(), 'testVideo.mp4'))
print("Getting video info ...")
# 获取视频的编码信息
print("[INFO] Codec parametrs: {0}".format(cap.get(cv2.CAP_PROP_FOURCC)))
# 获取视频包含的总的帧数
print("[INFO] Total frames : {0}".format(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
# 获取帧率
print("[INFO] FPS : {0}".format(cap.get(cv2.CAP_PROP_FPS)))
# 获取视频的宽和高
print("[INFO] Frame width: {0}".format(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("[INFO] Frame height: {0}".format(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print()

print("Starting generate GIF ...")

start = time.time()
for i in range(1, int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) + 1, 1):
    ret, frame = cap.read()
    if i % args["interval"] == 0:
        # BGR --> RGB顺序
        frameList.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # print("i = {0}".format(i))
cap.release()
imageio.mimwrite("test.gif", frameList, 'GIF')
print("Totally use {0:^9,.3f} seconds.".format(time.time() - start))
print("Done.")
