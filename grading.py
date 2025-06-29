import streamlit as st



st.title('Student Grading System')

marks=st.number_input('Enter Obtained Marks',min_value=1)
total=st.number_input('Enter Total Marks',min_value=1)
percentage=marks/total*100
st.button('Claculate Result')
st.subheader(f'Your Percentage:,:blue[{percentage}%]')


if percentage>=80:
    st.success('Excellent')
elif percentage>=60 and percentage<=80:
    st.info('pass')
else:
    st.error('Fail: Better luck next time')