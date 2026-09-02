import os
import time
import requests

# Список ваших кошельков
WALLETS = {
    "BTC": "15C9bpBaYAj5Vbcj637mb8EZ3rubnBLQA1",
    "ETH": "0x90C12E633fcb59995A1f0B28CDaE8b0CdA785770",
    "DOGE": "DMGXFyJjSXz8JUQv2g6jGwJZHmPfxC6vuh",
    "LITECOIN": "ltc1q8g9q4y8fy5ja25ylkchasnw6w520rg6x27rk5k",
    "BCH": "bitcoincash:qz7027kj6sd9dqdc6rp9v3lt37ljwp34gc8e4ger9t",
    "DASH": "XitiTgcWTRvWYWieNjZTbRiMzFexmTU921",
    "DGB": "DHGkbvxurTeGJ6FYrMSjAtikQpYRiMkSX9",
    "TRX": "TXDwVHFJdWLW1aLQmsZyDHAc3Tyc7sZdzP",
    "USDT": "TXDwVHFJdWLW1aLQmsZyDHAc3Tyc7sZdzP",
    "FEYORRA": "0x90C12E633fcb59995A1f0B28CDaE8b0CdA785770",
    "ZCASH": "t1e2wLr6BezRQKKjigSj47mYToysX4sms8Z",
    "BNB": "0x40ff878fbd7D2544218ee6E5fC60A7bC4EaB837c",
    "SOLANA": "7Rn2e1NLPp6zH8pDKEuuBDAkRS4Ysfe8vTPVpdwuFH5F",
    "RIPPLE": "rhi77L73jGvGN3zQf3AEbYnjWYZu7CSTe8//memo-6743922",
    "POLYGON": "0x4578861bE9ad85fE1619fEB578D2fD440A44b99C",
    "CARDANO": "addr1q9v57yhzw533leqyhnpdvpmehgeqdrju9a58379pky9352aqlx2rpr5asvy4r8kf6lxyu9uygf4fkq8mjawyuh32eh3qxeaq5x",
    "TONCOIN": "EQD14kgmngE0fNYVs7_9dw78V3rPhNt7_Ee-7X3ykDORQvMp//memo-6743922",
    "STELLAR": "GDAEZBKKPVVEBPDFSY6WMQ7Y4C7FYCS6CYODNURRN4EZIGTMNKKROESG//memo-6743922",
    "USDC": "7Rn2e1NLPp6zH8pDKEuuBDAkRS4Ysfe8vTPVpdwuFH5F",
    "MONERO": "4ByeEKTJbi3faVNHTWEupmM1fdwEv95CqCqC7rCDdVhXDt4vj5E4FB1jUKxNAF6EHFHmuQhnHoXcUK84Nc4cQfmfKQ8zXo5FtSDLpiz6wC"
}

# Прямые ссылки на страницы сбора монеты на ClaimFreeCoins
FAUCET_PAGES = {
    "BTC": "https://claimfreecoins.io/bitcoin-faucet/",
    "ETH": "https://claimfreecoins.io/ethereum-faucet/",
    "DOGE": "https://claimfreecoins.io/dogecoin-faucet/",
    "LITECOIN": "https://claimfreecoins.io/litecoin-faucet/",
    "BCH": "https://claimfreecoins.io/bitcoin-cash-faucet/",
    "DASH": "https://claimfreecoins.io/dash-faucet/",
    "DGB": "https://claimfreecoins.io/digibyte-faucet/",
    "TRX": "https://claimfreecoins.io/tron-faucet/",
    "USDT": "https://claimfreecoins.io/tether-faucet/",
    "FEYORRA": "https://claimfreecoins.io/feyorra-faucet/",
    "ZCASH": "https://claimfreecoins.io/zcash-faucet/",
    "BNB": "https://claimfreecoins.io/binance-coin-faucet/",
    "SOLANA": "https://claimfreecoins.io/solana-faucet/",
    "RIPPLE": "https://claimfreecoins.io/ripple-faucet/",
    "POLYGON": "https://claimfreecoins.io/polygon-faucet/",
    "CARDANO": "https://claimfreecoins.io/cardano-faucet/",
    "TONCOIN": "https://claimfreecoins.io/toncoin-faucet/",
    "STELLAR": "https://claimfreecoins.io/stellar-faucet/",
    "USDC": "https://claimfreecoins.io/usdc-faucet/",
    "MONERO": "https://claimfreecoins.io/monero-faucet/"
}

def run_gr8_claims():
    session_cookie = os.getenv("FAUCET_SESSION_COOKIE", "")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "Cookie": session_cookie,
        "Referer": "https://claimfreecoins.io/"
    }
    
    print(f"🚀 Запуск сборщика для {len(WALLETS)} монет...")
    
    for coin, address in WALLETS.items():
        url = FAUCET_PAGES.get(coin)
        if not url:
            continue
            
        print(f"\n[🔄] Обработка: {coin}")
        print(f"    Адрес: {address}")
        
        payload = {
            "address": address,
            "submit": "Claim"
        }
        
        try:
            response = requests.post(url, data=payload, headers=headers, timeout=15)
            
            if response.status_code == 200:
                if "sent to your FaucetPay" in response.text or "success" in response.text.lower():
                    print(f"    [✓] Успешно! Монеты отправлены на FaucetPay.")
                else:
                    print(f"    [~] Страница ответила (код 200), но требуется прохождение защиты/таймера.")
            else:
                print(f"    [-] Ошибка сервера: Код {response.status_code}")
                
        except Exception as e:
            print(f"    [❌] Сбой соединения: {e}")
            
        time.sleep(3)

if __name__ == "__main__":
    run_gr8_claims()
