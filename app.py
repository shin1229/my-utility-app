import streamlit as st
import pandas as pd
from datetime import datetime

# アプリのタイトル
st.set_page_config(page_title="My Quick Utility", layout="centered")
st.title("🚀 5分で動く！便利メモ帳")

# セッション状態の初期化（データを保持するため）
if 'notes' not in st.session_state:
    st.session_state.notes = []

# 入力エリア
with st.form("my_form", clear_on_submit=True):
    task = st.text_input("ここにメモやタスクを入力")
    category = st.selectbox("カテゴリ", ["仕事", "個人", "買い物", "その他"])
    submitted = st.form_submit_button("保存する")
    
    if submitted and task:
        new_note = {
            "日付": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "内容": task,
            "カテゴリ": category
        }
        st.session_state.notes.append(new_note)
        st.success("保存しました！")

# データの表示
if st.session_state.notes:
    df = pd.DataFrame(st.session_state.notes)
    st.divider()
    st.subheader("📝 保存済みリスト")
    st.dataframe(df, use_container_width=True)
    
    # CSVとしてダウンロード（ユーティリティ機能）
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("CSVで保存", csv, "my_notes.csv", "text/csv")
    
    if st.button("全データを消去"):
        st.session_state.notes = []
        st.rerun()
