import openai
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

openai.api_key = OPENAIKEY

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content

def GetSubtitles(video_link):
    video_id = video_link[32:43]
    op = YouTubeTranscriptApi.get_transcript(video_id)
    op_use = TextFormatter.format_transcript(op,op)
    return op_use


st.title('Youtube Summary Generator')
st.subheader(
    'Works well on videos having length ~10 mins')

video_link = st.text_area("Enter Youtube Link 😁")


if st.button('Generate Summary'):
    with st.spinner('Getting Subtitles'):
        subtitles = GetSubtitles(video_link)
        st.success('Done!')
    with st.spinner('Generating Summary.....'):
        chatGPTPrompt = f"""if i write something inside curly braces, take them as instructions for that specific part. You are a professional summarizer, who watches youtube videos and summarizes them. You will be provided with subtitles of a youtube video, the video would be mostly educational one. What your work is to analyze the subtitles and provide me with detailed notes from the captions. The Notes Should be in Numbered points with a heading, then explanation, covering every point covered in the video. So that even if i don't watch the video, it is sufficient for me to get all the knowledge of the video. Remember to be extensive,provide full information and not to miss out on important info and use your intelligence also.You are not required to output anything except the notes. The notes should be in the format : 

[Title]

[Summary in Bullet Points]

[Conclusion - Not more than two or three lines]

Here are the subtitles : {subtitles}

"""
    
        analysis = BasicGeneration(chatGPTPrompt)
        st.text_area("Analysis", analysis,
                     height=500)
        st.success('Done!')








    
    

    
    







