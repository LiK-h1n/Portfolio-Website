from streamlit import image, columns, title, write, set_page_config

set_page_config(layout="wide")

col_1, col_2 = columns(2)

with col_1:
    image("images/photo.jfif")
with col_2:
    title("Nikhil Idiculla")
    content = "Passionate Python programmer with a drive to create innovative solutions and explore the endless " \
              "possibilities of code, fueled by a deep curiosity and a love for elegant problem-solving."
    write(content)
