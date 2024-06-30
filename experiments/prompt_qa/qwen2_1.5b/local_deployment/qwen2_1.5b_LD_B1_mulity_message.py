import json
import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


with open(r'D:\中医问答\pythonProject1\B1_data_json\chap2_B1.json', encoding='utf-8') as f:
    data_json = json.load(f)

    index = [212, 387, 246, 216 ,377 , 76 ,366 , 24,  7 ,112,414 ,188 ,149 ,  9  ,28 ,313 ,196 ,239,  58 ,337]

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

#
# 大模型名称和模型定义
model_name = "Qwen/Qwen2-1.5B-Instruct"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")

# 这里对大模型角色进行定义
sys_content = "You are a helpful assistant"


if __name__ == '__main__':
    j = 0

    for prompt in prompt_list:
        print(answer_list[j])
        print(prompt)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        # 整理模型所需的输入信息
        # model_inputs = setup_model_input(tokenizer, prompt)

        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")
        # 需要提问的内容的 json 格式
        messages = [
            {"role": "system", "content": sys_content},
        ]
        for prompt_i in prompt:
            messages_i = {"role": "user", "content": "请做一下下面的选择题"+prompt_i}
            messages.append(messages_i)

            # 该函数将使用提供了标记化器来生成输入文本，然后对其进行标记化并将其转换为PyTorch张量。
            text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            model_inputs = tokenizer([text], return_tensors="pt").to(device)
            # 根据模型生成id集合
            generated_ids = model.generate(model_inputs.input_ids, max_new_tokens=512)
            # 删除没有响应的id
            generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(
                model_inputs.input_ids, generated_ids)]
            # 根据id集合对返回信息进行解码获得返回结果
            response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
            print(response)
            messages = messages[:-1]
            messages_i = {"role": "assistant", "content": response}
            messages.append(messages_i)

        print('-' * 100)
        j = j+1


