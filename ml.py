import os
import sys
import wikipedia
from gtts import gTTS
import pprint
from googleapiclient.discovery import build
from colorama import Fore, Back, Style

language='id'
kata = "Masukkan kata kunci pencarian Anda."
credit = "Tools ini Di Tulis Oleh Fadol, Berikut menu menu Yang Tersedia"
ada = "satu search pengetahuan wiki. dua search pengetahuan google. tiga search pertanyaan apa aja atau cari jawaban tugas. empat search pengetahuan pak onno center."
buka = "buka link kah"
rayu = "hayu mau pilih yang mana?"

def wiki():
   my_api_key = "AIzaSyC5DEN8jdxxCCp07aUoQUjpBA0uNipKPes"
   my_cse_id = "88fe994e36411957c"
   speech = gTTS(text = kata, lang=language, slow=False)
   speech.save("kata.mp3")
   os.system("mpv kata.mp3")
   os.system('clear')
   value=input(Fore.CYAN + "Masukkan Kata kunci pencarian anda : ")
   def wiki_search(search_term, api_key, cse_id, **kwargs):
       service = build("customsearch", "v1", developerKey=api_key)
       res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
       return res['items']
   jumlah=input(Fore.CYAN + "jumlah result : ")
   results = wiki_search(value, my_api_key, my_cse_id, num=jumlah)

   for result in results:
       '''pprint.pprint(result)'''
       title = result['title']
       link = result['formattedUrl']
       dis = result['snippet']
       print (title)
       print (dis)
       print (Fore.RED + link)
       def web():
           web = input(Fore.CYAN + "buka link kah (y/t)?")
           if web == 'y':
              os.system('xdg-open' + ' '+ link + '')
       hasil = dis
       speech = gTTS(text = hasil, lang=language, slow=False)
       speech.save("hasil.mp3")
       os.system("mpv hasil.mp3")
       os.system('clear')
       speech = gTTS(text = buka, lang=language, slow=False)
       speech.save("buka.mp3")
       os.system("mpv buka.mp3")
       os.system('clear')
       web()
   
def google():
   my_api_key = "AIzaSyBzrRAVaHxjENMFX48hsQfMzfE9b4yGzrM"
   my_cse_id = "84cd48900faca7110"
   speech = gTTS(text = kata, lang=language, slow=False)
   speech.save("kata.mp3")
   os.system("mpv kata.mp3")
   os.system('clear')
   value=input(Fore.CYAN + "Masukkan Kata kunci pencarian anda : ")
   jumlah=input(Fore.CYAN + "jumlah result : ")
   def google_search(search_term, api_key, cse_id, **kwargs):
       service = build("customsearch", "v1", developerKey=api_key)
       res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
       return res['items']

   results = google_search(value, my_api_key, my_cse_id, num=jumlah)

   for result in results:
       '''pprint.pprint(result)'''
       title = result['title']
       link = result['formattedUrl']
       dis = result['snippet']
       print (title)
       print (dis)
       print (Fore.RED + link)
       def web():
           web = input(Fore.CYAN + "buka link kah (y/t)?")
           if web == 'y':
              os.system('xdg-open' + ' '+ link + '')
       hasil = dis
       speech = gTTS(text = hasil, lang=language, slow=False)
       speech.save("hasil.mp3")
       os.system("mpv hasil.mp3")
       os.system('clear')
       speech = gTTS(text = buka, lang=language, slow=False)
       speech.save("buka.mp3")
       os.system("mpv buka.mp3")
       os.system('clear')
       web()
