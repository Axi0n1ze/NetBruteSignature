from scapy.all import send, IP, TCP, UDP, ICMP
import random
import time

def send_malicious_packets(target_ip, count=10, delay=1):

    """
        
        대상 IP로 악성 유사 패킷을 생성 및 전송하는 함수.
        param target_ip: 패킷을 보낼 대상 IP 주소.
        param count: 전송할 패킷 개수.
        param delay: 패킷 전송 간 지연 시간(초 단위).
    
    """
    
    for i in range(count):

        # 랜덤하게 프로토콜 선택: TCP, UDP, 또는 ICMP
        protocol = random.choice(['TCP', 'UDP', 'ICMP'])

        if protocol == 'TCP':

            # 비정상적인 플래그를 가진 TCP 패킷 생성
            packet = IP(dst=target_ip) / TCP(dport=random.randint(1, 65535), flags="FPU")

        elif protocol == 'UDP':

            # 임의의 포트를 가진 UDP 패킷 생성
            packet = IP(dst=target_ip) / UDP(dport=random.randint(1, 65535))

        elif protocol == 'ICMP':

            # 사용자 정의 페이로드를 포함한 ICMP Echo Request 패킷 생성
            packet = IP(dst=target_ip) / ICMP(type=8, code=0) / (b"MALICIOUS_PAYLOAD" * 5)

        # 패킷 전송
        send(packet, verbose=False)

        print(f"[{i + 1}/{count}] {protocol} 패킷을 {target_ip}로 전송 완료")

        # 패킷 간 지연 시간
        time.sleep(delay)

if __name__ == "__main__":
    
    target_ip = input("대상 IP 주소를 입력하세요: ")
    
    packet_count = int(input("전송할 패킷 개수를 입력하세요: "))
    
    delay_between_packets = float(input("패킷 간 지연 시간(초 단위)을 입력하세요: "))

    print("테스트 목적으로 악성 유사 패킷을 전송합니다...")
    
    send_malicious_packets(target_ip, count=packet_count, delay=delay_between_packets)
    
    print("패킷 전송이 완료되었습니다.")
