import hashlib

def hash_function (string_to_hash):
    encoded_string = string_to_hash.encode('utf-8')
    return hashlib.sha256(encoded_string).hexdigest()

def hash_together(prev_hash, new_hash):
    string_to_hash = prev_hash + new_hash
    return hash_function(string_to_hash)

