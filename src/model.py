from sklearn.linear_model import LinearRegression
import joblib

def train_model(df):
    X = df[['usage_hours', 'cost_per_hour']]
    y = df['total_cost']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Save the model
    joblib.dump(model, 'models/cost_optimizer_model.pkl')
    return model

def load_model():
    return joblib.load('models/cost_optimizer_model.pkl')

