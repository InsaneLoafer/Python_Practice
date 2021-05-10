#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from socket import *


class SyslogSend():

    def get_syslog(self, update_time, ADBOS_IP, type):
        FMT = "<189>{0} {2} %%01SEC/5/ATCKDF(1):" \
              "log_type=ip_drop " \
              "time={0} " \
              "device_ip=210.13.92.11 " \
              "device_type={1} " \
              "direction=inbound " \
              "zone_id=200 " \
              "zone_name=重保防护对象_M_128 " \
              "zone_ip=128.18.74.88 " \
              "biz_id=12 " \
              "is_deszone=ture " \
              "is_ipLocation=false " \
              "ipLocation_id=0 " \
              "total_pps=79043000 " \
              "total_kbps=88832 " \
              "tcp_pps=5628 " \
              "tcp_kbps=2365 " \
              "tcpfrag_pps=2365 " \
              "tcpfrag_kbps=2365 " \
              "tcp_stream=2365 " \
              "udp_pps=2365 " \
              "udp_kbps=2365 " \
              "udpfrag_pps=2365 " \
              "udpfrag_kbps=2365 " \
              "icmp_pps=2365 " \
              "icmp_kbps=2365 " \
              "other_pps=2365 " \
              "other_kbps=2365 " \
              "syn_pps=2365 " \
              "synack_pps=2365 " \
              "ack_pps=2365 " \
              "finrst_pps=2365 " \
              "http_pps=2365 " \
              "http_kbps=2365 " \
              "http_get_pps=2365 " \
              "https_pps=2365 " \
              "https_kbps=2365 " \
              "dns_request_pps=2365 " \
              "dns_request_kbps=2365 " \
              "dns_reply_pps=2365 " \
              "dns_reply_kbps=2365 " \
              "sip_invite_pps=2365 " \
              "sip_invite_kbps=365 ".format(update_time, type, ADBOS_IP)

        # Clean、DETECT依次执行。
        udpsocket = socket(AF_INET, SOCK_DGRAM)
        udpsocket.sendto(FMT.encode('utf-8'), (ADBOS_IP, 15141))
        print(FMT)
        with open('a.txt', 'a+') as f:
            f.write(FMT + '\n')
            print("write success!")

    def main(self):
        type = ["CLEAN", "DETECT"]
        ADBOS_IP = input("请输入adbos_ip：")
        continue_time = int(input("请输入持续时间（秒）："))
        interval_time = int(input("请输入间隔时间（秒）："))
        end_time = int(time.time()) + continue_time

        while time.time() < end_time:
            update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # 发送模板
            self.get_syslog(update_time, ADBOS_IP, type[0])
            self.get_syslog(update_time, ADBOS_IP, type[1])
            time.sleep(interval_time)


if __name__ == '__main__':
    syslog = SyslogSend()
    syslog.main()

