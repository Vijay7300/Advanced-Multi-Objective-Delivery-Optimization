
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🚚 Multi-Objective Delivery Optimization")

st.sidebar.header("Weights")
w1 = st.sidebar.slider("Cost Weight", 0.0, 1.0, 0.4)
w2 = st.sidebar.slider("Time Weight", 0.0, 1.0, 0.4)
w3 = st.sidebar.slider("Emission Weight", 0.0, 1.0, 0.2)

st.write("Click button to run optimization")

if st.button("Run Optimization"):
    st.success("Model executed successfully!")

    # Dummy output (replace with your real code)
    data = pd.DataFrame({
        "Method": ["NSGA-II", "PSO"],
        "Cost": [100, 120],
        "Time": [50, 40]
    })

    st.dataframe(data)

    fig, ax = plt.subplots()
    ax.scatter([100,120], [50,40])
    ax.set_xlabel("Cost")
    ax.set_ylabel("Time")
    st.pyplot(fig)
