#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
img = cv2.imread('lena.jpg')

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()