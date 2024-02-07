import streamlit as st

def main():
    st.title("Contact Us")

    # Sidebar with additional information
    st.sidebar.header("Contact Information")

    st.sidebar.write("Buildwhiz@beyoudeveloper.com")
    st.sidebar.write("+1234567890")

    st.write("Feel free to reach out to us for any inquiries or feedback!")

    name = st.text_input("Name", "")
    email = st.text_input("Email", "")

    # Dropdown for inquiry type
    inquiry_type = st.selectbox("Inquiry Type", ["General Inquiry", "Support", "Feedback"])

    message = st.text_area("Message", "")

    if st.button("Submit"):
        if name.strip() == "":
            st.warning("Please enter your name.")
        elif "@" not in email or "." not in email:
            st.warning("Please enter a valid email address.")
        elif inquiry_type == "":
            st.warning("Please select an inquiry type.")
        elif message.strip() == "":
            st.warning("Please enter your message.")
        else:
            # Here you can add code to handle the submission of the contact form
            # For demonstration purposes, printing the details
            st.success("Message sent successfully!")
            st.write(f"Name: {name}")
            st.write(f"Email: {email}")
            st.write(f"Inquiry Type: {inquiry_type}")
            st.write(f"Message: {message}")

if __name__ == "__main__":
    main()
