def anagrams(lists):
    dict = {}
    for value_of_str in lists:
        key = ''.join(sorted(value_of_str))

        if key in dict.keys():
            dict[key].append(value_of_str)
        else:
            dict[key] = []
            dict[key].append(value_of_str)
    output = ""
    for key, value in dict.items():
        output = output + ''.join(value) + ''
        return output


if __name__ == "__main__":
        lists = ['serve', 'rival', 'lovely',
                 'caveat', 'devote', 'irving','livery',
                 'selves', 'latvian', 'saviour', 'observe',' octavian',
                 'dovetail', 'levantine']
        print(anagrams(lists))



