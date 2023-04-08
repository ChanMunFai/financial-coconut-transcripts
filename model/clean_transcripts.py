import json 
import os 

def load_transcripts(filename): 
    with open(filename) as f: 
        data = json.load(f)

    return data 

def output_cleaned_transcripts(data, filename): 
    filename = filename.replace('transcripts', "cleaned_transcripts")
    with open(filename, 'w', encoding ='utf8') as f:
        json.dump(data, f, allow_nan=False)

def clean_indiv_transcript(filename): 
    data = load_transcripts(filename)
    
    text = data["text"]
    segments = data["segments"]

    cleaned_segments = []

    for segment in segments: 
        reduced_segment = {
            'start': segment['start'], 
            'end': segment['end'], 
            'text': segment['text']
        }

        cleaned_segments.append(reduced_segment)

    data = {
        "text": text, 
        "segments": cleaned_segments
    }

    output_cleaned_transcripts(data, filename)
    return 

def clean_transcripts(): 
    filenames = ["./transcripts/" + f for f in os.listdir("./transcripts/")]
    cleaned_filenames = ["./cleaned_transcripts/" + f for f in os.listdir("./cleaned_transcripts/")]
    
    for filename in filenames: 
        new_filename = filename.replace('transcripts', "cleaned_transcripts")
        if new_filename not in cleaned_filenames: 
            clean_indiv_transcript(filename)

if __name__ == "__main__": 
    clean_transcripts()
    
    