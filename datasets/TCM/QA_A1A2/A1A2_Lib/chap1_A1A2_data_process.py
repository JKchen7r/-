import json
import re

pattern = r"([0-9]+[\．.])"

file_path = r'D:\中医问答\pythonProject1\data_txt\chap1_A1A2.txt'
with open(file_path, "r", encoding='utf-8') as file:
    test_str = file.read()


result = re.split(pattern, test_str)
result.remove('')
# print(result)
# print(len(result))

result_list = [result[i] for i in range(len(result)) if i % 2 != 0]
result_list = [item.replace('\n', '') for item in result_list]
# print(result_list)

dict1_list = []
dict2_list = []
list1 = ['question', 'option', 'answer', 'analysis', 'index', 'chapter', 'question_type']
list2 = ['A', 'B', 'C', 'D', 'E']
j = 0
for item in result_list:
    regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
    result = re.split(regex, item)

    if len(result) != 8:
        result.append('')
    result.append(j)
    result.append('第一章：中医理论基础')
    result.append('A1/A2')
    # print(result, len(result))

    option_list = result[1:6]
    # print(option_list, len(option_list))

    dict2 = dict(zip(list2, option_list))
    # print(dict2, len(dict2))
    dict2_list.append(dict2)

    del result[1:6]
    result.insert(1, dict2)
    # print(result, len(result))

    dict1 = dict(zip(list1, result))

    # print(dict1)
    dict1_list.append(dict1)
    j = j+1

with open('../A1A2_data_json/chap1_A1A2.json', 'w', encoding='utf-8') as file:
    file.write('[')
    file.write('\n')
    for data in dict1_list:
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.write(',')
        file.write('\n')
    file.write(']')




