def sort_dict_list(data, key):
    data.sort(key=lambda item: item.get(key, 0))
    return data
