from flask import Flask, jsonify
from data_loader import load_data
from model import train_model, load_model
from optimizer import optimize_cost
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the AI Infrastructure Cost Optimizer!"

@app.route("/optimize", methods=["GET"])
def get_optimization():
    data_path = 'data/sample_usage.csv'
    df = load_data(data_path)

    if not os.path.exists('models/cost_optimizer_model.pkl'):
        model = train_model(df)
    else:
        model = load_model()

    recommendations = optimize_cost(df, model)

    if recommendations.empty:
        return jsonify({"message": "No cost-saving recommendations found."})
    
    return recommendations.to_json(orient="records")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

