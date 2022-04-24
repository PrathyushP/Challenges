import json

def get_value(dict_obj, key):
    path = []
    if '/' in key:
        path = key.split('/')
    else:
        path.append(key)
    for route in path:
        try:
            dict_obj = dict_obj[route]
        except KeyError as err:
            print("Specified key not found in object")
            raise(err)
    print(dict_obj)

if __name__ == "__main__":
    obj = input("Enter object:")
    try:
        obj = json.loads(obj)
    except Exception as exc:
        print("INVALID DICTIONARY")
        raise(exc)
    key = input("Enter Key:")
    get_value(obj, key)
