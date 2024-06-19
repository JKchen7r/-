import json
import numpy as np
from http import HTTPStatus
import dashscope
import os

with open(r'D:\中医问答\pythonProject1\B1_data_json\chap1_B1.json', encoding='utf-8') as f:
    data_json = json.load(f)
    # print(data_json)
    index = np.random.randint(0, 252, 10)
print(index)

test_list = []
answer_list = []
for i in index:
    # print(data_json[i]['option'])
    option = data_json[i]['option']
    question_value = data_json[i]['question']
    answer = data_json[i]['answer']

    option_value = 'A' + str(option['A'])+'B' + str(option['B'])+'C' + str(option['C'])+'D' + str(option['D'])+'E' + str(option['E'])
    # print(option_value)
    # print(question_value)
    test = question_value+option_value
    # print(test)
    test_list.append(test)
    answer_list.append(answer)
# print(test_list)
# print(len(test_list))

dashscope.api_key = os.getenv("API_KEY")
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

