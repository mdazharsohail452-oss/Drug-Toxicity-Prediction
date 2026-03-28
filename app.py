import streamlit as st
import numpy as np
import joblib

st.set_page_config(
    page_title="Drug Toxicity Prediction",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.markdown("""
<style>
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {
    padding-top: 2rem;
}

body {
    background: linear-gradient(135deg, #0a0f1e, #111827, #020617);
    color: #e5e7eb;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}
.title {
    text-align: center;
    font-size: 2.4rem;
    font-weight: 800;
    color: #fff012;
    margin-bottom: 4px;
}

.subtitle {
    text-align: center;
    font-size: 1rem;
    color:white;
    margin-bottom: 28px;
}

/* Section label */
.section {
    color: #844fc1;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 10px;
}

/* Footer */
.footer {
    text-align: center;
    color: #b5bcc4;
    font-size: 0.85rem;
    margin-top: 18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = joblib.load("tox_model.pkl")
scaler = joblib.load("tox_scaler.pkl")
features = joblib.load("feature_names.pkl")

# ---------------- UI ----------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown('<div class="title">🧪 AI-Driven Drug Toxicity Prediction for Safer Drug Discovery</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">NR-AR Receptor Toxicity Risk Estimation</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="section">Molecular Descriptor Inputs</div>', unsafe_allow_html=True)

inputs = []
for f in features:
    val = st.number_input(
        f,
        value=0.0,
        format="%.4f"
    )
    inputs.append(val)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Predict Toxicity", use_container_width=True):
    X = np.array(inputs).reshape(1, -1)
    X_scaled = scaler.transform(X)

    prob = model.predict_proba(X_scaled)[0][1]
    prediction = int(prob >= 0.25)  # safety-focused threshold

    st.markdown("---")
    st.subheader("Prediction Result")

    st.metric("Toxicity Risk Probability", f"{prob:.2%}")

    if prediction == 1:
        st.error("⚠️Potentially Toxic Compound")
    else:
        st.success("✅ Likely Non-Toxic Compound")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="footer">AI for Safer and Smarter Drug Development</div>',
    unsafe_allow_html=True
)
