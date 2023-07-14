from streamlit import image, columns, title, write, set_page_config, header
from pandas import read_csv

set_page_config("Portfolio Website", layout="wide", initial_sidebar_state="collapsed")

col_1, col_2 = columns(2)
with col_1:
    image("images/photo.jpeg", width=300)
with col_2:
    title("Nikhil Idiculla")
    content_1 = "Passionate Python programmer with a drive to create innovative solutions and explore the endless " \
                "possibilities of code, fueled by a deep curiosity and a love for elegant problem-solving."
    write(content_1)

content_2 = "Below you can find some of the apps I have built in Python. Feel free to contact me"
write(content_2)

col_3, empty_col, col_4 = columns([1.5, 0.5, 1.5])
df = read_csv("data.csv", sep=";")
for index, row in df.iterrows():
    if index % 2 == 0:
        with col_3:
            header(row["title"])
            write(row["description"])
            image(f"images/{row['image']}")
            write(f"[Source Code]({row['url']})")
    else:
        with col_4:
            header(row["title"])
            write(row["description"])
            image(f"images/{row['image']}")
            write(f"[Source Code]({row['url']})")
