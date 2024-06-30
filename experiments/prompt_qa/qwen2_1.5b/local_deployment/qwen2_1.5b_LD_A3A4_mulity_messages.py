import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

with open(r'D:\中医问答\pythonProject1\A3A4_data_json\chap15_A3A4.json', encoding='utf-8') as f:
    data_json = json.load(f)
    # print(data_json)
    index = range(0, 5)
    # index = [81,162,105,223,236,46,141,44,230,256,203,172,58,82,208,84,29,168,16,94]

print(index)

prompt_list = []
answer_list = []
for i in index:
    # print(data_json[i]['option'])
    context = data_json[i]['context']
    option = data_json[i]['list_options']
    question_value = data_json[i]['list_questions']
    answer = data_json[i]['list_answers']
    # print(question_value)
    # print(option)
    test = []
    for i in range(len(option)):
        # print(option[i])
        # print(question_value[i]['A'])

        question_values = 'A' + question_value[i]['A'] + 'B' + question_value[i]['B'] + 'C' + question_value[i]['C'] + 'D' + question_value[i]['D'] + 'E' + question_value[i]['E']
        # print(question_values)

        test_value = context + option[i] + question_values

        test.append(test_value)

    prompt_list.append(test)
    answer_list.append(answer)
# print(answer_list)
# print(prompt_list)
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
            # messages_i = {"role": "user", "content": "请你做一道中医测试中的选择题,请你一步一步思考并将思考过程写在【解析】和<eoe>之间"+prompt_i}
            messages_i = {"role": "user", "content": "请你做一道选择题,选出最合适的答案，并给出解释"+prompt_i}
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
            print(">>> " +response)
            messages = messages[:-1]
            messages_i = {"role": "assistant", "content": response}
            messages.append(messages_i)

        # print(messages)

        print('-' * 100)
        j = j+1