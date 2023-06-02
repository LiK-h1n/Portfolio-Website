from streamlit import header, form, form_submit_button, text_input, text_area, info
from send_email import send_email

header("Contact Me")

with form("Send Email", True):
    user_email = text_input("Your email address")
    raw_message = text_area("Your message")
    message = f"Subject: New email from {user_email}\n\nFrom: {user_email}\n\n{raw_message}"
    button = form_submit_button("SUBMIT")
    if button:
        send_email(message)
        info("Your email has been sent successfully.")
