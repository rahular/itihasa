import os
import sys
import json

ROOT_DIR = "./gen"
kandas = ["Bala Kanda", "Ayodhya Kanda", "Aranya Kanda", "Kishkinda Kanda", "Sundara Kanda", "Yuddha Kanda", "Uttara Kanda"]

def read(path):
    with open(path, "r") as f:
        return json.load(f)

def write_vol_index(text, data):
    html = f"<h2>{text.capitalize()}</h2>\n"
    for vol in data.keys():
        html += f"<a href='{vol}/index.html'>{vol}</a><br />\n"
    with open(os.path.join(ROOT_DIR, text, "index.html"), "w") as f:
        f.write(html)

def write_chapter_index(text, data):
    kid = -1
    for vol in data.keys():
        html = f"<h2>{text.capitalize()} - {vol}</h2>\n"
        vpath = os.path.join(ROOT_DIR, text, vol)
        os.makedirs(vpath, exist_ok=True)
        for idx, obj in enumerate(data[vol]):
            if text == "ramayana":
                if obj["chapter"] == "1":
                    kid += 1
                chapter_name = f"{kandas[kid]}: Chapter {obj['chapter']}"
            elif text == "mahabharata":
                chapter_name = f"{obj['parva']}: Chapter {obj['chapter']} - {obj['description']}"
            html += f"<a href='{idx+1}.html'>{chapter_name}</a><br />\n"
        with open(os.path.join(vpath, "index.html"), "w") as f:
            f.write(html)

def write_shlokas(text, data):
    kid = -1
    for vol in data.keys():
        for idx, obj in enumerate(data[vol]):
            if text == "ramayana":
                if obj["chapter"] == "1":
                    kid += 1
                html = f"<h3>{kandas[kid]}: Chapter {obj['chapter']}</h3>"
            elif text == "mahabharata":
                html = f"<h3>{obj['parva']}: Chapter {obj['chapter']}</h3><h4>{obj['description']}</h4>"
            for aid, (s, t) in enumerate(zip(obj["sn"], obj["en"])):
                html += f"<p id='{aid+1}'><a href='#{aid+1}'></a>{s}<br />{t}</p>\n"
            with open(os.path.join(ROOT_DIR, text, vol, f"{idx+1}.html"), "w") as f:
                f.write(html)


def main(text):
    assert text in ["ramayana", "mahabharata"], f"Invalid option: {text}"
    os.makedirs(os.path.join(ROOT_DIR, text), exist_ok=True)
    data = read(f"./res/{text}.json")
    write_vol_index(text, data)
    write_chapter_index(text, data)
    write_shlokas(text, data)


if __name__ == "__main__":
    main(sys.argv[1])