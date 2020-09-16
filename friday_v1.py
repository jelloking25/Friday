import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random


speech = sr.Recognizer()


greeting_dict = {'hello':'hello', 'hi':'hi'}
open_launch_dict = {'open':'open','launch':'launch'}

mp3_open_launch_list = ['mp3/friday/Open1.mp3','mp3/friday/Open2.mp3','mp3/friday/Open3.mp3']
output = str(random.choice(mp3_open_launch_list))
mp3_greeting_list = ['mp3/friday/Greeting accept.mp3','mp3/friday/Greeting accept2.mp3']
social_media_list = {'youtube':'https://www.youtube.com/','twitter':'https://twitter.com/?lang=en','facebook':'https://www.facebook.com/','instagram':'https://www.instagram.com/?hl=en','tiktok':'https://www.tiktok.com/en/','google':'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk','manorama':'https://www.manoramaonline.com/home.html','news':'https://www.youtube.com/results?search_query=news','mail':'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'}
mp3_greeting_accept_list = ['mp3/friday/How accept.mp3','mp3/friday/How accept2.mp3']
mp3_search_found_list = ['mp3/friday/Search Found.mp3','mp3/friday/Search1.mp3']
mp3_bye_list = ['mp3/friday/Bye.mp3']
mp3_how_accept_list = ['mp3/friday/How accept.mp3','mp3/friday/How accept2.mp3']
mp3_thank_you_list = ['mp3/friday/Thankyou1.mp3','mp3/friday/Thankyou2.mp3']


def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    play_sound(mp3_list)


def read_voice_cmd():
    voice_text = ''
    print('Listening...')
    with sr.Microphone() as source:
        audio = speech.listen(source=source,timeout=5,phrase_time_limit=5)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network Error.')
    except sr.WaitTimeoutError:
        pass

    return voice_text


def is_valid_note(greet_dict, voice_note):
    for key,value in greet_dict.items():
        #'Hello Friday'
        try:
            if value == voice_note.split(' ')[0]:
                return True
                break
            elif key == voice_note.split(' ')[1]:
                return True
                break

        except IndexError:
            pass

    return False


if __name__ == '__main__':

    playsound('mp3/friday/Greeting.mp3')

    while True:

        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))

        if 'hello' in voice_note:
            print('In greeting...')
            playsound(random.choice(mp3_greeting_list))
        elif 'thank you' in voice_note:
            playsound(random.choice(mp3_thank_you_list))
        elif 'hai' in voice_note:
            playsound(random.choice(mp3_greeting_list))
        elif 'how are you' in voice_note:
            playsound(random.choice(mp3_how_accept_list))
        elif is_valid_note(open_launch_dict,voice_note):
            print('In open...'.format(playsound(output)))
            if (is_valid_note(social_media_list,voice_note)):
                # Launching web browser
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_list.get(key))
            else:
                os.system('explorer C:\\ "{}"'.format(voice_note.replace('open ', '').replace('launch ', '')))
            continue
        elif 'by' in voice_note:
            playsound(random.choice(mp3_bye_list))
            exit()
