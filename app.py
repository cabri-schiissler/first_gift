import streamlit as st

st.set_page_config(page_title="Happy 6 Months 💖", layout="centered")

st.markdown("<h1 style='text-align: center; color: hotpink;'>💘 Happy 6 Month Anniversary! 💘</h1>", unsafe_allow_html=True)

st.image([
    "https://raw.githubusercontent.com/cabri-schiissler/first_gift/main/pic1.jpg",
    "https://raw.githubusercontent.com/cabri-schiissler/first_gift/main/pic2.jpg",
    "https://raw.githubusercontent.com/cabri-schiissler/first_gift/main/pic3.jpg"
], width=250)

st.markdown("""
<div style='text-align: center; font-size: 20px; color: #c71585;'>
I am so happy I met you!.<br>
Thank you for everything<br>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🎵 Press play to hear our song")
st.video("https://www.youtube.com/watch?v=Uc12NL0HN7w&list=RDUc12NL0HN7w&start_radio=1")


if st.button("Click here 💝"):
    st.balloons()
    st.success("I miss you. 💘")
