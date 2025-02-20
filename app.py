from flask import Flask, render_template, request

app = Flask(__name__)

# Disease-to-pesticide mapping
disease_pesticides = {
    "Tomato___Bacterial_spot": "Copper-based fungicides like Copper Hydroxide or Copper Oxychloride.",
    "Tomato___Early_blight": "Use Chlorothalonil or Mancozeb-based fungicides.",
    "Tomato___Late_blight": "Apply Metalaxyl, Mancozeb, or Copper-based fungicides.",
    "Tomato___Leaf_Mold": "Use Chlorothalonil or Copper-based fungicides.",
    "Tomato___Septoria_leaf_spot": "Mancozeb, Chlorothalonil, or Copper fungicides are effective.",
    "Tomato___Spider_mites Two-spotted_spider_mite": "Apply Abamectin, Neem oil, or Sulfur-based miticides.",
    "Tomato___Target_Spot": "Use Chlorothalonil or Difenoconazole-based fungicides.",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "No chemical control available; use resistant varieties and control whiteflies.",
    "Tomato___Tomato_mosaic_virus": "No chemical control; use disease-free seeds and resistant varieties.",
    "Tomato___healthy": "Your tomato plant is healthy! No pesticides needed."
}

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        disease = request.form.get("disease")
        response = disease_pesticides.get(disease, "I'm not sure about that disease. Please check with an expert.")
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
