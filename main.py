#!/usr/bin/env python
"""
info about our project
"""

# import


__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


from ipshow.ipshow import print_ip
from passgenerator.passgenerator import start
from systemUpgrade.systemupgrade import call_system_update_upgrade
from systeminfo.systeminfo import print_system_info
from networkScanner.ns import get_ip
from gpiocheck.gpiocheck import check_gpio
from temperature.temperature import print_cpu_temperature


def main():
    while True:
        choice = input("\n\nWat wil je doen?: \n"
                       "1) Show my ip\n"
                       "2) Generate password\n"
                       "3) update and upgrade linux system\n"
                       "4) get system info\n"
                       "5) scan network\n"
                       "6) read gpio pin\n"
                       "7) check temperature of cpu\n"
                       "q) close program\n"
                       "give your input: ")
        if choice == '1':
            print_ip()
        elif choice == '2':
            start()
        elif choice == '3':
            call_system_update_upgrade()
        elif choice == '4':
            print_system_info()
        elif choice == '5':
            get_ip()
        elif choice == '6':
            check_gpio()
        elif choice == '7':
            print_cpu_temperature()
        elif choice == 'q':
            print("\nprogram closed")
            break
        else:
            print("\ntry again")


if __name__ == '__main__':
    main()
