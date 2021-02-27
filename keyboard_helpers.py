from pynput import keyboard

running = True
holding_key = {'[': False}
released_key = {']': False}

def on_press(key):
    global running, holding_key, released_key
    try:
        holding_key[key.char] = True
        released_key[key.char] = False
        if key.char == 'q':
            running = False
            return False
    except:
        # print(f'unhandled {key}')
        pass

def on_release(key):
    global holding_key, released_key
    try:
        holding_key[key.char] = False
        released_key[key.char] = True
    except:
        # print(f'unhandled {key}')
        pass

def start_keyboard():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
        )
    listener.start()
