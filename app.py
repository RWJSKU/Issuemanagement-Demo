# 設置應用標題
st.title("客戶問題管理系統 Demo")

# 設置側邊欄
st.sidebar.title("功能選單")
page = st.sidebar.radio("選擇頁面", ["數據總覽", "問題統計", "AI 問題預測"])

# 定義每個頁面的內容
if page == "數據總覽":
    st.header("所有問題記錄")
    st.write("這裡會顯示所有問題數據的概覽。")

elif page == "問題統計":
    st.header("統計分析")
    st.write("這裡會顯示問題的統計圖表和數據分析。")

elif page == "AI 問題預測":
    st.header("AI 問題預測")
    st.write("這裡展示如何利用數據進行問題預測。")
