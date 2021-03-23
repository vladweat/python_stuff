import datetime
import hashlib
import json
import os

BLOCKCHAIN_DIR = os.curdir + '/blockchain/'


def get_files():
    files = os.listdir(BLOCKCHAIN_DIR)
    return sorted([int(i) for i in files])


def get_hash(filename):
    file = open(BLOCKCHAIN_DIR + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()


def check_integrity():
    files = get_files()

    results = []

    for file in files[1:]:
        h = json.load(open(BLOCKCHAIN_DIR + str(file)))['hash']

        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'

        # print(f'block {prev_file} is {res}')

        results.append({'block': prev_file, 'result': res})

    return results


def create_first_block():
    transaction_time = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
    filename = '0'

    data = {
        'from': 'creator',
        'amount': 1,
        'to_whom': 'Elon Mask',
        'transaction_time': transaction_time,
        'hash': ''
    }
    with open(BLOCKCHAIN_DIR + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def write_block(name, amount, to_whom, prev_hash=''):
    files = get_files()

    prev_file = files[-1]
    filename = str(prev_file + 1)

    transaction_time = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
    prev_hash = get_hash(str(prev_file))

    data = {
        'from': name,
        'amount': amount,
        'to_whom': to_whom,
        'transaction_time': transaction_time,
        'hash': prev_hash
    }

    with open(BLOCKCHAIN_DIR + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block(name='vlad', amount='100', to_whom='Dasha')


if __name__ == '__main__':
    # print(check_integrity())
    print(os.curdir)
