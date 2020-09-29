
import speech_recognition as sr
import webbrowser as wb


r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search youtube: search wikipedia]')
    print('What do you wish to see?! If its youtube say "video" or for any particular details say "information"  ')
    print('SPEAK NOW!!')
    audio = r3.listen(source)


    if 'information' in r2.recognize_google(audio):
        r2 = sr.Recognizer()
        url = 'https://en.wikipedia.org/wiki/'

        with sr.Microphone() as source:
            print('SEARCH YOUR QUERY!!')
            audio = r2.listen(source)


        try:
                 get = r2.recognize_google(audio)
                 print(get)
                 wb.get().open_new(url+get)

        except sr.UnknownValueError:
                print('say that again please...')
        except sr.RequestError as e:
                print('failed'.format(e))

    if 'video' in r1.recognize_google(audio):
        r1 = sr.Recognizer()
        url = 'https://www.youtube.com/results?search_query='

        with sr.Microphone() as source:
            print('search your query')
            audio = r1.listen(source)

            try:
                 get = r1.recognize_google(audio)
                 print(get)
                 wb.get().open_new(url+get)

            except sr.UnknownValueError:
                print('error')
            except sr.RequestError as e:
                print('failed'.format(e))

                if 'find' in r2.recognize_google(audio):
                    r2 = sr.Recognizer()
                    url = 'https://en.wikipedia.org/wiki/'

                    with sr.Microphone() as source:
                        print('SEARCH YOUR QUERY!!')
                        audio = r2.listen(source)

                        try:
                            get = r2.recognize_google(audio)
                            print(get)
                            wb.get().open_new(url + get)

                        except sr.UnknownValueError:
                            print('say that again please...')
                        except sr.RequestError as e:
                            print('failed'.format(e))
