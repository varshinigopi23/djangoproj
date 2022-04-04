from django import views
import pyautogui
import time
from pynput.keyboard import Key,Controller as KeyboardController



keyboard= KeyboardController()

#import pyscreenshot
def screenshot(t1,vm):
    
    if t1==0:
        pyautogui.screenshot(r'C:\\Users\\gvarshini\\Desktop\\screenshot\\'+vm+'_'+'imagefinal.png')
    else:
        #pyautogui.screenshot(r'C:\\Users\\gvarshini\\Desktop\\screenshot\\imagefinal.png')
        for i in range(t1,0,-1):

            #i=i+1
            
            pyautogui.screenshot(r'C:\\Users\\gvarshini\\Desktop\\screenshot\\'+vm+'_'+'image'+str(i)+'.png')
            with keyboard.pressed(Key.shift):
                keyboard.press(Key.page_up)
                keyboard.release(Key.page_up)
            #with keyboard.pressed(Key.shift):
                keyboard.press(Key.page_up)
                keyboard.release(Key.page_up)
                
            #pyautogui.screenshot(r'C:\\Users\\gvarshini\\Desktop\\screenshot\\image'+str(i)+'.png')
            time.sleep(4)
        
        pyautogui.screenshot(r'C:\\Users\\gvarshini\\Desktop\\screenshot\\'+vm+'_'+'image0.png')

#screenshot()