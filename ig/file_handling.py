def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None


def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError:
        print(f"An error occurred while writing to the file {file_path}.")


def store_data(data, file_path):
    try:
        with open(file_path, 'w') as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")
    except IOError:
        print(f"An error occurred while storing data to the file {file_path}.")
