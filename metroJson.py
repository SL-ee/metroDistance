import pandas as pd
import json

data = pd.read_excel("D:/전체DB_github_업로드용.xlsx", "real_final_json")

indexs = []
values = []
enters_up = {}
enters_down = {}
metroEnterance = []
num_columns = len(data.columns)
num_rows = len(data.index)

# print(num_rows)
for i in range(num_columns):
    indexs.append(data.columns[i])
for j in range(num_columns):
    values.append(data[indexs[j]])

start = 0
count = 1
for k in range(0, num_rows-1):
    if int(values[0][k]) == int(values[0][k+1]) and values[1][k] == values[1][k+1] and values[2][k] == values[2][k+1]:
        continue
    else:
        until = k
        for i in range(start, until + 1):
            if values[3][i] == "상선":
                enters_up[values[4][i]] = {indexs[5]: int(values[5][i]),
                                        indexs[6]: values[6][i],
                                        indexs[8]: values[8][i],
                                        indexs[11]: values[11][i],
                                        indexs[12]: int(values[12][i])}
            else:
                enters_down[values[4][i]] = {indexs[5]: int(values[5][i]),
                                           indexs[6]: values[6][i],
                                           indexs[8]: values[8][i],
                                           indexs[11]: values[11][i],
                                           indexs[12]: int(values[12][i])}

        metroEnterance.append({
            'id': count,
            indexs[0]: int(data[indexs[0]][k]),
            indexs[1]: data[indexs[1]][k],
            indexs[2]: data[indexs[2]][k],
            'entrances_up': enters_up,
            'entrances_down': enters_down,
            indexs[7]: data[indexs[7]][k],
            indexs[9]: data[indexs[9]][k],
            indexs[10]: data[indexs[10]][k]
        })
        start = k + 1
        enters_up = {}
        enters_down = {}
        count += 1

with open('metroEnterance.json', 'w', encoding="utf-8") as file:
    json.dump(metroEnterance, file, ensure_ascii=False, indent="\t")
