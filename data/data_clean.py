import xlsxwriter

with open("train.txt", encoding="utf-8") as file:
    lines1 = file.read()

with open("test.txt", encoding="utf-8") as file:
    lines2 = file.read()

lines1 = lines1.split("\n")
lines2 = lines2.split("\n")


lines = lines1+lines2
emotions = {"sad" : 0,
            "happy": 0,
            "angry": 0,
            "fear": 0,
            "disgust": 0}

perfect_list_emotions = []

keys = emotions.keys()
print(keys)

for line in lines:
    for key in keys:
        if key in line:
            text = line.replace(key+" ","")
            perfect_list_emotions.append({"text":text,"reaction":key})
            emotions[key]+=1

print(emotions)
# print(perfect_list_emotions)
print(lines[200])
print(perfect_list_emotions[200])
print(len(lines))
print(len(perfect_list_emotions))

# excel file
wb = xlsxwriter.Workbook("DS1.xlsx")
ws = wb.add_worksheet()

row = 0

for i in perfect_list_emotions:
    ws.write(row, 0, i["text"])
    ws.write(row, 1, i["reaction"])

    row+=1

wb.close()