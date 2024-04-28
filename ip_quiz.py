#!/usr/bin/env python3

import ipaddress
import random


def main():
    menu = [
        '1. Integers (0-255) to bits',
        '2. IPv4 address to network and broadcast addresses',
        '3. IPv4 address to first and last host addresses'
    ]
    print()
    for i in menu:
        print(i)
    print()
    try:
        selection = int(input('>'))
        print()
        if selection == 1:
            eight_bit_integer_quiz()
        if selection == 2:
            subnet_and_broadcast_address_quiz()
        if selection == 3:
            first_and_last_host_address_quiz()
    except (KeyboardInterrupt, EOFError):
        pass


def eight_bit_integer_quiz():
    try:
        while True:
            num = random.randint(0, 255)
            print(num)
            input()
            print(f"{format(num, '08b')}\n")
    except (KeyboardInterrupt, EOFError):
        pass


def subnet_and_broadcast_address_quiz():
    try:
        while True:
            random_ip_address = generate_random_ip_address()
            print(random_ip_address)
            #input()
            input()
            print(ipaddress.IPv4Interface(random_ip_address).network.network_address)
            print(ipaddress.IPv4Interface(random_ip_address).network.broadcast_address)
            print()
            print('------------')
            print()
    except (KeyboardInterrupt, EOFError):
        pass


def first_and_last_host_address_quiz():
    try:
        while True:
            random_ip_address = generate_random_ip_address()
            print(random_ip_address)
            #input()
            input()
            print(ipaddress.IPv4Interface(random_ip_address).network.network_address + 1)
            print(ipaddress.IPv4Interface(random_ip_address).network.broadcast_address - 1)
            print()
            print('------------')
            print()
    except (KeyboardInterrupt, EOFError):
        pass


def generate_random_ip_address():
    octets = [str(random.randint(0, 255)) for i in range(4)]
    random_ip_address = ".".join(octets)
    random_ip_address += f"/{str(random.randint(0, 32))}"
    return random_ip_address

main()
