# Infrastructure-cost-optimizer

## AI-Based Infrastructure Cost Optimizer

This project helps identify cloud cost-saving opportunities across AWS services like EC2, RDS, and S3 by analyzing infrastructure usage. Using a trained AI model, it predicts optimized costs and suggests where spending can be reduced — all visualized through a user-friendly Streamlit dashboard.

## Problem Statement
Cloud resources are often over-provisioned or under-utilized, leading to unnecessary costs. This tool uses machine learning to:
- Analyze usage data (hours, cost per hour)
- Predict what the optimized cost should be
- Calculate the difference (potential savings)
- Show all insights via a live dashboard

## Features
- AI-based cost prediction model trained using `scikit-learn`
- Streamlit dashboard to visualize costs, savings, and resource insights
- CSV-based input for usage data (can be extended to real AWS billing API)
- Easy deployment on AWS EC2
- Lightweight and fast to run

## Tech Stack

| Component         | Technology        |
|------------------|-------------------|
|  Model          | scikit-learn      |
|  Dashboard      | Streamlit         |
|  Data Analysis  | pandas, joblib    |
|  Deployment     | AWS EC2 (Ubuntu)  |
|  Language       | Python 3.12       |


## How It Works

1. Data Input: `usage_data.csv` contains:
   - `resource_id`, `resource_type`, `usage_hours`, `cost_per_hour`, `total_cost`

2. Model Training:
   - Linear Regression learns to predict `total_cost` from usage patterns

3. Cost Optimization:
   - `predicted_cost` is computed
   - `potential_savings = total_cost - predicted_cost`

4. Dashboard:
   - View total cost vs predicted
   - See filtered savings suggestions

## How to Run (Locally or on EC2)

### 1. Clone and Set Up Environment

```bash
git clone https://github.com/Vaishnavi1607678/Infrastructure-cost-optimizer.git
cd Infrastructure-cost-optimizer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

### 2. Train the Model

```bash
python3 src/main.py
```
This saves the trained model to: `models/cost_optimizer_model.pkl`

### 3. Launch the Dashboard

```bash
streamlit run src/dashboard.py --server.enableCORS false --server.enableXsrfProtection false --server.port 8501 --server.address 0.0.0.0
```

Then visit in browser:

```
http://<your-ec2-public-ip>:8501
```

---

## Example Output

| resource\_id | resource\_type | usage\_hours | total\_cost | predicted\_cost | potential\_savings |
| ------------ | -------------- | ------------ | ----------- | --------------- | ------------------ |
| r1           | EC2            | 12           | ₹24.00      | ₹17.92          | ₹6.08              |
| r2           | RDS            | 20           | ₹100.00     | ₹77.91          | ₹22.09             |

---

## Future Enhancements

* Integrate AWS Cost Explorer API to fetch real billing data
* Add Docker + GitHub Actions for CI/CD
* Auto email alerts for high-cost resources
* Add OAuth login to protect dashboard

---


