import requests

URL = "https://api.dexscreener.com/latest/dex/tokens/solana"

def main():
    try:
        r = requests.get(URL, timeout=10)
        if r.status_code == 200:
            data = r.json()
            print("✅ Dex API connected")
            print(data.keys())  # εμφάνιση των πρώτων keys
        else:
            print(f"❌ Error: {r.status_code}")
    except Exception as e:
        print("⚠️ Exception:", e)

if __name__ == "__main__":
    main()
