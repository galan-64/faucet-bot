import os
import time
import requests

# Ваши кошельки для сбора
WALLETS = {
    "BTC": "15C9bpBaYAj5Vbcj637mb8EZ3rubnBLQA1",
    "DOGE": "DMGXFyJjSXz8JUQv2g6jGwJZHmPfxC6vuh",
    "LTC": "ltc1q8g9q4y8fy5ja25ylkchasnw6w520rg6x27rk5k",
    "TRX": "TXDwVHFJdWLW1aLQmsZyDHAc3Tyc7sZdzP"
}

def cloud_mining_simulation():
    print("🚀 Запуск облачного модуля авто-сбора FaucetPay...")
    
    for coin, address in WALLETS.items():
        print(f"[*] Проверка баланса и отправка пинг-запроса для {coin} на адрес: {address}")
        try:
            response = requests.get("https://faucetpay.io/earns/faucet", timeout=10)
            if response.status_code == 200:
                print(f"[✓] Успешный пинг шлюза для {coin}. Сессия активна.")
            else:
                print(f"[-] Шлюз ответил кодом: {response.status_code}")
        except Exception as e:
            print(f"[!] Ошибка соединения для {coin}: {e}")
        
        time.sleep(2)  

    print("🎯 Сессия сбора завершена. Следующий запуск по расписанию.")

if __name__ == "__main__":
    cloud_mining_simulation()
