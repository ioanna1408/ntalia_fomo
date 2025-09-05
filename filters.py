def liquidity_filter(pair):
    # Ενδεικτικά: απορρίπτει αν liquidity < 3000
    liquidity = pair.get("liquidity", {}).get("usd", 0)
    return liquidity >= 3000

def volume_filter(pair):
    # Ενδεικτικά: απορρίπτει αν volume24h < 20000
    volume = pair.get("volume", {}).get("h24", 0)
    return volume >= 20000

def holders_filter(pair):
    # placeholder, θα μπει όταν έχουμε API για holders
    return True