def wiki_ono():
   my_api_key = "AIzaSyBzrRAVaHxjENMFX48hsQfMzfE9b4yGzrM"
   my_cse_id = "e55bb4d3e100ee347"
   speech = gTTS(text = kata, lang=language, slow=False)
   speech.save("kata.mp3")
   os.system("mpv kata.mp3")
   os.system('clear')
   value=input(Fore.CYAN + "Masukkan Kata kunci pencarian anda : ")
   jumlah=input(Fore.CYAN + "jumlah result : ")
   def wiki_ono_search(search_term, api_key, cse_id, **kwargs):
       service = build("customsearch", "v1", developerKey=api_key)
       res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
       return res['items']

   results = wiki_ono_search(value, my_api_key, my_cse_id, num=jumlah)

   for result in results:
       '''pprint.pprint(result)'''
       title = result['title']
       link = result['formattedUrl']
       dis = result['snippet']
       print (title)
       print (dis)
       print (Fore.RED + link)
       def web():
           web = input(Fore.CYAN + "buka link kah (y/t)?")
           if web == 'y':
              os.system('xdg-open' + ' '+ link + '')
       hasil = dis
       speech = gTTS(text = hasil, lang=language, slow=False)
       speech.save("hasil.mp3")
       os.system("mpv hasil.mp3")
       os.system('clear')
       speech = gTTS(text = buka, lang=language, slow=False)
       speech.save("buka.mp3")
       os.system("mpv buka.mp3")
       os.system('clear')
       web()
def brainly():
   my_api_key = "AIzaSyBzrRAVaHxjENMFX48hsQfMzfE9b4yGzrM"
   my_cse_id = "fe2f6d6d7ec5b0dbd"
   speech = gTTS(text = kata, lang=language, slow=False)
   speech.save("kata.mp3")
   os.system("mpv kata.mp3")
   os.system('clear')
   value=input(Fore.CYAN + "Masukkan Kata kunci pencarian anda : ")
   jumlah=input(Fore.CYAN + "jumlah result : ")
   def brainly_search(search_term, api_key, cse_id, **kwargs):
       service = build("customsearch", "v1", developerKey=api_key)
       res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
       return res['items']

   results = brainly_search(value, my_api_key, my_cse_id, num=jumlah)

   for result in results:
       '''pprint.pprint(result)'''
       title = result['title']
       link = result['formattedUrl']
       dis = result['snippet']
       print (title)
       print (dis)
       print (Fore.RED + link)
       def web():
           web = input(Fore.CYAN + "buka link kah (y/t)?")
           if web == 'y':
              os.system('xdg-open' + ' '+ link + '')
       hasil = dis
       speech = gTTS(text = hasil, lang=language, slow=False)
       speech.save("hasil.mp3")
       os.system("mpv hasil.mp3")
       os.system('clear')
       speech = gTTS(text = buka, lang=language, slow=False)
       speech.save("buka.mp3")
       os.system("mpv buka.mp3")
       os.system('clear')
       web()
def error():
   menu()
def menu():
    os.system('clear')
    print ("")
    print ("")
    print (Fore.RED + " / \ / \ / \ / \ / \ / \ " +Fore.WHITE + "  / \ / \ / \ / \ / \ / \ ")
    print (Fore.RED + "( S | E | A | R | C | H )" +Fore.WHITE + " ( E | N | G | I | N | E )")
    print (Fore.RED + " \_/ \_/ \_/ \_/ \_/ \_/  " +Fore.WHITE + " \_/ \_/ \_/ \_/ \_/ \_/ ")
    print (Fore.BLUE + "				by mr_dilz v1")
    print ("")
    speech = gTTS(text = credit, lang=language, slow=False)
    speech.save("credit.mp3")
    os.system("mpv credit.mp3")
    os.system('clear')
    speech = gTTS(text = ada, lang=language, slow=False)
    speech.save("menu.mp3")
    os.system("mpv menu.mp3")
    os.system('clear')
    speech = gTTS(text = rayu, lang=language, slow=False)
    speech.save("rayu.mp3")
    os.system("mpv rayu.mp3")
    os.system('clear')
    print (Fore.YELLOW + "1 search pengetahuan wiki.")
    print (Fore.GREEN + "2 search pengetahuan google.")
    print (Fore.MAGENTA + "3 search pertanyaan apa aja.")
    print (Fore.CYAN + "4 search pengetahuan pak onno center.")
    menu = input(Fore.RESET + "hayu mau pilih yang mana? : ")
    
    if menu == '1':
       wiki()
       tanya()
    elif menu == '2':
       google()
    elif menu == '3':
       brainly()
    elif menu == '4':
       wiki_ono()
    else:
       error()
def tanya():
    tanya = input(Fore.CYAN + "Kembali ke menu (y/t)?")
    if tanya == 'y':
        os.system('clear')
        menu()
    elif tanya == 't':
        os.system('clear')
        exit
    elif tanya == '':
        os.system('clear')
        error()
menu()
tanya()
