import os
import hashlib


def join_files(directory):
    os.chdir(directory)

    hash_table = {}
    with open("hash_table.txt", 'r') as hash_table_file:
        for line in hash_table_file:
            type, file_path, file_hash = line.strip().split()
            if type == "文件块":
                hash_table[file_path] = file_hash
    chunk_files = sorted(hash_table.keys())

    output_filename = "merged_file"  # 你可以在这里自定义输出文件名
    with open(output_filename, 'wb') as output_file:
        for chunk_file in chunk_files:
            with open(chunk_file, 'rb') as chunk:
                chunk_data = chunk.read()
            output_file.write(chunk_data)

    with open(output_filename, 'rb') as output_file:
        data = output_file.read()
        output_hash = hashlib.blake2b(data).hexdigest()

    with open("hash_table.txt", 'a') as hash_table:
        hash_table.write(f"重组文件 {output_filename} {output_hash}\n")


def check_integrity(directory):
    os.chdir(directory)

    hash_table = {}
    with open("hash_table.txt", 'r') as hash_table_file:
        for line in hash_table_file:
            type, file_path, file_hash = line.strip().split()
            hash_table[file_path] = (type, file_hash)

    source_hash = None
    joined_hash = None
    for file_path, (type, file_hash) in hash_table.items():
        if type == "源文件":
            source_hash = file_hash
        elif type == "重组文件":
            joined_hash = file_hash

    if source_hash != joined_hash:
        return False

    for file_path, (type, file_hash) in hash_table.items():
        if type != "文件块":
            continue

        with open(file_path, 'rb') as chunk:
            chunk_data = chunk.read()
        blake2b_hash = hashlib.blake2b(chunk_data).hexdigest()
        if blake2b_hash != file_hash:
            return False

    return True


# 示例用法
directory = input("请输入一个路径: ")
while not os.path.isdir(directory):
    print("路径不存在.")
    directory = input("请重新输入路径，零散的文件和指纹表放在其中: ")

join_files(directory)

if check_integrity(directory):
    print("文件完整性验证通过！")
else:
    print("文件完整性验证失败！")
