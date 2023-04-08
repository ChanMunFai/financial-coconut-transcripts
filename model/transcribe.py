import whisper 
import json 
import time 
import os 
from tqdm import tqdm 
# import torch 

def load_model(model_name="large"): 
    if model_name == "large": 
        model=whisper.load_model("large")

    # checkpoint_path = "./checkpoints/checkpoint-epoch=0004.PT"
    # state_dict = torch.load(checkpoint_path)
    # model.load_state_dict(state_dict)
    return model 

def transcribe(model, audio_file, output_file): 
    st = time.time()
    result=model.transcribe(audio_file, language = "en")
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    with open(output_file, 'w', encoding ='utf8') as f:
        json.dump(result, f, allow_nan=False)

def extract_title(file_path):
    # Get just the filename without the extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    bracket_pos = file_name.rfind('[')
    if bracket_pos != -1:
        title = file_name[:bracket_pos].strip()
    title = title.replace("?", "") # remove question marks for consistency
    return title

def transcribe(model_name="large"): 
    model = load_model(model_name)
    audio_folder = "./data/audio_files"
    metadata = "./data/metadata.json"
    
    with open(metadata) as f: 
        data = json.load(f)

    transcribed_files = ['./transcripts/' + i for i in os.listdir('./transcripts/')]

    for vid in tqdm(data): 
        audio_file = vid["audio_location"]
        title = extract_title(audio_file)
        transcript_file = './transcripts/' + title + '.json'
        vid["transcript_location"] = transcript_file

        # Start Transcript 
        if transcript_file not in transcribed_files: 
            print(f"Transcribing into {transcript_file}...")
            transcribe(model, audio_file, transcript_file)

    with open('./data/metadata_v2.json', 'w', encoding ='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    

if __name__ == "__main__": 
    transcribe()
    


    
        



