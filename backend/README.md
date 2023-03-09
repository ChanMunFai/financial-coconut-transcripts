This is the backend for transcribing Youtube videos. 

General steps are: 
1. Load model and transcribe audio file 
2. Format transcriptions into correct JSON format 
3. Summarise transcriptions using AI
4. Format summaries + transcriptions into correct JSON format 
5. Compile all final JSON files into 1 big JSON file 

Possible post-processing steps: 
1. Cleaning up of video title 

Things to think about 
1. How to label each video? Do we use the url even though it is distinct (however, it is too ugly)
    - Or do we want to use an ID for each video? We can then keep track of each video's ID, using a dictionary --> is this too complicated? 
2. How to ensure that a transcribed video does not get transcribed again? 

Things to experiment about 
- Docker??