import json
import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


with open(r'D:\中医问答\pythonProject1\B1_data_json\chap15_B1.json', encoding='utf-8') as f:
    data_json = json.load(f)

    index = [ 27 , 48  ,33,  58,  82 , 29 ,114 , 13 , 71 , 57,4,53,40,72,63,81,20,16,75,35]


print(index)

answer_list = []
prompt_list = []

for i in index:

    prompt_value = []
    option = data_json[i]['options']
    question_value = data_json[i]['list_question']
    answer = data_json[i]['list_answer']
    question_number = len(question_value)
    # print(question_value)
    # print(option)
    option_value = 'A.' + str(option['A']) + 'B.' + str(option['B']) + 'C.' + str(option['C']) + 'D.' + str(
        option['D']) + 'E.' + str(option['E'])
    # print(option_value)

    for j in range(question_number):

        prompt = question_value[j]+option_value
        prompt_value.extend([prompt])
    # print(prompt_value)

    prompt_list.append(prompt_value)
    answer_list.append(answer)

# 大模型名称和模型定义
model_name = "Qwen/Qwen2-1.5B-Instruct"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")

# 这里对大模型角色进行定义
sys_content = "You are a helpful assistant"

# 获取千问 token 实例
def setup_qwen_tokenizer():
    return AutoTokenizer.from_pretrained(model_name)

# 设置问答输入信息
def setup_model_input(tokenizer, prompt):
    # 判断硬件使用情况，有 cuda 用 cuda 没有 cuda 用 cpu
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")
    # 需要提问的内容的 json 格式
    messages = [
        {"role": "system", "content": sys_content},
        {"role": "user", "content": prompt}
    ]
    # 该函数将使用提供了标记化器来生成输入文本，然后对其进行标记化并将其转换为PyTorch张量。
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    return tokenizer([text], return_tensors="pt").to(device)

# 提交问题并获取回复
def msg_generate(prompt):
    tokenizer = setup_qwen_tokenizer()
    # 整理模型所需的输入信息
    model_inputs = setup_model_input(tokenizer, prompt)
    # 根据模型生成id集合
    generated_ids = model.generate(model_inputs.input_ids, max_new_tokens=512)
    # 删除没有响应的id
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(
        model_inputs.input_ids, generated_ids)]
    # 根据id集合对返回信息进行解码获得返回结果
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]


if __name__ == '__main__':
    j = 0
    for i in prompt_list:
        print(i)
        print(answer_list[j])
        prompt_number = len(i)
        for p in range(prompt_number):
            prompt = "请你做一下下面一道选择题：" + i[p]
            response = msg_generate(prompt)
            print(">>> " + response)
        print("-" * 100)
        j = j + 1



       # # prompt = "请你做一道中医测试中A1或者A2类型的选择题,请你一步一步思考并将思考过程写在【解析】和<eoe>之间。你将从A，B，C，D，E中选出一个最正确的答案，并写在【答案】和<eoa>之间。\n例如：【答案】: A <eoa>\n完整的题目回答的格式如下：\n【解析】 ... <eoe>\n【答案】 ... <eoa>\n请你严格按照上述格式作答。\n题目如下：" + i
       # prompt = "请你做一下下面一道选择题：" + i[j]
       # response = msg_generate(prompt)
       # print(">>> " + response)
       # print("-"*100)
       # j = j+1