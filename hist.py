import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ページのタイトル設定
st.set_page_config(
    page_title="histogram",
)

# csv読み込み
df0 = pd.read_csv('test.csv', index_col=0)

# セッション情報の初期化
if "page_id" not in st.session_state:
    st.session_state.page_id = -1
    st.session_state.df0 = df0

# 各種メニューの非表示設定
hide_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_style, unsafe_allow_html=True)

# 最初のページ
def main_page():
    st.markdown(
        "<h1 style='text-align: center;'>ヒストグラム表示</h1>",
        unsafe_allow_html=True,
    )

    shop_list=['A',"B","C","D","E","F","G","H","I","J"]
    Day_list=["2020/03/31","2020/04/01","2020/04/02","2020/04/03","2020/04/04","2020/04/05","2020/04/06"]
    shop_list_selector=st.sidebar.selectbox( "ショップ選択",shop_list)
    Day_list_selector=st.sidebar.selectbox( "日時選択",Day_list)

    hist_array=[]
    top5=[]
    day5=[]


    for i in range(7):
        hist_array.append(st.session_state.df0[shop_list_selector][i])

    top=st.session_state.df0.sort_values(shop_list_selector,ascending=False)[:5][shop_list_selector]

    #for i in range(5):
        #top5.append(top[1][i])
        #day5.append(top[0][i])

    shop_list_top5=st.session_state.df0.iloc[0]
    shop_list_top5=shop_list_top5[:5]

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    ax1.hist(hist_array,bins=4)
    #ax2.bar(top5,top5)

    st.pyplot(fig1)
    st.pyplot(fig2)

    #st.text([top5[1]])
    #st.text(st.session_state.df0)
    #st.text(st.session_state.df0.at[Day_list_selector,shop_list_selector])

# ページ判定
if st.session_state.page_id == -1:
    main_page()
