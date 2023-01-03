from copy import copy

# 定義一個空的 set 型別
lines = set()

txt = "/home/hsu/Desktop/Auto_Concolic/data/source_group"
api_txt = "/home/hsu/Desktop/Auto_Concolic/data/API"

with open(txt, "r") as f:
    # 逐行讀取文件
    for line in f:
        # 將讀取的字串存入 set 中
        lines.add(line.strip())


api_list = []

with open(api_txt, "r") as f:
    for api in f:
        api_list.append(api)

# group list = [keyword, func_name, Source, Sink]
group_list = []


for line in lines:
    arr = line.split()
    group_list.append( [arr[1], arr[3], arr[5], arr[9]] )

api_dict = {}

for string in api_list:
    # 去除非字母的字符
    filtered_string = ''.join([ch for ch in string if ch.isalpha()])
    # 將字符串轉成小寫
    lowercase_string = filtered_string.lower()
    api_dict[lowercase_string] = string.replace('\n','')

# print(api_dict) 



# match api with func_name find longest is api
def longest_substring(string1, string2):
    # 建立一個二維數組，用於記錄最長公共子序列的長度
    lengths = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]
    # 初始化最長公共子序列的長度為 0
    longest = 0
    # 迭代字符串中的每個字符
    for i, ch1 in enumerate(string1):
        for j, ch2 in enumerate(string2):
            # 如果字符相同，就將最長公共子序列的長度加 1
            if ch1 == ch2:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
                longest = max(longest, lengths[i + 1][j + 1])
            # 否則，最長公共子序列的長度保持不變
            else:
                lengths[i + 1][j + 1] = 0
    # 返回最長公共子序列的長度
    return longest
'''
remove_list = []
kass_list = group_list

for group in group_list:
    # kick out non-abc and trun into lower
    func_name = ''.join([ch for ch in group[1] if ch.isalpha()]).lower()
    max_similarity = 0
    closest_key = ''
    for key in api_dict.keys():
        similarity = longest_substring(func_name, key)
        if similarity > max_similarity:
            max_similarity = similarity
            closest_key = key
    if max_similarity < 5:
        # print(f'{group[1]} : similarity < 5')
        remove_list.append(group)
        group_list.remove(group)
        continue
    # print(f'{group[1]} -> {api_dict[closest_key]}')
    group[1] = api_dict[closest_key]
'''
remove_list = []
kass_list = copy(group_list)

for group in kass_list:
    # kick out non-abc and trun into lower
    func_name = ''.join([ch for ch in group[1] if ch.isalpha()]).lower()
    max_similarity = 0
    closest_key = ''
    for key in api_dict.keys():
        similarity = longest_substring(func_name, key)
        if similarity > max_similarity:
            max_similarity = similarity
            closest_key = key
    if max_similarity < 5:
        remove_list.append(group)
        group_list.remove(group)
        continue
    group[1] = api_dict[closest_key]

print(len(group_list))
print(len(remove_list))

for i in group_list:
    print(i)