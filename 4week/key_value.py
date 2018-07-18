import os
import tempfile
import json
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def clear():
    os.remove(storage_path)

def get_data():
	if not os.path.exists(storage_path):
		return {}
	with open(storage_path, 'r') as f:
		try:
			data = json.loads(str(f.read()))
		except ValueError:
			print("got in ValueError")
			data = {}
	return data

def put_data(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))

def get_value(key):
	data = get_data()
	return data.get(key)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--key")
	parser.add_argument("--value")
	parser.add_argument("--clear")
	args = parser.parse_args()

	if args.clear:
		clear()	
	elif (args.key and args.value):
		put_data(args.key, args.value)
	elif args.key:
		print(get_value(args.key))
	else:
		print('Wrong command')




if __name__ == '__main__':
	main()

