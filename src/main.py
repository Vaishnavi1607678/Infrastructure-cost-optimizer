from data_loader import load_data
from model import train_model, load_model
from optimizer import optimize_cost
import os

def main():
    data_path = 'data/sample_usage.csv'
    
    # Step 1: Load data
    df = load_data(data_path)
    print("Loaded data:")
    print(df)
    
    # Step 2: Train model
    if not os.path.exists('models/cost_optimizer_model.pkl'):
        print("Training model...")
        model = train_model(df)
    else:
        print("Loading existing model...")
        model = load_model()
    
    # Step 3: Get optimization recommendations
    recommendations = optimize_cost(df, model)
    
    print("\nCost Optimization Recommendations:")
    if recommendations.empty:
        print("No optimization recommendations found.")
    else:
        print(recommendations)

if __name__ == "__main__":
    main()

