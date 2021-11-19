import random
import string

def gen_random_string(type, num_chars=10):
    if type == "NUM":
        char_set = string.digits
    elif type == "ALPHA":
        char_set = string.ascii_uppercase + string.ascii_lowercase
    else:
        char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
    s_random_chars = ''.join(random.sample(char_set * num_chars, num_chars))
    return s_random_chars

print(gen_random_string("NUM", 10))
print(gen_random_string("ALPHA", 10))
print(gen_random_string("ALPHA-NUM", 10))

def gen_random_string_02(num_chars = 10):
    char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
    s_random_chars1 = ''.join(random.sample(char_set*num_chars, num_chars))
    print(s_random_chars1)

    s_random1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(num_chars))
    print(s_random1)

    #random.SystemRandom()
    s_random2 = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(num_chars))
    print(s_random2)

    #after 3.6
    s_random10 = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=num_chars))
    print(s_random10)

#gen_random_string02(5)

def gen_random_from_uuid(num_chars = 10):
    import uuid
    s_uuid1 = uuid.uuid4()
    s_uuid1 = str(s_uuid1).replace('-', '')[0:num_chars]
    print("UUID=", s_uuid1)
    return s_uuid1

#gen_random_from_uuid(5)

#def gen_random_from_shuffle(num_chars = 10):
    #using shuffle - NOT WORKING YET
    #shuffle_range = (range(48, 58) + range(65, 91) + range(97, 123))
    #s_shuffle1 = random.shuffle(shuffle_range)
    #print('Shuffled string=', s_shuffle1)

#gen_random_from_shuffle(5)

#---- random int between 2 numbers
print(random.randint(100, 200))

#---- random item from list
def get_random_from_list(data_list):
    return data_list[random.randint(0, len(data_list)-1)]

data = ['aaa', 'ccc', 'ggg', 'yyy']
for _ in range(5):
    s_random = get_random_from_list(data)
    print("1. random from list:", s_random)


def get_random_from_list2(data_list, already_picked_list, trials=3):
    # Does not return duplicates
    while trials > 0:
        rand_index = random.randint(0, len(data_list) - 1)
        if rand_index in already_picked_list:
            trials -= 1
        else:
            already_picked_list.append(rand_index)
            return data_list[rand_index]
    return ""

already_picked_list = []
for _ in range(5):
    s_random = get_random_from_list2(data, already_picked_list, 3)
    print("2. random from list:", s_random)


#---- random item from dict: return a list with key & val
def get_random_item_from_dict(data_dict):
    dict_keys = list(data_dict)
    #dict_keys = list(data_dict.keys())
    dict_keys_index = random.randint(0, len(dict_keys) - 1)
    return [dict_keys[dict_keys_index], data_dict[dict_keys[dict_keys_index]]]

data_dict = {
    itm: itm for itm in data
}
for _ in range(5):
    s_random = get_random_item_from_dict(data_dict)
    print("1. random from dict:", s_random)

def get_random_item_from_dict2(data_dict, already_picked_list, trials=3):
    # returns list [key, val]
    # Does not return duplicates; "" if no item
    dict_keys = list(data_dict)
    # dict_keys = list(data_dict.keys())
    while trials > 0:
        dict_keys_index = random.randint(0, len(dict_keys) - 1)
        if dict_keys_index in already_picked_list:
            trials -= 1
        else:
            already_picked_list.append(dict_keys_index)
            return [dict_keys[dict_keys_index], data_dict[dict_keys[dict_keys_index]]]
    return ["", ""]

already_picked_list = []
for _ in range(5):
    s_random = get_random_item_from_dict2(data_dict, already_picked_list, 3)
    print("2. random from dict:", s_random)

