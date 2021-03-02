import os

ipOuHost = input("Digite ip ou host a ser verificado")

os.system('ping -n 6 {}'.format(ipOuHost))

