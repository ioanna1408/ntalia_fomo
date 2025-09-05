import requests

URL = "https://api.dexscreener.com/latest/dex/search?q=solana"

def main():
    try:
        r = requests.get(URL, timeout=10)
        if r.status_code == 200:
            data = r.json()
            print("✅ Scanner working")
            pairs = data.get("pairs") or []
            print("Pairs:", len(pairs))
            if pairs:
                first = pairs[0]
                print("First pair:", first.get("baseToken", {}).get("symbol"), "/", first.get("quoteToken", {}).get("symbol"))
                print("Dex:", first.get("dexId"), "| Chain:", first.get("chainId"))
                print("Price (usd):", first.get("priceUsd"))
        else:
            print(f"❌ Error: {r.status_code}")
    except Exception as e:
        print("⚠️ Exception:", e)

if __name__ == "__main__":
    main()
