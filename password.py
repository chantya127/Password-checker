import requests 
import hashlib  #for getting sha1 

def pawned_api_check(password): 
    sha1_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char,tail = sha1_pass[:5],sha1_pass[5:]
    response = request_api_data(first5_char)  #passing only first 5 chars of sha1 hashcode
    print()
    return get_count(response,tail)


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char 
    response = requests.get(url)
    if response.status_code !=200:
        raise RuntimeError(f'Error fetching {response.status_code} .please check api')
    else:
        return response  

#Server returns a response containing hashes and count of that hash    
    
def get_count(hashes,hash_to_check): #to get count of how many times password was cracked
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hash_to_check:
            return count
    return 0       


password = input('Enter password')
count = pawned_api_check(password)

if count:
    print(f'Please change as {password}  was found {count} times!!')
else:
    print(f'{password} was not found')
    





