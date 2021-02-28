from colorama import Fore
from colorama import Style
import colorama
import cursor

REC_TEXT = ' REC'

def init_print():
    cursor.hide()
    colorama.init()

def print_exit():
    cursor.show()
    print()
    print('Bye!')

def print_start_recording():
    print()
    print('usage:')
    print(f'hold  "[": record')
    print('press "]": final take')
    print('press "q": quit')
    print('-----------------------')
    print('seq# | try#')
    print(' 001 |', end = '', flush=True)

def print_next_seq(seqn):
    print()
    print(f' {seqn:03} |', end = '', flush=True)

rec_text_state = REC_TEXT
def print_rec():
    global rec_text_state
    print(Fore.YELLOW + rec_text_state + Style.RESET_ALL, end = '\b'*len(rec_text_state))
    rec_text_state = ' '*len(REC_TEXT) if rec_text_state == REC_TEXT else REC_TEXT

def print_final_try(tryn):
    print('\b'*4 + Fore.GREEN + f' {tryn:03}' + Style.RESET_ALL, end = '', flush = True)

def print_failed_try(tryn):
    print('\b'*4 + Fore.RED + f' {tryn:03}' + Style.RESET_ALL, end = '', flush = True)

def print_latest_try(tryn):
    print(Fore.YELLOW + f' {tryn:03}' + Style.RESET_ALL, end = '', flush = True)
