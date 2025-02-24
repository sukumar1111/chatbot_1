from flask import Flask, render_template, request, jsonify
import time

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

# Crop improvement tips
crop_improvement_tips = [
    "Use well-drained soil rich in organic matter for better growth.",
    "Rotate crops to prevent soil-borne diseases and improve yield.",
    "Water early in the morning to avoid fungal infections.",
    "Use natural compost and fertilizers to enhance soil health.",
    "Control weeds regularly to prevent nutrient competition."
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.json
    disease = data.get("disease", "").strip()

    # Get pesticide recommendation
    pesticide = disease_pesticides.get(disease, "I am not sure about that disease. Please consult an expert.")

    # Provide random crop improvement tip
    tip = crop_improvement_tips[int(time.time()) % len(crop_improvement_tips)]

    return jsonify({"pesticide": pesticide, "tip": tip})

if __name__ == "__main__":
    app.run(debug=True)
