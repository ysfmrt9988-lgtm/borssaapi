# server_api.py
from flask import Flask, jsonify
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

# Popüler BIST hisseleri
hisseler = [
    "ASELS.IS", "THYAO.IS", "GARAN.IS", "BIMAS.IS", "AKBNK.IS",
    "EREGL.IS", "SISE.IS", "PETKM.IS", "TUPRS.IS", "TAVHL.IS",
    "ISCTR.IS", "HALKB.IS", "VAKBN.IS", "YKBNK.IS", "TCELL.IS",
    "FROTO.IS", "TOASO.IS", "TSKB.IS", "TTRAK.IS", "MGROS.IS",
    "KCHOL.IS", "AKSUE.IS", "KRDMD.IS", "KOZAL.IS", "KOZAA.IS",
    "ARCLK.IS", "ENKAI.IS", "SODA.IS", "ISGYO.IS", "KAPLM.IS",
    "IHLGM.IS", "KORDS.IS", "KARSN.IS"
]

def fetch_hisseler():
    result = {}
    for hisse in hisseler:
        try:
            data = yf.download(hisse, period="1d", interval="1d", progress=False)
            if not data.empty:
                fiyat = float(data['Close'].iloc[-1])
                tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                result[hisse] = {"fiyat": fiyat, "tarih": tarih}
            else:
                result[hisse] = {"fiyat": None, "tarih": None, "error": "Veri yok"}
        except Exception as e:
            result[hisse] = {"fiyat": None, "tarih": None, "error": str(e)}
    return result

@app.route("/api/hisseler", methods=["GET"])
def get_hisseler():
    data = fetch_hisseler()
    return jsonify(data)

if __name__ == "__main__":
    # API'yi başlat
    app.run(host="0.0.0.0", port=5000)
