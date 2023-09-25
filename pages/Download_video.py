import streamlit as st

from utils import download_video

st.title("Download video")

# Fields
youtube_link_col, path_col, button_col, progress_col = st.columns(4)

with youtube_link_col:
    youtube_url = st.text_area("YouTube video url")
with path_col:
    video_path = st.text_area("Folder for video files")
with button_col:
    download_button = st.button("Download video")

# Button action
if youtube_url is not None and video_path is not None:
    with button_col:
        if download_button:
            with st.spinner("Please wait..."):
                try:
                    download_video(
                        video_folder=video_path,
                        youtube_url=youtube_url
                    )
                    st.success("Done!")
                except:
                    st.error("Download error")
