from pytube import YouTube, Playlist
from tqdm import tqdm 
import os 
import json 
import time 


def download_audio(vid, title, dest_folder): 
    filenames = os.listdir(dest_folder)
    audio_location = dest_folder + title + ".mp4"
    if audio_location in filenames:
        return audio_location 

    vid.streams.filter(only_audio=True).first().download(dest_folder)
    return audio_location

def clean_title(title): 
    bracket_pos = title.rfind('[')
    if bracket_pos != -1:
        # if '[' is found, remove everything after it (including the '[' character itself)
        title = title[:bracket_pos].strip()
    return title 

def extract_title(url):
    ''' Tries to get around random bug in extracting video data. 
    https://github.com/pytube/pytube/issues/1473
    '''
    vid = YouTube(url)
    while True:
        try:
            title = vid.title
            title = title.replace("?", "") # remove question marks as this is automatically deleted by PyTube when downloading files 
            title = title.replace("$", "") # remove dollar sign
            return title 
        except:
            print("Retrying extraction of title")
            time.sleep(0.1)
            vid = YouTube(url)
            continue

def download_ytaudio(urls): 
    # Update initial metadata file instead of overwriting it 
    if os.path.exists('./data/metadata.json'):
        with open('./data/metadata.json') as f: 
            metadata_list = json.load(f)
    else: 
        metadata_list = []

    initial_urls = [item["url"] for item in metadata_list]
        
    for url in tqdm(urls): 
        vid = YouTube(url)
        title = extract_title(url)
        audio_location = download_audio(vid, title, "./data/audio_files/") # download audio files 

        metadata_dict = {
            "url": url, 
            "title": clean_title(title), 
            "audio_location": audio_location   
        }

        if metadata_dict["url"] not in initial_urls: 
            metadata_list.append(metadata_dict)
            initial_urls.append(url) # prevent duplicates 

        # Continuously update metadata.json
        with open('./data/metadata.json', 'w', encoding ='utf8') as f:
            json.dump(metadata_list, f, ensure_ascii=False)


if __name__ == "__main__": 
    # urls = []
    urls = Playlist("https://www.youtube.com/watch?v=5ywZibui2Jc&list=PLpo30qPT9yc4YW3_-8-7IZ5oUiSlxXdSz")
    download_ytaudio(urls)
    