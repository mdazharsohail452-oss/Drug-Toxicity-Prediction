Drug Toxicity Prediction using Machine Learning
📌 Overview

Drug development frequently fails due to unforeseen toxicity during later clinical stages.
This project focuses on early-stage toxicity prediction using machine learning and molecular descriptor data, helping identify potentially toxic drug candidates before costly experimental testing.

The model specifically predicts NR-AR (Androgen Receptor) toxicity, a key biological pathway evaluated in the Tox21 benchmark dataset.

🎯 Objectives
Predict potential drug toxicity using molecular descriptors
Handle extreme class imbalance in toxic vs non-toxic compounds
Identify molecular features contributing most to toxicity risk
Provide an interactive UI for real-time toxicity prediction
🧬 Dataset
Source: Tox21 dataset
Target Variable: NR-AR
0 → Non-toxic
1 → Toxic

⚙️ Methodology
Cleaned and filtered labeled data
Stratified train–test split
Feature scaling using StandardScaler
Random Forest classifier with class-weight balancing
Lowered decision threshold to improve toxic recall

📊 Results
Metric	       Value
ROC-AUC	       ~0.73
Toxic Recall	 ~0.48
Accuracy	     ~0.82

The model successfully detects a significant portion of toxic compounds, trading precision for higher recall, which is appropriate in pharmacological risk screening.

🧠 Interpretability

Feature importance analysis revealed that molecular size, polarity, and lipophilicity-related descriptors contribute most strongly to toxicity predictions.
This aligns with known receptor-binding and bioavailability mechanisms in pharmacology.
🛠️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
Streamlit
Joblib

👨‍🔬 Conclusion
This project demonstrates how machine learning can assist in early toxicity screening, reducing development costs and improving patient safety.
By combining robust ML techniques with interpretability and UI deployment, the system provides a practical foundation for AI-driven drug discovery workflows.
