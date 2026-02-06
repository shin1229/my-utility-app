mport streamlit as st
import pandas as pd
from datetime import datetime

st.title("🚀 5分で動く！便利メモ帳")

if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.form("my_form", clear_on_submit=True):
    task = st.text_input("ここにメモやタスクを入力")
    category = st.selectbox("カテゴリ", ["仕事", "個人", "買い物", "その他"])
    submitted = st.form_submit_button("保存する")

    if submitted and task:
        new_note = {"日付": datetime.now().strftime("%Y-%m-%d %H:%M"), "内容": task, "カテゴリ": category}
        st.session_state.notes.append(new_note)
        st.success("保存しました！")

if st.session_state.notes:
    df = pd.DataFrame(st.session_state.notes)
    st.dataframe(df, use_container_width=True)
