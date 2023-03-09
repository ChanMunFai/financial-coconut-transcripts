urls = []

if __name__ == ""__main__": 
    pass 
    for url in urls: 
        transcribe(url)
        init_transcripts2json()
        summarise()
        final_transcripts2json()

    for file in final_data: 
        combine_json_files()