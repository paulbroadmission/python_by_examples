import webbrowser
import requests
from bs4 import BeautifulSoup
from gtts import gTTS

def get_hotline_udnnews(url):
    resp = requests.get(url)
    
    if resp.status_code is 200:
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
        scope1 = soup.select("#tab1") 
        scope2 = scope1[0].select(".taba")
        
        hot_lines = []
        
        for line in scope2:
            hot_lines.append(line.text)
            
        return hot_lines

def translate_text_to_speech(text):
    if text is not None:
        tts=gTTS(text, lang='zh')
        print(text)
        tts.save("news.mp3")

if __name__ == '__main__':
    udnnews_lines = get_hotline_udnnews("https://udn.com/news/index")
    i = 0
    udnnews_dicts = {}
    while i < len(udnnews_lines):
        udnnews_dicts['time'] = udnnews_lines[i][:5]
        udnnews_dicts['title'] = udnnews_lines[i][5:]
        #print("Time[{}]: {}".format(udnnews_dicts['time'], udnnews_dicts['title']))
        i += 1
    
    all_lines =""
    for line in udnnews_lines:
        all_lines += " "+str(line[5:])
    #print(all_lines)
    
    translate_text_to_speech(str(all_lines))
    webbrowser.open("news.mp3")