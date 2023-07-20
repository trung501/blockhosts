from urllib.parse import urlparse
from googlesearch import search
import os
list_domain_block = []

def extract_domain_from_url(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

def read_file():
    global list_domain_block
    # check file domain.txt
    if os.path.isfile("domain.txt") == False:
        with open("domain.txt", "w") as f:
            f.write("")
    with open("domain.txt", "r") as f:
        for line in f:
            list_domain_block.append(line.strip())
    print("Đã đọc file domain.txt")

def write_file():
    global list_domain_block
    with open("domain.txt", "w") as f:
        for line in list_domain_block:
            f.write(line+"\n")
    print("Đã ghi file domain.txt")

def delete_white_list():
    global list_domain_block
    list_domain_block=list(set(list_domain_block))
    with open("whitelist.txt", "r") as f:
        for line in f:
            domain="127.0.0.1 "+line.strip()
            if domain in list_domain_block:
                list_domain_block.remove(domain)
    print("Đã xóa domain trong whitelist.txt")

def search_and_print_domains(keyword, num_results=50):
    print(f"Searching Google for '{keyword}'...")
    search_results = search(keyword, num_results=num_results)

    for url in search_results:
        domain = extract_domain_from_url(url)
        if domain:
            domain_block="127.0.0.1 "+domain
            if domain_block not in list_domain_block:
                list_domain_block.append(domain_block)
                print(f"Website domain found: {domain}")
        else:
            print(f"No domain found for: {url}")

if __name__ == "__main__":
    read_file()
    # search_keyword = input("Nhập từ khóa cần tìm trên Google: ")
    # search_and_print_domains(search_keyword)
    delete_white_list()
    write_file()
