
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🚚 Multi-Objective Delivery Optimization")

# Sidebar weights
st.sidebar.header("Weights")
w1 = st.sidebar.slider("Cost Weight", 0.0, 1.0, 0.4)
w2 = st.sidebar.slider("Time Weight", 0.0, 1.0, 0.4)
w3 = st.sidebar.slider("Emission Weight", 0.0, 1.0, 0.2)

# Normalize weights
total = w1 + w2 + w3
if total > 0:
    w1, w2, w3 = w1/total, w2/total, w3/total

st.write("Click button to run optimization")

if st.button("Run Optimization"):
    
    st.success("Model executed successfully!")

    # ---- SAMPLE REALISTIC DATA (replace with your dataset if needed) ----
    np.random.seed(42)
    n = 50
    cost = np.random.uniform(10, 100, n)
    time = np.random.uniform(5, 50, n)
    emission = np.random.uniform(20, 200, n)

    # ---- SIMPLE OPTIMIZATION (weighted score) ----
    score = w1*cost + w2*time + w3*emission
    best_idx = np.argmin(score)

    best_cost = cost[best_idx]
    best_time = time[best_idx]
    best_emission = emission[best_idx]

    # Dummy comparison (you can replace with your full algorithms)
    final_df = pd.DataFrame({
        "Method": ["Best Solution"],
        "Cost": [round(best_cost,2)],
        "Time": [round(best_time,2)],
        "Emission": [round(best_emission,2)]
    })

    st.subheader("📊 Results")
    st.dataframe(final_df)

    # ---- Plot ----
    fig, ax = plt.subplots()
    ax.scatter(cost, time)
    ax.scatter(best_cost, best_time, marker='x')
    ax.set_xlabel("Cost")
    ax.set_ylabel("Time")
    ax.set_title("Cost vs Time")
    st.pyplot(fig)

