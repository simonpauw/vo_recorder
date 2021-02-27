import time

import print_helpers as pr
import audio_helpers as audio
import keyboard_helpers as kb

def loop():
    # when finished last try
    if kb.released_key[']']:
        kb.released_key[']'] = False

        # if still recording for some reason, stop
        if audio.audio_state['recording']:
            audio.stop_rec_stream()
            audio.write_frames()

        # is there has been at least one try
        if audio.audio_state['try'] > 0:
            pr.print_final_try(audio.audio_state['try'])
            audio.audio_state['seq'] += 1
            audio.audio_state['try'] = 0

        # show seq number
        pr.print_next_seq(audio.audio_state['seq'])

    # while record key pressed
    if kb.holding_key['[']:

        if not audio.audio_state['recording']:
            if audio.audio_state['try'] > 0:
                pr.print_failed_try(audio.audio_state['try'])
            audio.start_rec_stream()
        audio.rec_frame()
        pr.print_rec()

    # if record key not pressed
    else:
        # if still recording, stop
        if audio.audio_state['recording']:
            audio.stop_rec_stream()
            audio.write_frames()
            pr.print_latest_try(audio.audio_state['try'])

def init():
    audio.select_audio_device()

    kb.start_keyboard()

    pr.init_print()

    pr.print_start_recording()

def exit():

    pr.cursor.show()

    pr.print_exit()

if __name__ == '__main__':
    init()
    while kb.running:
        loop()
    exit()
