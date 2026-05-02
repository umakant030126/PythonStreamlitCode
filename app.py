import streamlit as st
import pandas as pd

st.title("st.write() with Different Data Types")

# ── Passing a DataFrame ───────────────────────────────────
df = pd.DataFrame({
    "Name":   ["Umakant", "Ravi", "Priya"],
    "Role":   ["QA Lead", "Dev", "BA"],
    "Score":  [95, 88, 91]
})

st.subheader("DataFrame → shows as interactive table")
st.write(df)   # Automatic — renders as a nice sortable table

st.divider()

# ── Passing a dictionary ──────────────────────────────────
st.subheader("Dict → shows as JSON-style")
st.write({"project": "ICAPS", "sprint": 42, "pass_rate": "90%"})

st.divider()

# ── Passing a list ────────────────────────────────────────
st.subheader("List → shows as a list")
st.write(["Selenium", "Postman", "Jira", "SQL"])

st.divider()

# ── Mixing text AND data in one call ──────────────────────
st.write("The DataFrame has", df.shape[0], "rows and", df.shape[1], "columns.")