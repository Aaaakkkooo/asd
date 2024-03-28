def merge_dicts(*dicts):
    merged_dict = {}
    for dictionary in dicts:
        merged_dict.update(dictionary)
    return merged_dict

# Пример использования:
dict1 = {'a': 'abai', 'b': 'Aiym'}
dict2 = {'b': 'dias', 'c': 'nurs'}
dict3 = {'d': 'eraly'}

merged_dict = merge_dicts(dict1, dict2, dict3)
print("Объединенный словарь:", merged_dict)
