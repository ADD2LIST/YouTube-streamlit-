

import streamlit as st

from pytube import YouTube

import moviepy.editor as mp

import os

def main():

    st.title("YouTube Video Downloader")

    # Get the YouTube video URL from the user

    video_url = st.text_input("Enter YouTube video URL:")

    if video_url:

        try:

            # Download the YouTube video

            st.text("Downloading video...")

            yt = YouTube(video_url)

            video = yt.streams.get_highest_resolution()

            video_file = video.default_filename

            # Download the video

            video.download(filename=video_file)

            # Convert the video to MP3 format

            st.text("Converting video to MP3...")

            mp3_file = os.path.splitext(video_file)[0] + ".mp3"

            clip = mp.VideoFileClip(video_file)

            clip.audio.write_audiofile(mp3_file)

            clip.close()

            # Provide download link to the MP3 file

            st.success("Video downloaded successfully!")

            st.audio(mp3_file, format='audio/mp3')

            # Provide download link to the video file

            st.text("Download video file:")

            st.download_button(label="Download", data=open(video_file, 'rb'), file_name=video_file)

            # Clean up downloaded files

            os.remove(video_file)

            os.remove(mp3_file)

        except Exception as e:

            st.error("An error occurred: " + str(e))

if __name__ == "__main__":

    main()


        

   



        

   
