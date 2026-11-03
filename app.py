import streamlit as st

st.set_page_config(page_title="Market Risk Analysis", layout="wide")

st.title("Market Risk Analysis")
st.markdown(
    """
    Cette application explore le comportement statistique des rendements financiers.

    - **Market Data** : prix historiques et rendements logarithmiques
    - **Risk Explorer** : covariance, corrélation et ellipse de covariance
    - **Gaussian Simulator** : comparaison avec un modèle gaussien

    Choisis une page dans la barre latérale.
    """
)