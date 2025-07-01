import streamlit as st
from PIL import Image
import random
import pandas as pd
import altair as alt

# --- Page Setup ---
st.set_page_config(page_title="💀 Degen Card Generator", page_icon="💀", layout="wide")

# --- Card Definitions ---
card_files = {
    "🔮 1": "Deleteit.png",
    "🔮 2": "Hodl.png",
    "🔮 3": "Fukwrong.png",
    "💣 4": "Mahnigga.png",
    "🎲 Random": "Surprise_mf.png"
}
label_names = {
    "🔮 1": "🪼 Delete This Nephew",
    "🔮 2": "🚩 Bitch Hodl On",
    "🔮 3": "😐 F*ck's Wrong With You",
    "💣 4": "🪡 Mah Nigga",
    "🎲 Random": "🎴 Surprise Muthafuka"
}

# --- Session State ---
if "selected_label" not in st.session_state:
    st.session_state.selected_label = label_names["🎲 Random"]
if "selected_card" not in st.session_state:
    st.session_state.selected_card = card_files["🎲 Random"]

# --- CSS Styling ---
st.markdown("""
<style>
[data-testid="stImage"] img {
    max-height: 460px;
    object-fit: contain;
}
.caption-style {
    text-align: center;
    font-size: 0.9rem;
    color: #ccc;
    margin-top: 0.5rem;
}
.button-row {
    display: flex;
    justify-content: center;
    gap: 0.75rem;
    flex-wrap: wrap;
    margin-top: 10px;
}
.button-row button {
    font-size: 0.9rem;
    padding: 0.3rem 0.8rem;
}
</style>
""", unsafe_allow_html=True)

# --- Main Header ---
st.markdown("<h1 style='text-align: center; font-size: 3rem;'>💀 Degen Card Generator</h1>", unsafe_allow_html=True)
st.markdown(
    f"<h3 style='text-align: center;'>🔹 Your Meme Form: <span style='color: white'>{st.session_state.selected_label}</span></h3>",
    unsafe_allow_html=True
)

# --- MAIN VIEW: MEME | STATS | CHART ---
card_col, stats_col, chart_col = st.columns([2.2, 1.5, 3])

# LEFT: Meme Card
with card_col:
    try:
        st.image(Image.open(st.session_state.selected_card), use_container_width=True)
        st.markdown("<div class='caption-style'>With this card, you can surprise a muthafuka.</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading image: {e}")

# MIDDLE: Stats
with stats_col:
    st.markdown("<h4 style='text-align: center;'>📊 Stats</h4>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.metric(label="🔪 Degens Unleashed", value=f"{random.randint(420, 6666)}")
    st.metric(label="🧠 Memes Consumed", value=f"{random.randint(10000, 99999)}")
    st.metric(label="🤡 Cringe Index", value=f"{random.randint(85, 100)}%", delta="+69%")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; font-size:0.85rem; color:#aaa;'>Stats are fake. Just like your portfolio.</div>", unsafe_allow_html=True)

# RIGHT: Chart
with chart_col:
    st.markdown("### 📈 Cringe Momentum")
    data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Cringe Level": [random.randint(60, 100) for _ in range(7)]
    })
    chart = alt.Chart(data).mark_line(point=True).encode(
        x="Day",
        y=alt.Y("Cringe Level", scale=alt.Scale(domain=(50, 110))),
        tooltip=["Day", "Cringe Level"]
    ).properties(
        height=300,
        title="Cringe Momentum This Week"
    )
    st.altair_chart(chart, use_container_width=True)

# --- SECTION 2: Try Your Luck Buttons ---
st.markdown("<br><br><h4 style='text-align: center;'>🎯 Try Your Luck</h4>", unsafe_allow_html=True)

with st.container():
    cols = st.columns([1, 1, 1, 1, 1], gap="medium")
    for i, (btn_label, img_file) in enumerate(card_files.items()):
        with cols[i]:
            if st.button(btn_label, use_container_width=True):
                st.session_state.selected_card = img_file
                st.session_state.selected_label = label_names[btn_label]
