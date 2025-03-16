import streamlit as st

def meme_display():
    # Set the expander
    with st.expander("Meme"):
        # Set the subheader
        st.subheader("Siguiente")

        # Display the image
        st.image("components/meme/imgs/meme3.png", caption="Meme Image", use_column_width=True)