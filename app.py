from flask import Flask, render_template, request
from exchange_rate import get_exchange_rate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        amount = float(request.form["amount"])
        target_currency = request.form["target_currency"]
        base_currency = "THB"  # แปลงจาก USD เป็นสกุลอื่น

        # ดึงอัตราแลกเปลี่ยนจาก API
        rate = get_exchange_rate(base_currency, target_currency)
        
        if rate:
            converted_amount = amount * rate
            result = f"{amount:.2f} {base_currency} → {converted_amount:.2f} {target_currency}"
        else:
            result = "เกิดข้อผิดพลาดในการดึงอัตราแลกเปลี่ยน"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
