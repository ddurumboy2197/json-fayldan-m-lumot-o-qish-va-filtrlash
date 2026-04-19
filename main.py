import json

def oqish_fayl(nom):
    try:
        with open(nom, 'r') as fayl:
            return json.load(fayl)
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return []
    except json.JSONDecodeError:
        print("Faylda JSON formati topilmadi.")
        return []

def filtrlash(ro'yxat):
    return [foydalanuvchi for foydalanuvchi in ro'yxat if foydalanuvchi['yosh'] >= 18]

def main():
    foydalanuvchilar = oqish_fayl('foydalanuvchilar.json')
    kattalar = filtrlash(foydalanuvchilar)
    print(kattalar)

if __name__ == "__main__":
    main()
```

```json
// foydalanuvchilar.json
[
    {"ism": "Ali", "yosh": 25},
    {"ism": "Vali", "yosh": 17},
    {"ism": "Hasan", "yosh": 30},
    {"ism": "Husan", "yosh": 20}
]
