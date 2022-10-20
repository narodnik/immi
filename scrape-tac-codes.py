import os, random, time

# Open this URL for i=1 in firefox
url = "https://swappa.com/imei/tac?page=%i"
number_pages = 605

# Start ydotoold

KEY_END = 107
KEY_BACKSPACE = 14
KEY_ENTER = 28
KEY_LEFTCTRL = 29
KEY_A = 30
KEY_S = 31

def move_mouse(x, y):
    os.system(f"ydotool mousemove --absolute -- {x} {y}")

def left_click():
    os.system(f"ydotool click 0xC0")

# Converts integer to keycode
def keycode_n(n):
    if n == 0:
        return 11
    return n + 1

def press_keys(keys):
    keys = [f"{k}:1 {k}:0" for k in keys]
    cmd = "ydotool key " + " ".join(keys)
    os.system(cmd)

def type_text(text):
    os.system(f"ydotool type '{text}'")

def ctrl_s():
    os.system(f"ydotool key {KEY_LEFTCTRL}:1 {KEY_S}:1 {KEY_S}:0 {KEY_LEFTCTRL}:0")

def ctrl_a():
    os.system(f"ydotool key {KEY_LEFTCTRL}:1 {KEY_A}:1 {KEY_A}:0 {KEY_LEFTCTRL}:0")

def randomly_sleep():
    # Select a random number between 6 and 12
    end = 12
    start = 6
    random_value = (end - start) * random.random() + start
    print(f"Sleeping {random_value} secs...")
    time.sleep(random_value)

    # 2% of the time, take a toilet break and sleep far longer
    if random.random() < 0.02:
        toilet_break = random.random() * 60
        time.sleep(toilet_break)

# ydotool mousemove --absolute -- 4500 32
# ydotool click 0xC0
# ydotool key 107:1 107:0 14:1 14:0 3:1 3:0

# Make sure to disable browser.urlbar.autoFill in about:config
def next_page(page_number):
    # move mouse to the location of the URL bar
    move_mouse(4500, 32)
    left_click()
    ctrl_a()
    press_keys([KEY_BACKSPACE])
    type_text(url % page_number)
    press_keys([KEY_ENTER])

def save_html_page(page_number):
    # make sure you have a folder called 'pages'
    move_mouse(4500, 32)
    ctrl_s()
    move_mouse(3900, 185)
    time.sleep(1)
    left_click()
    move_mouse(4100, 25)
    time.sleep(0.2)
    left_click()
    ctrl_a()
    press_keys([KEY_BACKSPACE])
    type_text(f"{page_number}.html")
    press_keys([KEY_ENTER])
    time.sleep(5)

# For testing
#next_page(4)
#randomly_sleep()
#save_html_page(1)

# Debugging
# Make sure to comment this when running for real
number_pages = 4

#os.system("rm -fr pages/*")

for current_page in range(1, number_pages + 1):
    next_page(current_page)
    randomly_sleep()
    save_html_page(current_page)

