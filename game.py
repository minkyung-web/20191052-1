import json

def set_charact(name):
    character = {
        "이름" : name,
        "가게" : "집게리아",
        "메뉴" : ["햄버거", "아이스크림", "감자튀김"]
    }
    
    with open("static/save.txt", "w", encoding='utf-8') as f:
        json.dump(character, f, ensure_ascii = False, indent=4)
    print(character)
    return character


def save_game(filename, charact):
    f = open(filename, "w", encoding="utf-8")
    for key in charact:
        print("%s:%s" % (key, charact[key]))
        f.write("%s:%s\n" % (key, charact[key]))
    f.close()