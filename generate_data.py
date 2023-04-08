"""
Consolidate all transcripts into one single JSON file 
"""
import os 
import json 
from pytube import Playlist
from data.download_ytaudio import download_ytaudio
from model.transcribe import transcribe
from model.clean_transcripts import clean_transcripts

transcripts_folder = "./cleaned_transcripts/"
transcripts_filenames = ["./cleaned_transcripts/" + f for f in os.listdir(transcripts_folder)]

def summarise(text): 
    return "This is a placeholder summary text."

def generate_data(): 
    final_data = []

    with open('./data/metadata_v2.json') as f: 
        metadata = json.load(f)

    for id, vid in enumerate(metadata): 
        vid_dict = {}

        transcript_loc = vid["transcript_location"]
        transcript_loc = transcript_loc.replace("transcripts", "cleaned_transcripts")
        
        with open(transcript_loc) as f: 
            transcript = json.load(f)

        content = summarise(transcript["text"])
        
        vid_dict = {
            "id": str(id+1), 
            "title": vid["title"],
            "url": vid["url"], 
            "content": content
        }
        vid_dict["transcript"] = {}
        
        for line in transcript["segments"]: 
            start = str(round(line["start"], 2))
            vid_dict["transcript"][start] = line["text"].strip()

        final_data.append(vid_dict)
    
   
    final_dict = {"posts": final_data} 

    with open("./src/data.json", 'w', encoding ='utf8') as f:
        json.dump(final_dict, f, allow_nan=False)

if __name__ == "__main__": 
    # urls = []
    urls = Playlist("https://www.youtube.com/watch?v=5ywZibui2Jc&list=PLpo30qPT9yc4YW3_-8-7IZ5oUiSlxXdSz")
    print("---Downloading Audio Files---")
    download_ytaudio(urls)
    print("---Transcribing---")
    transcribe()
    clean_transcripts()
    generate_data()

    