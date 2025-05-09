from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Disease-to-pesticide mapping
disease_pesticides = {
    "Apple___Apple_scab": "Apply fungicides like Captan or Mancozeb.",
    "Apple___Black_rot": "Use fungicides like Ziram or Captan.",
    "Apple___Cedar_apple_rust": "Use Myclobutanil or Sulfur-based sprays.",
    "Apple___healthy": "Your apple plant is healthy! No pesticides needed.",
    "Blueberry___healthy": "Your blueberry plant is healthy! No pesticides needed.",
    "Cherry_(including_sour)___healthy": "Your cherry plant is healthy! No pesticides needed.",
    "Cherry_(including_sour)___Powdery_mildew": "Use sulfur, neem oil, or potassium bicarbonate sprays.",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": "Apply fungicides such as azoxystrobin or propiconazole.",
    "Corn_(maize)___Common_rust_": "Use fungicides like Mancozeb or Trifloxystrobin.",
    "Corn_(maize)___healthy": "Your corn plant is healthy! No pesticides needed.",
    "Corn_(maize)___Northern_Leaf_Blight": "Use fungicides such as Pyraclostrobin or Propiconazole.",
    "Grape___Black_rot": "Apply Mancozeb or Myclobutanil.",
    "Grape___Esca_(Black_Measles)": "No effective chemical control; remove infected vines.",
    "Grape___healthy": "Your grape plant is healthy! No pesticides needed.",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": "Use fungicides like Captan or Mancozeb.",
    "Orange___Haunglongbing_(Citrus_greening)": "No cure available; control psyllid vectors and remove infected trees.",
    "Peach___Bacterial_spot": "Apply copper-based bactericides and choose resistant varieties.",
    "Peach___healthy": "Your peach plant is healthy! No pesticides needed.",
    "Pepper__bell___Bacterial_spot": "Use copper-based bactericides or streptomycin.",
    "Pepper__bell___healthy": "Your pepper plant is healthy! No pesticides needed.",
    "Potato___Early_blight": "Use Chlorothalonil or Mancozeb.",
    "Potato___healthy": "Your potato plant is healthy! No pesticides needed.",
    "Potato___Late_blight": "Apply Metalaxyl or Mancozeb.",
    "Raspberry___healthy": "Your raspberry plant is healthy! No pesticides needed.",
    "Soybean___healthy": "Your soybean crop is healthy! No pesticides needed.",
    "Squash___Powdery_mildew": "Use sulfur-based fungicides or neem oil.",
    "Strawberry___healthy": "Your strawberry plant is healthy! No pesticides needed.",
    "Strawberry___Leaf_scorch": "Use fungicides like Captan or Myclobutanil.",
    "Tomato___Bacterial_spot": "Copper-based fungicides like Copper Hydroxide or Copper Oxychloride.",
    "Tomato___Early_blight": "Use Chlorothalonil or Mancozeb-based fungicides.",
    "Tomato___healthy": "Your tomato plant is healthy! No pesticides needed.",
    "Tomato___Late_blight": "Apply Metalaxyl, Mancozeb, or Copper-based fungicides.",
    "Tomato___Leaf_Mold": "Use Chlorothalonil or Copper-based fungicides.",
    "Tomato___Septoria_leaf_spot": "Mancozeb, Chlorothalonil, or Copper fungicides are effective.",
    "Tomato___Spider_mites Two-spotted_spider_mite": "Apply Abamectin, Neem oil, or Sulfur-based miticides.",
    "Tomato___Target_Spot": "Use Chlorothalonil or Difenoconazole-based fungicides.",
    "Tomato___Tomato_mosaic_virus": "No chemical control; use disease-free seeds and resistant varieties.",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "No chemical control available; use resistant varieties and control whiteflies."
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
