import json
import re

pattern = r"([0-9]+[\．.]\D)"

file_path = r'D:\中医问答\pythonProject1\A3A4_data_txt\chap12_A3A4.txt'
with open(file_path, "r", encoding='utf-8') as file:
    test_str = file.read()

result = re.split(pattern, test_str)
result.remove('')
# print(result)
# print(len(result))

result_list = []
for i in range(len(result)):
    if i % 2 == 0:
        new_sentence = result[i][-1]+result[i+1]

        result_list.append(new_sentence)


# result_list = [result[i] for i in range(len(result)) if i % 2 != 0]
result_list = [item.replace('\n', '') for item in result_list]
# print(result_list)
# print(len(result_list))

dict1_list = []
dict2_list = []
list1 = ['context', 'list_options', 'list_questions', 'list_answers', 'list_analysis', 'index', 'chapter', 'answer_type']
list2 = ['A', 'B', 'C', 'D', 'E']
j = 0

for item in result_list:

    list3 = []
    list_questions = []
    list_options = []
    list_answers = []
    list_analysis = []

    # regex = r"[a-zA-Z]+[\．.]|\d\)."
    regex = r"\d\)."
    result = re.split(regex, item)
    # del result[0]
    # print((result), len(result))
    list3.append(result[0])

    if len(result) == 3:

        content1 = result[1]
        # print(content1)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result1 = re.split(regex, content1)
        # print(result, len(result))
        option1_list = [item for item in result1[1:6]]
        option1_dict = dict(zip(list2, option1_list))

        list_questions.append(result1[0])       # 问题
        list_options.append(option1_dict)      # 选项
        list_answers.append(result1[6])         # 答案

        if len(result1) == 8:
            list_analysis.append(result1[7])    # 解析
        else: list_analysis.append('')

        content2 = result[2]
        # print(content2)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result2 = re.split(regex, content2)
        # print(result, len(result))
        option2_list = [item for item in result2[1:6]]
        option2_dict = dict(zip(list2, option1_list))

        list_questions.append(result2[0])  # 问题
        list_options.append(option2_dict)  # 选项
        list_answers.append(result2[6])  # 答案

        if len(result2) == 8:
            list_analysis.append(result2[7])  # 解析
        else:
            list_analysis.append('')

    elif len(result) == 4:

        content1 = result[1]
        # print(content1)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result1 = re.split(regex, content1)
        # print(result, len(result))
        option1_list = [item for item in result1[1:6]]
        option1_dict = dict(zip(list2, option1_list))

        list_questions.append(result1[0])  # 问题
        list_options.append(option1_dict)  # 选项
        list_answers.append(result1[6])  # 答案

        if len(result1) == 8:
            list_analysis.append(result1[7])  # 解析
        else:
            list_analysis.append('')

        content2 = result[2]
        # print(content2)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result2 = re.split(regex, content2)
        # print(result, len(result))
        option2_list = [item for item in result2[1:6]]
        option2_dict = dict(zip(list2, option2_list))

        list_questions.append(result2[0])  # 问题
        list_options.append(option2_dict)  # 选项
        list_answers.append(result2[6])  # 答案

        if len(result2) == 8:
            list_analysis.append(result2[7])  # 解析
        else:
            list_analysis.append('')

        content3 = result[3]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result3 = re.split(regex, content3)
        # print(result3, len(result3))
        option3_list = [item for item in result3[1:6]]
        option3_dict = dict(zip(list2, option3_list))

        list_questions.append(result3[0])  # 问题
        list_options.append(option3_dict)  # 选项
        list_answers.append(result3[6])  # 答案

        if len(result3) == 8:
            list_analysis.append(result3[7])  # 解析
        else:
            list_analysis.append('')

    elif len(result) == 5:

        content1 = result[1]
        # print(content1)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result1 = re.split(regex, content1)
        # print(result, len(result))
        option1_list = [item for item in result1[1:6]]
        option1_dict = dict(zip(list2, option1_list))

        list_questions.append(result1[0])  # 问题
        list_options.append(option1_dict)  # 选项
        list_answers.append(result1[6])  # 答案

        if len(result1) == 8:
            list_analysis.append(result1[7])  # 解析
        else:
            list_analysis.append('')

        content2 = result[2]
        # print(content2)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result2 = re.split(regex, content2)
        # print(result, len(result))
        option2_list = [item for item in result2[1:6]]
        option2_dict = dict(zip(list2, option2_list))

        list_questions.append(result2[0])  # 问题
        list_options.append(option2_dict)  # 选项
        list_answers.append(result2[6])  # 答案

        if len(result2) == 8:
            list_analysis.append(result2[7])  # 解析
        else:
            list_analysis.append('')

        content3 = result[3]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result3 = re.split(regex, content3)
        # print(result3, len(result3))
        option3_list = [item for item in result3[1:6]]
        option3_dict = dict(zip(list2, option3_list))

        list_questions.append(result3[0])  # 问题
        list_options.append(option3_dict)  # 选项
        list_answers.append(result3[6])  # 答案

        if len(result3) == 8:
            list_analysis.append(result3[7])  # 解析
        else:
            list_analysis.append('')

        content4 = result[4]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result4 = re.split(regex, content4)
        # print(result3, len(result3))
        option4_list = [item for item in result4[1:6]]
        option4_dict = dict(zip(list2, option4_list))

        list_questions.append(result4[0])  # 问题
        list_options.append(option4_dict)  # 选项
        list_answers.append(result4[6])  # 答案

        if len(result4) == 8:
            list_analysis.append(result4[7])  # 解析
        else:
            list_analysis.append('')

    elif len(result) == 6:

        content1 = result[1]
        # print(content1)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result1 = re.split(regex, content1)
        # print(result, len(result))
        option1_list = [item for item in result1[1:6]]
        option1_dict = dict(zip(list2, option1_list))

        list_questions.append(result1[0])  # 问题
        list_options.append(option1_dict)  # 选项
        list_answers.append(result1[6])  # 答案

        if len(result1) == 8:
            list_analysis.append(result1[7])  # 解析
        else:
            list_analysis.append('')

        content2 = result[2]
        # print(content2)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result2 = re.split(regex, content2)
        # print(result, len(result))
        option2_list = [item for item in result2[1:6]]
        option2_dict = dict(zip(list2, option2_list))

        list_questions.append(result2[0])  # 问题
        list_options.append(option2_dict)  # 选项
        list_answers.append(result2[6])  # 答案

        if len(result2) == 8:
            list_analysis.append(result2[7])  # 解析
        else:
            list_analysis.append('')

        content3 = result[3]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result3 = re.split(regex, content3)
        # print(result3, len(result3))
        option3_list = [item for item in result3[1:6]]
        option3_dict = dict(zip(list2, option3_list))

        list_questions.append(result3[0])  # 问题
        list_options.append(option3_dict)  # 选项
        list_answers.append(result3[6])  # 答案

        if len(result3) == 8:
            list_analysis.append(result3[7])  # 解析
        else:
            list_analysis.append('')

        content4 = result[4]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result4 = re.split(regex, content4)
        # print(result3, len(result3))
        option4_list = [item for item in result4[1:6]]
        option4_dict = dict(zip(list2, option4_list))

        list_questions.append(result4[0])  # 问题
        list_options.append(option4_dict)  # 选项
        list_answers.append(result4[6])  # 答案

        if len(result4) == 8:
            list_analysis.append(result4[7])  # 解析
        else:
            list_analysis.append('')

        content5 = result[5]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result5 = re.split(regex, content5)
        # print(result3, len(result3))
        option5_list = [item for item in result5[1:6]]
        option5_dict = dict(zip(list2, option5_list))

        list_questions.append(result5[0])  # 问题
        list_options.append(option5_dict)  # 选项
        # print(j,'xxx')
        list_answers.append(result5[6])  # 答案

        if len(result5) == 8:
            list_analysis.append(result5[7])  # 解析
        else:
            list_analysis.append('')

    elif len(result) == 7:

        content1 = result[1]
        # print(content1)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result1 = re.split(regex, content1)
        # print(result, len(result))
        option1_list = [item for item in result1[1:6]]
        option1_dict = dict(zip(list2, option1_list))

        list_questions.append(result1[0])  # 问题
        list_options.append(option1_dict)  # 选项
        list_answers.append(result1[6])  # 答案

        if len(result1) == 8:
            list_analysis.append(result1[7])  # 解析
        else:
            list_analysis.append('')

        content2 = result[2]
        # print(content2)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result2 = re.split(regex, content2)
        # print(result, len(result))
        option2_list = [item for item in result2[1:6]]
        option2_dict = dict(zip(list2, option2_list))

        list_questions.append(result2[0])  # 问题
        list_options.append(option2_dict)  # 选项
        list_answers.append(result2[6])  # 答案

        if len(result2) == 8:
            list_analysis.append(result2[7])  # 解析
        else:
            list_analysis.append('')

        content3 = result[3]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result3 = re.split(regex, content3)
        # print(result3, len(result3))
        option3_list = [item for item in result3[1:6]]
        option3_dict = dict(zip(list2, option3_list))

        list_questions.append(result3[0])  # 问题
        list_options.append(option3_dict)  # 选项
        list_answers.append(result3[6])  # 答案

        if len(result3) == 8:
            list_analysis.append(result3[7])  # 解析
        else:
            list_analysis.append('')

        content4 = result[4]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result4 = re.split(regex, content4)
        # print(result3, len(result3))
        option4_list = [item for item in result4[1:6]]
        option4_dict = dict(zip(list2, option4_list))

        list_questions.append(result4[0])  # 问题
        list_options.append(option4_dict)  # 选项
        list_answers.append(result4[6])  # 答案

        if len(result4) == 8:
            list_analysis.append(result4[7])  # 解析
        else:
            list_analysis.append('')

        content5 = result[5]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result5 = re.split(regex, content5)
        # print(result3, len(result3))
        option5_list = [item for item in result5[1:6]]
        option5_dict = dict(zip(list2, option5_list))

        list_questions.append(result5[0])  # 问题
        list_options.append(option5_dict)  # 选项
        # print(j)
        list_answers.append(result5[6])  # 答案

        if len(result5) == 8:
            list_analysis.append(result5[7])  # 解析
        else:
            list_analysis.append('')

        # print(j,'sss')
        content6 = result[6]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result6 = re.split(regex, content6)
        # print(result3, len(result3))
        option6_list = [item for item in result6[1:6]]
        option6_dict = dict(zip(list2, option6_list))

        list_questions.append(result6[0])  # 问题
        list_options.append(option6_dict)  # 选项
        list_answers.append(result6[6])  # 答案

        if len(result6) == 8:
            list_analysis.append(result6[7])  # 解析
        else:
            list_analysis.append('')

    elif len(result) == 8:

        content1 = result[1]
        # print(content1)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result1 = re.split(regex, content1)
        # print(result, len(result))
        option1_list = [item for item in result1[1:6]]
        option1_dict = dict(zip(list2, option1_list))

        list_questions.append(result1[0])  # 问题
        list_options.append(option1_dict)  # 选项
        list_answers.append(result1[6])  # 答案

        if len(result1) == 8:
            list_analysis.append(result1[7])  # 解析
        else:
            list_analysis.append('')

        content2 = result[2]
        # print(content2)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result2 = re.split(regex, content2)
        # print(result, len(result))
        option2_list = [item for item in result2[1:6]]
        option2_dict = dict(zip(list2, option2_list))

        list_questions.append(result2[0])  # 问题
        list_options.append(option2_dict)  # 选项
        list_answers.append(result2[6])  # 答案

        if len(result2) == 8:
            list_analysis.append(result2[7])  # 解析
        else:
            list_analysis.append('')

        content3 = result[3]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result3 = re.split(regex, content3)
        # print(result3, len(result3))
        option3_list = [item for item in result3[1:6]]
        option3_dict = dict(zip(list2, option3_list))

        list_questions.append(result3[0])  # 问题
        list_options.append(option3_dict)  # 选项
        list_answers.append(result3[6])  # 答案

        if len(result3) == 8:
            list_analysis.append(result3[7])  # 解析
        else:
            list_analysis.append('')

        content4 = result[4]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result4 = re.split(regex, content4)
        # print(result3, len(result3))
        option4_list = [item for item in result4[1:6]]
        option4_dict = dict(zip(list2, option4_list))

        # print(j)
        list_questions.append(result4[0])  # 问题
        list_options.append(option4_dict)  # 选项
        list_answers.append(result4[6])  # 答案

        if len(result4) == 8:
            list_analysis.append(result4[7])  # 解析
        else:
            list_analysis.append('')

        content5 = result[5]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result5 = re.split(regex, content5)
        # print(result3, len(result3))
        option5_list = [item for item in result5[1:6]]
        option5_dict = dict(zip(list2, option5_list))

        list_questions.append(result5[0])  # 问题
        list_options.append(option5_dict)  # 选项
        list_answers.append(result5[6])  # 答案

        if len(result5) == 8:
            list_analysis.append(result5[7])  # 解析
        else:
            list_analysis.append('')

        content6 = result[6]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result6 = re.split(regex, content6)
        # print(result3, len(result3))
        option6_list = [item for item in result6[1:6]]
        option6_dict = dict(zip(list2, option6_list))

        list_questions.append(result6[0])  # 问题
        list_options.append(option6_dict)  # 选项
        list_answers.append(result6[6])  # 答案

        if len(result6) == 8:
            list_analysis.append(result6[7])  # 解析
        else:
            list_analysis.append('')

        content7 = result[7]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result7 = re.split(regex, content7)
        # print(result3, len(result3))
        option7_list = [item for item in result7[1:6]]
        option7_dict = dict(zip(list2, option7_list))

        list_questions.append(result7[0])  # 问题
        list_options.append(option7_dict)  # 选项
        list_answers.append(result7[6])  # 答案

        if len(result7) == 8:
            list_analysis.append(result7[7])  # 解析
        else:
            list_analysis.append('')

    elif len(result) == 8:

        content1 = result[1]
        # print(content1)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result1 = re.split(regex, content1)
        # print(result, len(result))
        option1_list = [item for item in result1[1:6]]
        option1_dict = dict(zip(list2, option1_list))

        list_questions.append(result1[0])  # 问题
        list_options.append(option1_dict)  # 选项
        list_answers.append(result1[6])  # 答案

        if len(result1) == 8:
            list_analysis.append(result1[7])  # 解析
        else:
            list_analysis.append('')

        content2 = result[2]
        # print(content2)
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result2 = re.split(regex, content2)
        # print(result, len(result))
        option2_list = [item for item in result2[1:6]]
        option2_dict = dict(zip(list2, option2_list))

        list_questions.append(result2[0])  # 问题
        list_options.append(option2_dict)  # 选项
        list_answers.append(result2[6])  # 答案

        if len(result2) == 8:
            list_analysis.append(result2[7])  # 解析
        else:
            list_analysis.append('')

        content3 = result[3]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result3 = re.split(regex, content3)
        # print(result3, len(result3))
        option3_list = [item for item in result3[1:6]]
        option3_dict = dict(zip(list2, option3_list))

        list_questions.append(result3[0])  # 问题
        list_options.append(option3_dict)  # 选项
        list_answers.append(result3[6])  # 答案

        if len(result3) == 8:
            list_analysis.append(result3[7])  # 解析
        else:
            list_analysis.append('')

        content4 = result[4]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result4 = re.split(regex, content4)
        # print(result3, len(result3))
        option4_list = [item for item in result4[1:6]]
        option4_dict = dict(zip(list2, option4_list))

        list_questions.append(result4[0])  # 问题
        list_options.append(option4_dict)  # 选项
        list_answers.append(result4[6])  # 答案

        if len(result4) == 8:
            list_analysis.append(result4[7])  # 解析
        else:
            list_analysis.append('')

        content5 = result[5]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result5 = re.split(regex, content5)
        # print(result3, len(result3))
        option5_list = [item for item in result5[1:6]]
        option5_dict = dict(zip(list2, option5_list))

        list_questions.append(result5[0])  # 问题
        list_options.append(option5_dict)  # 选项
        list_answers.append(result5[6])  # 答案

        if len(result5) == 8:
            list_analysis.append(result5[7])  # 解析
        else:
            list_analysis.append('')

        content6 = result[6]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result6 = re.split(regex, content6)
        # print(result3, len(result3))
        option6_list = [item for item in result6[1:6]]
        option6_dict = dict(zip(list2, option6_list))

        list_questions.append(result6[0])  # 问题
        list_options.append(option6_dict)  # 选项
        list_answers.append(result6[6])  # 答案

        if len(result6) == 8:
            list_analysis.append(result6[7])  # 解析
        else:
            list_analysis.append('')

        content7 = result[7]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result7 = re.split(regex, content7)
        # print(result3, len(result3))
        option7_list = [item for item in result7[1:6]]
        option7_dict = dict(zip(list2, option7_list))

        list_questions.append(result7[0])  # 问题
        list_options.append(option7_dict)  # 选项
        list_answers.append(result7[6])  # 答案

        if len(result7) == 8:
            list_analysis.append(result7[7])  # 解析
        else:
            list_analysis.append('')

        content8 = result[8]
        regex = r"[a-zA-Z]+[\．.]|【答案】|【解析】"
        result8 = re.split(regex, content8)
        # print(result3, len(result3))
        option8_list = [item for item in result8[1:6]]
        option8_dict = dict(zip(list2, option8_list))

        list_questions.append(result8[0])  # 问题
        list_options.append(option8_dict)  # 选项
        list_answers.append(result8[6])  # 答案

        if len(result8) == 8:
            list_analysis.append(result8[7])  # 解析
        else:
            list_analysis.append('')

    list3.append(list_questions)
    list3.append(list_options)
    list3.append(list_answers)
    list3.append(list_analysis)
    list3.append(j)
    list3.append('第十二章：内科学')
    list3.append('A3A4')
    j = j+1
    # print(list3, len(list3))

    dict3 = dict(zip(list1, list3))
    dict1_list.append(dict3)

with open('../A3A4_data_json/chap12_A3A4.json', 'w', encoding='utf-8') as file:
    file.write('[')
    file.write('\n')
    for data in dict1_list:
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.write(',')
        file.write('\n')
    file.write(']')



