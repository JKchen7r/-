import json
import numpy as np
from http import HTTPStatus
import dashscope

with open(r'D:\中医问答\pythonProject1\A3A4_data_json\chap15_A3A4.json', encoding='utf-8') as f:
    data_json = json.load(f)
    # print(data_json)
    # index = np.random.randint(0, 290, 12)
    index = range(5)
print(index)

test_list = []
answer_list = []
for i in index:
    # print(data_json[i]['option'])
    context = data_json[i]['context']
    option = data_json[i]['list_options']
    question_value = data_json[i]['list_questions']
    answer = data_json[i]['list_answers']
    # print(question_value)
    # print(option)
    test = ''
    for i in range(len(option)):
        # print(option[i])
        # print(question_value[i]['A'])

        question_values = 'A' + question_value[i]['A'] + 'B' + question_value[i]['B'] + 'C' + question_value[i]['C'] + 'D' + question_value[i]['D'] + 'E' + question_value[i]['E']
        # print(question_values)
        test = test + option[i]+question_values+'。'
    test1 = context + test
    test_list.append(test1)
    answer_list.append(answer)

# print(test_list)
# print(len(test_list))

#     # print(option_value)
#     question_values = ''
#     for q in question_value:
#         question_values = question_values+q
#     # print(question_values)
#
#     test = question_values+option_value
#     # print(test)

#
dashscope.api_key="sk-e82bb881b7844f1e97e426fc476184bc"
def call_with_messages(test_example):
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': '请给出下面选择题的答案：'+test_example}]

    response = dashscope.Generation.call(
        dashscope.Generation.Models.qwen_turbo,
        messages=messages,
        result_format='message',  # 将返回结果格式设置为 message
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))

if __name__ == '__main__':
    j = 0
    for i in test_list:
       print(i)
       print(answer_list[j])
       call_with_messages(i)
       j = j+1