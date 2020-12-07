from gpiozero import CPUTemperature

def print_cpu_temperature():
    cpu = CPUTemperature
    print(cpu.temperature)