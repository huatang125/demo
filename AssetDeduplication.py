import argparse

def wt(path,items):
    with open(path, 'w', encoding='utf-8') as f:
        for item in items:
            f.write(item + '\n')

def rt(path):
    with open(path, 'r') as f:
        items = f.read().split("\n")
    return items

def my_splicing(items1, items2, s):
    tar = []
    for i1 in items1:
        for i2 in items2:
            tmp = i1 + s + i2
            tar.append(tmp)
    return tar
def ad(dir_str, ports_str, protocols_str):
    """

    :param dir_str: 资产列表所在路径
    :param ports_str: 端口号
    :param protocols_str: 协议
    :return: none
    """
    ports = ports_str.split(',') if ports_str is not None else []
    protocols = protocols_str.split(',') if protocols_str is not None else []

    urls_set = set(rt(dir_str))
    print("Deduplicated!")
    print(f'\033[0;32mfinished\033[0m ===> {len(urls_set)} targets')

    my_complete = (my_splicing(protocols, my_splicing(urls_set, ports, ':'), '://') if len(protocols) != 0 else my_splicing(urls_set, ports, ':')) if len(ports) != 0 else ( my_splicing(protocols, urls_set, '://') if len(protocols) != 0 else urls_set)

    with open('./result.txt', 'w', encoding='utf-8') as f:
        for item in my_complete:
            f.write(item + '\n')

if __name__ == "__main__":
    begin = '''
\033[0;31m _   _ _____  \033[0m  \033[0;32m ____           _             _ _           _           _ \033[0m
\033[0;31m| | | |_   _| \033[0m  \033[0;32m|  _ \  ___  __| |_   _ _ __ | (_) ___ __ _| |_ ___  __| |\033[0m
\033[0;31m| |_| | | |   \033[0m  \033[0;32m| | | |/ _ \/ _` | | | | '_ \| | |/ __/ _` | __/ _ \/ _` |\033[0m
\033[0;31m|  _  | | |   \033[0m  \033[0;32m| |_| |  __/ (_| | |_| | |_) | | | (_| (_| | ||  __/ (_| |\033[0m
\033[0;31m|_| |_| |_|   \033[0m  \033[0;32m|____/ \___|\__,_|\__,_| .__/|_|_|\___\__,_|\__\___|\__,_|\033[0m
\033[0;31m              \033[0m  \033[0;32m                       |_|                                \033[0m
v1.0
'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", help="The path of the text file, only the domain name is needed in the content of the text", required=True, type=str)
    parser.add_argument("-p", "--port", help="Specify the ports to be spliced, and separate multiple ports with commas", type=str)
    parser.add_argument("-P", dest="protocol", help="Specify the protocols to be spliced, and separate multiple protocols with commas", default="https", type=str)
    args = parser.parse_args()
    print(begin)
    ports_str = None if args.port is None else args.port
    protocols_str = None if args.protocol is None else args.protocol
    ad(args.list, args.port, args.protocol)
    print()



