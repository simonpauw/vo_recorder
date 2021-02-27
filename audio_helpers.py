import pyaudio
import wave


AUDIO_PARAMS = {'channels':         2,
                'format':           pyaudio.paInt16,
                'rate':             44100,
                'chunk':            22050,
                'audio_device_id':  None}

audio_state = {
    'recording': False,
    'frames': None,
    'player': None,
    'stream': None,
    'basename': 'test',
    'dir': 'recordings',
    'seq': 1,
    'try': 0}

def filename(state):
    return f"{state['dir']}/{state['basename']}_{state['seq']:03}_{state['try']:03}.wav"


def start_rec_stream():
    global AUDIO_PARAMS, audio_state
    p = pyaudio.PyAudio()
    stream = p.open(format              = AUDIO_PARAMS['format'],
                    channels            = AUDIO_PARAMS['channels'],
                    rate                = AUDIO_PARAMS['rate'],
                    input               = True,
                    frames_per_buffer   = AUDIO_PARAMS['chunk'],
                    input_device_index  = AUDIO_PARAMS['audio_device_id'])

    audio_state['stream'] = stream
    audio_state['player'] = p
    audio_state['recording'] = True
    audio_state['frames'] = []
    audio_state['try'] += 1



def stop_rec_stream():
    audio_state['stream'].stop_stream()
    audio_state['stream'].close()
    audio_state['stream'] = None
    audio_state['player'].terminate()
    audio_state['recording'] = False


def write_frames():
    wf = wave.open(filename(audio_state), 'wb')
    wf.setnchannels(AUDIO_PARAMS['channels'])
    wf.setsampwidth(audio_state['player'].get_sample_size(AUDIO_PARAMS['format']))
    wf.setframerate(AUDIO_PARAMS['rate'])
    wf.writeframes(b''.join(audio_state['frames']))
    wf.close()

def rec_frame():
    data = audio_state['stream'].read(AUDIO_PARAMS['chunk'])
    audio_state['frames'].append(data)


def select_audio_device():
    global AUDIO_PARAMS
    print("Audio input devices:")
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

    device_id = -1
    while device_id < 0 or device_id >= numdevices:
        try:
            device_id = int(input('Select input device id: '))
        except:
            print('Invalid input')
            device_id = -1

    AUDIO_PARAMS['audio_device_id'] = device_id

    print(f'Using {p.get_device_info_by_host_api_device_index(0, device_id).get("name")}')
