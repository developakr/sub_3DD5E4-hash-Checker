import time
import hashlib
import sys

def sofia_hash(msg):
    h = ""
    m = hashlib.md5()
    m.update(msg)
    msg_md5 = m.digest()
    for i in range(8):
        n = (ord(msg_md5[2*i]) + ord(msg_md5[2*i+1])) % 0x3e
        if n > 9:
            if n > 35:
                n += 61
            else:
                n += 55
        else:
            n += 0x30
        h += chr(n)
    return h

print '--------------------------------------'
print '| DevelopAKR sub_3DD5E4 hash Checker |'
print '--------------------------------------'
print 'Hash(sub_3DD5E4): ', sys.argv[1]
print 'Wordlist: ', sys.argv[2]



counter = 1
md5_hash = sys.argv[1]
pwdfile = sys.argv[2]
print '--------------------------------------'
print '-------Process, please wait!!!--------'


try:
    pwdfile = open(pwdfile,"r")
except:
    print "\nFile not found"
    quit()


for password in pwdfile:
    filemd5 = sofia_hash(password.strip())
    start = time.time()
    #print "Trying passowrd %d: %s" % (counter, password.strip())
    #print counter, password.strip()
    #print "\033", counter, "\r",
    #sys.stdout.flush()

    counter += 1
    end = time.time()
    t_time = end - start

    if md5_hash == filemd5:
        print "\nPassword Found. \nPassword is : %s" % password
        print "Total runtime was -- ", t_time, "second"
        time.sleep(5)
        break
      

else:
    print "\nPassword not Found."
