import os
from eth_account import Account
import secrets

def create_file(fpath, fname, content):
    if not os.path.exists(fpath):
        os.makedirs(fpath)
    with open(os.path.join(fpath, fname), 'w+') as f:
        f.write(content)

priv = secrets.token_hex(32)
private_key = "0x" + priv
acct = Account.from_key(private_key)
address = acct.address
pubkey = acct._key_obj.public_key


print(private_key)
create_file("/tmp", "nodekey", str(private_key))
print(pubkey)
create_file("/tmp","nodekey.pub", str(pubkey))
print(address)
create_file("/tmp","address", address)
