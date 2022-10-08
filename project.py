import streamlit as st
import pandas as pd

st.title("App to visualize water levels")

def main():
    uploaded_file = st.file_uploader("Choose a csv file to visualize")
    if uploaded_file:
        df = pd.read_csv(uploaded_file, header=0, sep=';', index_col=0)
        # st.write('Head of the uploaded dataframe:')
        st.header("Data processing and visualization")
        st.write("Here is description of my dataset. Dataframe shows differneces in water level of an uploaded file. A bit more text and so on. I just wanted to go to the second line.:coffee::ocean::pig:")
        pd.to_datetime(df.index)
        
        
        left_column, padding, right_column = st.columns((20,1,10))
        
        with left_column:
            st.write("**Original dataframe:**")
            table = st.dataframe(df.iloc[:20,:])
        with right_column:
            df['diff'] = df['Poziom wody_original'] - df['Poziom wody_adjusted']
            df_diff = df[df['diff'] != 0]['diff']
            st.write("**Water level difference:**")
            st.dataframe(df_diff)
        
        length = df.shape[0]
        st.header("Water level original:")
        st.line_chart(df.iloc[:int(length/38),0])
        

        st.header("Download data:")
        st.write("CSV file with water level differences.:bomb::file_folder::+1:")
        new_df = df.iloc[:,1]
        csv_data = df_diff.to_csv().encode('utf-8')
        st.download_button(
            label="Download data as CSV",
            data=csv_data,
            file_name='water_level_difference.csv',
            mime='text/csv',
        )
password_placeholder = st.empty()
password = password_placeholder.text_input('Enter password', type='password')
if password == 'arup':
    password_placeholder.empty()
    main()