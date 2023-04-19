# The Financial Coconut Transcript

In this project, I design a website where users can access transcripts of a popular podcast on financial literacy in Singapore - The Financial Coconut. Note that I am in no way affilated to the podcast and I do not receive any commercial benefits from this. This is purely a hobbyist exercise. 

### Transcription
Transcripts were generated using an opensource speech-to-text model called Whisper by OpenAI. Specifically, I finetuned Whisper on Singaporean-accented English to further improve performance. To learn more about the finetuning, please visit this [repo](https://github.com/ChanMunFai/Whisper_SG). 

Features that I have included: 
* Search function 
* Summarisation 

### Summarisation 
I attempted to use AI to generate summaries as well. This turns out to be a highly challenging problem (I mean, if humans struggle with summarisation, it's no surprise that machines do as well). I found that [Langchain](https://python.langchain.com/en/latest/index.html) and a powerful Large Language Model (LLM) that can be run locally does the job decently. Specifically, I was able to run the [Koala 7b-8bit](https://bair.berkeley.edu/blog/2023/04/03/koala/) model on my personal RTX 3090 Ti. 

There are some errors with the transcriptions and especially the summaries. I did not edit them as I like to highlight both the good and bad of AI systems though better results can be expected with more finetuning and prompting. I apologise to the owners and guests of The Financial Coconut podcast for any inaccuracies portrayed here. 

