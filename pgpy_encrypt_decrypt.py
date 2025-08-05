'''

source my_venv/bin/activate
pip list



'''




#---------decrypt
#import pgpy
from pgpy import PGPKey, PGPMessage

#--pri key
key_file = "km/km_practice/keys/km_key.asc"

with open(key_file, 'r') as f: recipient_key = f.read()

priv_key = PGPKey.from_blob(recipient_key)[0]
priv_key = """
"""
input_data_path = "km/km_practice/data/"
input_filename = "sample_data.TXT.pgp"

enc_data = PGPMessage.from_file(f"{input_data_path}/{input_filename}")

decrypted_filename = ".".join(input_filename.split(".")[:-1])
with priv_key.unlock("mypass") as key:
    with open(f"{input_data_path}/{decrypted_filename}", "wb") as f:
        f.write(priv_key.decrypt(enc_data).message)
