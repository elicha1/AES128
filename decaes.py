from Crypto.Cipher import AES
from Crypto import Random
import time
import os
from struct import pack


# get the PID
print "PID = " + str(os.getpid())
raw_input("continue...")
#-----------------------#

f_time = "%.20f" % time.time()
bs = AES.block_size
key = 'Sixteen byte key'
iv = Random.new().read(AES.block_size) #DES3.block_size==8
cipher= AES.new(key, AES.MODE_CBC, iv)
with open("encrypt_16MB.txt", "r") as f:
    plaintext = f.readlines()

plaintext = ''.join(plaintext)

plen = bs - divmod(len(plaintext),bs)[1]
padding = [plen]*plen
padding = pack('b'*plen, *padding)
#----------------------------

msg = iv + cipher.encrypt(plaintext + padding)

#----------------------------
l_time = "%.20f" % time.time()

done_time = float(l_time) - float(f_time)

f= open("DECRYPT.txt","w+")
f.write(msg)
f.close()

print "dEncrypt time : " + str(done_time)
raw_input("continue...")
