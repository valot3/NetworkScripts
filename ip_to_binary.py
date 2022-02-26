#!/bin/python3

ip = str(input("IP: ")).split('.')
ip_binaria = ""
ip_index = 0

for octeto in ip:
    #Por cada ciclo se suma una unidad al indice de la IP para saber cuando esta esta en su ultimo octeto
    ip_index += 1

    
    bin_octeto = bin(int(octeto))
    
    #Lista de los caracteres del binario del octeto para poder modificarlo.
    l_bin_octeto = list(bin_octeto)
    l_bin_octeto[0:2] = ''
    #Si la longitud es menor a 8, agregamos los ceros correspondientes al inicio
    while len(l_bin_octeto) < 8:
        #Agregamos un 0, en el indice 0.
        l_bin_octeto.insert(0, '0')

    bin_octeto = ''.join(l_bin_octeto)


    if ip_index < 4:
        ip_binaria += bin_octeto + '.'
    else:
        ip_binaria += bin_octeto



print(ip_binaria)





