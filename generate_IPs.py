print('The program generates X amount of IPs consequent to the provided base IP\nNote that the same base IP will also count\n\n')


# How many IPs are going to be generated
# We subtract 1 because the same base IP also counts
IPs_to_generate = int(input("IPs to generate: ")) - 1


IP_base = input("IPs from: ").split('.')
IP_base_first_term = int(IP_base[0])
IP_base_second_term = int(IP_base[1])
IP_base_third_term = int(IP_base[2])
IP_base_quarter_term = int(IP_base[3])


# For each iteration we check if it can be added to the last term, if not, with the next one and so on
for IP in range(IPs_to_generate):
    if IP_base_quarter_term < 255:
        IP_base_quarter_term += 1
        continue
    else:
        if IP_base_third_term < 255:
            IP_base_third_term += 1
            
            IP_base_quarter_term = 0
            continue
        else:
            if IP_base_second_term < 255:
                IP_base_second_term += 1

                IP_base_third_term = 0
                continue
            else:
                if IP_base_first_term < 255:
                    IP_base_first_term += 1

                    IP_base_second_term = 0
                    continue
                else:
                    print("The IP reached its maximum possible: 255.255.255.255") 


final_IP = str(IP_base_first_term) + '.' + str(IP_base_second_term) + '.' + str(IP_base_third_term) + '.' + str(IP_base_quarter_term)
print(f"Final IP: {final_IP}")