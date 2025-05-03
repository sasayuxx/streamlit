import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('Interative Widgets')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラムです')

expander1 = st.expander('問合せ1')
expander1.write('問合せ1の回答')
expander2 = st.expander('問合せ2')
expander2.write('問合せ2の回答')
expander3 = st.expander('問合せ3')
expander3.write('問合せ3の回答')

# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は', text, 'です'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition
# option = st.selectbox(
#   'あなたが好きな数字を教えてください',
#   list(range(1, 11))
# )
# 'あなたの好きな数字は', option, 'です'

# img = Image.open('つばくろう_hanochin.png')

# st.image(img, caption='tsubakurou', use_container_width =True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/(50, 50) + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# df

# st.map(df)

# st.table(df.style.highlight_max(axis=0))
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)


