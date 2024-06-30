import json
import re

pattern = r"([0-9]+[\．.]\D)"

file_path = r'D:\中医问答\pythonProject1\B1_data_txt\chap12_B1.txt'
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

dict1_list = []
dict2_list = []
list1 = ['options', 'list_question', 'list_answer', 'list_analysis', 'index', 'chapter', 'answer_type']
list2 = ['A', 'B', 'C', 'D', 'E']
j = 0

for item in result_list:

    list3 = []
    list_questions = []
    list_answers = []
    list_analysis = []

    regex = r"[a-eA-E]+[\．.]|\d\)."
    result = re.split(regex, item)
    del result[0]
    # print((result), len(result))


    option_list = result[0:5]
    # print(option_list)
    dict2 = dict(zip(list2, option_list))

    del result[0:5]
    result.insert(0, dict2)
    # print(result, len(result))

    if len(result) == 3:

        qlist1 = result[1]
        regex1 = r"【答案】|【解析】"
        qlist1 = re.split(regex1, qlist1)
        if len(qlist1) != 3:
            qlist1.append('')
        list_questions.append(qlist1[0])
        list_answers.append(qlist1[1])
        list_analysis.append(qlist1[2])
        # print(list_questions, list_answers, list_analysis)

        qlist2 = result[2]
        qlist2 = re.split(regex1, qlist2)
        if len(qlist2) != 3:
            qlist2.append('')
        list_questions.append(qlist2[0])
        list_answers.append(qlist2[1])
        list_analysis.append(qlist2[2])
        # print(list_questions, list_answers, list_analysis)

    elif len(result) == 4:

        qlist1 = result[1]
        regex1 = r"【答案】|【解析】"
        qlist1 = re.split(regex1, qlist1)
        if len(qlist1) != 3:
            qlist1.append('')
        list_questions.append(qlist1[0])
        list_answers.append(qlist1[1])
        list_analysis.append(qlist1[2])
        # print(list_questions, list_answers, list_analysis)

        qlist2 = result[2]
        qlist2 = re.split(regex1, qlist2)
        if len(qlist2) != 3:
            qlist2.append('')
        list_questions.append(qlist2[0])
        list_answers.append(qlist2[1])
        list_analysis.append(qlist2[2])
        # print(list_questions, list_answers, list_analysis)

        qlist3 = result[3]
        qlist3 = re.split(regex1, qlist3)
        if len(qlist3) != 3:
            qlist3.append('')
        list_questions.append(qlist3[0])
        list_answers.append(qlist3[1])
        list_analysis.append(qlist3[2])

    elif len(result) == 5:

        qlist1 = result[1]
        regex1 = r"【答案】|【解析】"
        qlist1 = re.split(regex1, qlist1)
        if len(qlist1) != 3:
            qlist1.append('')
        list_questions.append(qlist1[0])
        list_answers.append(qlist1[1])
        list_analysis.append(qlist1[2])
        # print(list_questions, list_answers, list_analysis)

        qlist2 = result[2]
        qlist2 = re.split(regex1, qlist2)
        if len(qlist2) != 3:
            qlist2.append('')
        list_questions.append(qlist2[0])
        list_answers.append(qlist2[1])
        list_analysis.append(qlist2[2])
        # print(list_questions, list_answers, list_analysis)

        qlist3 = result[3]
        qlist3 = re.split(regex1, qlist3)
        if len(qlist3) != 3:
            qlist3.append('')
        list_questions.append(qlist3[0])
        list_answers.append(qlist3[1])
        list_analysis.append(qlist3[2])

        qlist4 = result[4]
        qlist4 = re.split(regex1, qlist4)
        if len(qlist4) != 3:
            qlist4.append('')
        list_questions.append(qlist4[0])
        list_answers.append(qlist4[1])
        list_analysis.append(qlist4[2])

    elif len(result) == 6:

        qlist1 = result[1]
        regex1 = r"【答案】|【解析】"
        qlist1 = re.split(regex1, qlist1)
        if len(qlist1) != 3:
            qlist1.append('')
        list_questions.append(qlist1[0])
        list_answers.append(qlist1[1])
        list_analysis.append(qlist1[2])
        # print(list_questions, list_answers, list_analysis)

        qlist2 = result[2]
        qlist2 = re.split(regex1, qlist2)
        if len(qlist2) != 3:
            qlist2.append('')
        list_questions.append(qlist2[0])
        list_answers.append(qlist2[1])
        list_analysis.append(qlist2[2])
        # print(list_questions, list_answers, list_analysis)

        qlist3 = result[3]
        qlist3 = re.split(regex1, qlist3)
        if len(qlist3) != 3:
            qlist3.append('')
        list_questions.append(qlist3[0])
        list_answers.append(qlist3[1])
        list_analysis.append(qlist3[2])

        qlist4 = result[4]
        qlist4 = re.split(regex1, qlist4)
        if len(qlist4) != 3:
            qlist4.append('')
        list_questions.append(qlist4[0])
        list_answers.append(qlist4[1])
        list_analysis.append(qlist4[2])

        qlist5 = result[5]
        qlist5 = re.split(regex1, qlist5)
        if len(qlist5) != 3:
            qlist5.append('')
        list_questions.append(qlist5[0])
        list_answers.append(qlist5[1])
        list_analysis.append(qlist5[2])

    elif len(result) == 7:

        qlist1 = result[1]
        regex1 = r"【答案】|【解析】"
        qlist1 = re.split(regex1, qlist1)
        if len(qlist1) != 3:
            qlist1.append('')
        list_questions.append(qlist1[0])
        list_answers.append(qlist1[1])
        list_analysis.append(qlist1[2])
        # print(list_questions, list_answers, list_analysis)

        qlist2 = result[2]
        qlist2 = re.split(regex1, qlist2)
        if len(qlist2) != 3:
            qlist2.append('')
        list_questions.append(qlist2[0])
        list_answers.append(qlist2[1])
        list_analysis.append(qlist2[2])
        # print(list_questions, list_answers, list_analysis)

        qlist3 = result[3]
        qlist3 = re.split(regex1, qlist3)
        if len(qlist3) != 3:
            qlist3.append('')
        list_questions.append(qlist3[0])
        list_answers.append(qlist3[1])
        list_analysis.append(qlist3[2])

        qlist4 = result[4]
        qlist4 = re.split(regex1, qlist4)
        if len(qlist4) != 3:
            qlist4.append('')
        list_questions.append(qlist4[0])
        list_answers.append(qlist4[1])
        list_analysis.append(qlist4[2])

        qlist5 = result[5]
        qlist5 = re.split(regex1, qlist5)
        if len(qlist5) != 3:
            qlist5.append('')
        list_questions.append(qlist5[0])
        list_answers.append(qlist5[1])
        list_analysis.append(qlist5[2])

        qlist6 = result[6]
        qlist6 = re.split(regex1, qlist6)
        if len(qlist6) != 3:
            qlist6.append('')
        list_questions.append(qlist6[0])
        list_answers.append(qlist6[1])
        list_analysis.append(qlist6[2])

    elif len(result) == 8:

        qlist1 = result[1]
        regex1 = r"【答案】|【解析】"
        qlist1 = re.split(regex1, qlist1)
        if len(qlist1) != 3:
            qlist1.append('')
        list_questions.append(qlist1[0])
        list_answers.append(qlist1[1])
        list_analysis.append(qlist1[2])
        # print(list_questions, list_answers, list_analysis)

        qlist2 = result[2]
        qlist2 = re.split(regex1, qlist2)
        if len(qlist2) != 3:
            qlist2.append('')
        list_questions.append(qlist2[0])
        list_answers.append(qlist2[1])
        list_analysis.append(qlist2[2])
        # print(list_questions, list_answers, list_analysis)

        qlist3 = result[3]
        qlist3 = re.split(regex1, qlist3)
        if len(qlist3) != 3:
            qlist3.append('')
        list_questions.append(qlist3[0])
        list_answers.append(qlist3[1])
        list_analysis.append(qlist3[2])

        qlist4 = result[4]
        qlist4 = re.split(regex1, qlist4)
        if len(qlist4) != 3:
            qlist4.append('')
        list_questions.append(qlist4[0])
        list_answers.append(qlist4[1])
        list_analysis.append(qlist4[2])

        qlist5 = result[5]
        qlist5 = re.split(regex1, qlist5)
        if len(qlist5) != 3:
            qlist5.append('')
        list_questions.append(qlist5[0])
        list_answers.append(qlist5[1])
        list_analysis.append(qlist5[2])

        qlist6 = result[6]
        qlist6 = re.split(regex1, qlist6)
        if len(qlist6) != 3:
            qlist6.append('')
        list_questions.append(qlist6[0])
        list_answers.append(qlist6[1])
        list_analysis.append(qlist6[2])

        qlist7 = result[7]
        qlist7 = re.split(regex1, qlist7)
        if len(qlist7) != 3:
            qlist7.append('')
        list_questions.append(qlist7[0])
        list_answers.append(qlist7[1])
        list_analysis.append(qlist7[2])

    list3.append(dict2)
    list3.append(list_questions)
    list3.append(list_answers)
    list3.append(list_analysis)
    list3.append(j)
    list3.append('第十二章：内科学')
    list3.append('B1')
    j = j+1
    # print(list3, len(list3))

    dict3 = dict(zip(list1, list3))
    dict1_list.append(dict3)

with open('../B1_data_json/chap12_B1.json', 'w', encoding='utf-8') as file:
    file.write('[')
    file.write('\n')
    for data in dict1_list:
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.write(',')
        file.write('\n')
    file.write(']')


