from multiprocessing import Pool
import random
import subprocess
import os

passcode = 'abcdefghijklmnopqrstuvwxyz0123456789'
key_array = []
file_path = "D:\\Parallels_Desktop_17.1.2.51548_by_TNT_.7z"

def f(password):
    if random.randrange(1, 20) == 1:
        print("processing ", password)

    command = '"C:\\Program Files\\7-Zip\\7z.exe" -pmac-torrent-download.net_' + password + ' t ' + file_path
    child = subprocess.call(command, stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
    if child == 0:
        print("password is mac-torrent-download.net_"+password)
        exit()
    return

if __name__ == '__main__':
    for i in passcode:
        for j in passcode:
            for k in passcode:
                key_array.append(i + j + k)
    print("Key size: ", len(key_array))

    p = Pool(6)
    p.map(f, key_array)


