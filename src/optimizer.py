def optimize_cost(df, model):
    X = df[['usage_hours', 'cost_per_hour']]
    df['predicted_cost'] = model.predict(X)
    
    # Calculate savings potential
    df['potential_savings'] = df['total_cost'] - df['predicted_cost']
    
    # Recommend optimization if potential savings > 5
    recommendations = df[df['potential_savings'] > 5][['resource_id', 'resource_type', 'total_cost', 'predicted_cost', 'potential_savings']]
    return recommendations

