# About

This site is created by [Chan Mun Fai](https://chanmunfai.github.io) and is unaffilated to the Financial Coconut Podcast. This is purely a hobbyist project with no commercial interests. I do not have any intentions to monetise this project in the future. 

### Transcription
Inspired by Aleska Gordic and Lex Friedman, this is my attempt in building a full-stack ML project. On the backend, I used OpenAI's [Whisper](https://openai.com/research/whisper) (speech-to-text) model to transcribe videos from the Financial Coconut Podcast. 

However, noticing the peculiarities of the Singaporean-accented English, I first *finetuned my model on 800 GB** of Singaporean-accented English, attaining an improvement in the error rate from 13% to 6%. More training details can be found in this [repository](https://github.com/ChanMunFai/Whisper_SG). 

### Summarisation 
I also decided to use AI to generate summaries. This turns out to be more challenging than I thought. First, the 'traditional' summarisation models will not work without additional prompts. The podcasts are in a first-persion point of view and it is difficult for the model to understand what is going on without giving it some additional context such as *"This is a podcast on fiancial literacy...*

This problem remains true even with the more modern and sophisticated LLMs. Specifically, I ended up using the [Koala 7b-8bit model](https://bair.berkeley.edu/blog/2023/04/03/koala/) as it turned out to be really smart and could fit nicely into my 24GB RTX 3090Ti. I also tried using Cohere's API but found the development (free trial) API to be too restrictive and the results not that ideal. 

#### Langchain
[Langchain](https://python.langchain.com/en/latest/index.html) is extremely powerful and the sky (or compute) seems to be the limit with this tool. For summarisation, Langchain offers 2 wonderful tools: 

1. Custom prompts
2. Map_reduce

I will discuss more on custom prompts in the section below, but 'map_reduce' basically works by chunking the document into separate passages. The model then summarises each individual chunk before recursively summarising the summaries of chunks. Essentially, this reduces the amount of memory needed to generate a summary. 
#### Prompt Engineering 
When I used the standard summarisation prompt, Koala had a tendency to hallucinate, often talking about things that were not at all remotely present. After much trial and error, I figured that the summaries tend to be a lot better if the model already knows what the title of the episode is. It also has to be prompted not to make up facts that are not in the transcript. 

The prompt that I use is: 

```
"""This is a podcast series on financial literacy in Singapore. It is called The Financial Coconuts.\n 

The title for this episode is:  

{title} \n 

Write a concise summary of the podcast: 

{text}\n

Only include facts from the context. \n 

CONCISE SUMMARY:"""
```

In general, there does appear to be some errors with the accuracy and at times formatting of the summary. One will notice that the model often assigns names to the podcasts hosts even when they are unknown. Future work will involve editing these mistakes automatically using an LLM as well. 