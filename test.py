
import pyautogui

import test2
import test1
import sys
import os
import time
import shutil
from pynput.keyboard import Key,Controller as KeyboardController
from pynput.mouse import Button,Controller as MouseController

keyboard= KeyboardController()
def controlmouse():
    mouse=  MouseController()
    time.sleep(3)


    mouse.position=(423, 234)
    mouse.click(Button.left,1)

def controlkey(content_list,vm,u,p):
    #keyboard= KeyboardController()
    time.sleep(3)
    
    t=0
    for i in content_list:
        keyboard.type(i)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        c=test1.para(i,vm,u,p)
        if c!='':
            c=int(c)
            
            t=t+c
    

    time.sleep(5)
    
    t1=t//44
    shutil.rmtree('C:\\Users\\gvarshini\\Desktop\\screenshot')
    main_dir = "C:\\Users\\gvarshini\\Desktop\\screenshot"
 
    os.mkdir(main_dir)
    test2.screenshot(t1,vm)
    #pyautogui.screenshot(r'C:\\Users\\gvarshini\\Desktop\\screenshot\\image0.png')

    '''i=10
    for i in range(i,-1,-1):

        #i-=1
        test2.screenshot(i)
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.page_up)
            keyboard.release(Key.page_up)
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.page_up)
            keyboard.release(Key.page_up)

        time.sleep(3)'''
try:        
    src_path = r"C:\\Users\\gvarshini\\Downloads\\cred.txt"
    dst_path = r"C:\\Users\\gvarshini\\Desktop\\djangoproj\\cred1.txt"
    shutil.move(src_path, dst_path)
    my_file=open('C:\\Users\\gvarshini\\Desktop\\djangoproj\\cred1.txt',"r")
    content=my_file.read()
    content_list=content.split("\n")
except:
    my_file=open('C:\\Users\\gvarshini\\Desktop\\djangoproj\\cred1.txt',"r")
    content=my_file.read()
    content_list=content.split("\n")
src_path1 = r"C:\\Users\\gvarshini\\Downloads\\commandtext.txt"
dst_path1 = r"C:\\Users\\gvarshini\\Desktop\\djangoproj\\command.txt"
shutil.move(src_path1, dst_path1)
my_file1=open('C:\\Users\\gvarshini\\Desktop\\djangoproj\\command.txt',"r")
content1=my_file1.read()
#print(content1)
content_list1=content1.split("\n")
#print(content_list1)
s='putty '+content_list[0]+'@'+content_list1[0]+' -pw '+content_list[1]
#print(s)    
        
        
        
os.popen(cmd=s)
with keyboard.pressed(Key.alt):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
time.sleep(3)
with keyboard.pressed(Key.cmd):
    keyboard.press(Key.up)
    keyboard.release(Key.up)
controlmouse()
controlkey(content_list1[1:],content_list1[0],content_list[0],content_list[1])
print(content_list1[0])
with keyboard.pressed(Key.ctrl):
    keyboard.press('d')
    keyboard.release('d')


