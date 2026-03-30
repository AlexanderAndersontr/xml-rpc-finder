from time import sleep
import requests
import os
import argparse

parse = argparse.ArgumentParser(description="XML-RPC Zafiyet Tarama Toolu")
parse.add_argument("-f", default="sites.txt", required=True, help="Sitelerin olduğu dosya")
args = parse.parse_args()


print("""
  █████╗ ██╗     ███████╗██╗  ██╗
 ██╔══██╗██║     ██╔════╝╚██╗██╔╝
 ███████║██║     █████╗   ╚███╔╝ 
 ██╔══██║██║     ██╔══╝   ██╔██╗ 
 ██║  ██║███████╗███████╗██╔╝ ██╗
 ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
    """)


bulunan = []
sites = []
fileway = ""
payload = "xmlrpc.php"

def tarama():
    try:
        for i in sites:
            link = i + payload
            res = requests.get(link, verify=False)
            if res.status_code == 200:
                print(f"{link} | Bulundu! | 200")
                with open("bulunan.txt", "w") as file:
                    file.writelines(f"{link} | 200\n")
            else:
                print(f"{link} | Bulunmadı! | 404")

    except requests.exceptions.SSLError:
        print("SSL Hatası")

    except Exception:
        print("Bilinmeyen Hata")

while True:
    try:
        fileway = args.f
        if os.path.isfile(fileway):

            with open(fileway, "r") as file:
                sites.extend(file.read().splitlines())
                print(f"{len(sites)} tane site toplandı. 5 saniye sonra tarama başlıyor...")
                sleep(5)
                tarama()
                break
        else:
            print("Verdiğiniz Dosya Yolu Bulunamadı. Lütfen Tekrar Deneyim. Tool Kapatılıyor...")
            sleep(3)
            break

    except FileNotFoundError:
        print("Lütfen tekrar deneyin.")
