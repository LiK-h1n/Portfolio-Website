from streamlit import header, form, form_submit_button, text_input, text_area

header("Contact Me")

with form("Send Email", True):
    user_email = text_input("Your email address")
    message = text_area("Your message")
    form_submit_button("SUBMIT")
