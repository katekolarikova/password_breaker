import hashlib
import time

# python scrip which will count hashes for passwords in rockyou.txt dictionary and compare them with the hashes from the hash list

hash_functions = [hashlib.md5, hashlib.sha1, hashlib.sha224, hashlib.sha256, hashlib.sha384, hashlib.sha512] # some of the most common hash functions

hashes_to_guess = ['5f4dcc3b5aa765d61d8327deb882cf99', 'e99a18c428cb38d5f260853678922e03', '8d3533d75ae2c3966d7e0d4fcc69216b', '0d107d09f5bbe40cade3de5c71e9e9b7']
hash_count = len(hashes_to_guess)
# compute hash for each password in the rockyou file and compare it with the hashes, try different hash functions
found_hashes = 0

with open('rockyou.txt', 'r', encoding = "ISO-8859-1") as f:
    start_time = time.time()
    for line in f:
        line = line.strip() # remove whitespace

        for hash_function in hash_functions:
            hash_object = hash_function(line.encode())
            hex_dig = hash_object.hexdigest() # get the hash in hexadecimal format
            if hex_dig in hashes_to_guess:
                print(f"Func:{hash_function.__name__}, Hash:{hex_dig}, Pass:{line}")
                found_hashes += 1

        if found_hashes == hash_count:
            break

end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: " + str(elapsed_time) + " seconds")
