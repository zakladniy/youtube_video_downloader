"""Module with get preview of video page"""
import streamlit as st

from src.utils import get_preview_image

st.title("Get video preview")

# Fields
youtube_link_col, button_col, preview_col = st.columns(3)
with youtube_link_col:
    youtube_url = st.text_area("YouTube video url")
with button_col:
    preview_button = st.button("Get video preview")

# Button action
if youtube_url is not None:
    with button_col:
        if preview_button:
            image = get_preview_image(youtube_url)
            with preview_col:
                st.image(image, caption="Video preview")
