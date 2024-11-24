import streamlit as st
import requests
st.title("Xmas quiz submission :santa:")

"""Hi there,
Thank you for joining us. You are already aware of the emails that inform you of the question. This quiz operates differently; the correct answer is not necessarily the right one, as you could really easily cheat. Instead, the correct answer is the one that most people choose, so majority rules apply. This is the only quiz with DEMOCRACY, LIBERTY, AND FREEDOM (even if the majority is wrong).
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