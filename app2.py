import streamlit as st
import pandas as pd
import numpy as np

# 隨機生成與 5 部 IMDB 真實電影相關的樣本數據集
np.random.seed(42)
data = {
    'Movie': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Duration': np.random.randint(80, 180, 5),
    'IMDb Rating': np.random.uniform(5.0, 9.0, 5),
    'Genre': ['Action', 'Comedy', 'Drama', 'Thriller', 'Sci-Fi'],
    'Director': ['Director A', 'Director B', 'Director C', 'Director D', 'Director E'],
    'Box Office Gross': np.random.randint(1000000, 100000000, 5),
    'Number of Votes': np.random.randint(1000, 100000, 5),
    'Release Year': np.random.randint(2000, 2025, 5)
}
df = pd.DataFrame(data)

# 設定 Streamlit 應用程式標題
st.title('IMDB Movie Data Visualization')

# 在側邊欄中讓用戶選擇圖表類型
chart_type = st.sidebar.selectbox(
    'Select Chart Type',
    ('Scatter Chart', 'Bar Chart', 'Line Chart', 'Area Chart')
)

# 顯示數據表格
st.write('### Movie Dataset')
st.dataframe(df)

# 根據用戶選擇的圖表類型顯示相應的圖表
if chart_type == 'Scatter Chart':
    st.write('### Scatter Chart: Movie Duration vs IMDb Rating')
    st.write('This scatter chart shows the relationship between movie duration and IMDb rating.')
    st.scatter_chart(df[['Duration', 'IMDb Rating']])

elif chart_type == 'Bar Chart':
    category = st.sidebar.selectbox('Select Category', ('Genre', 'Director'))
    value = st.sidebar.selectbox('Select Value', ('Box Office Gross', 'Number of Votes'))
    st.write(f'### Bar Chart: {category} vs {value}')
    st.write(f'This bar chart shows the {value} for each {category}.')
    st.bar_chart(df.set_index(category)[value])

elif chart_type == 'Line Chart':
    y_axis = st.sidebar.selectbox('Select Y-Axis', ('IMDb Rating', 'Box Office Gross'))
    st.write(f'### Line Chart: Release Year vs {y_axis}')
    st.write(f'This line chart shows the {y_axis} over the release years.')
    st.line_chart(df.set_index('Release Year')[y_axis])

elif chart_type == 'Area Chart':
    st.write('### Area Chart: Release Year vs Box Office Gross')
    st.write('This area chart shows the box office gross over the release years.')
    st.area_chart(df.set_index('Release Year')['Box Office Gross'])