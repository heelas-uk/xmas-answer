import streamlit as st
import requests
st.title("Xmas quiz submission :santa:")

"""Hi there,
Thank you for joining us. This quiz isn't about getting the right answer, it's about choosing the most popular answer.
 """





def submit_data():
    name = st.text_input("Name")
    day = st.number_input("Day", min_value=1, max_value=500)
    answer = st.text_input("Answer:")

    if st.button("Submit"):
        url = "https://heelas.uk/save_data.php"
        data = {
            "name": name,
            "day": day,
            "answer": answer
        }

        response = requests.post(url, data=data)

        if response.status_code == 200:
            st.success("Data sent successfully!")
        else:
            st.error("Error sending data:", response.text)

if __name__ == "__main__":
    submit_data()