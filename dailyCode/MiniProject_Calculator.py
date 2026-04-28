import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")
st.caption("Day 2 - Mini project => 'Build with Streamlit Widget'")
st.divider()

# Widget 1
num1 = st.number_input("First Number : ",value= 0.0, step = 1.0)

# Widget 2
operation = st.radio("Select Operation : ", ["➕ Add", "➖ Subtract", "✖️ Multiply", "➗ Divide"], horizontal=True)

# Widget 3
num2 = st.number_input("Second Number : ", value= 0.0, step=1.0)

# Widget 4: Optional checkbox to show steps
show_steps = st.checkbox("Show calculation steps")

st.divider()

if st.button("Calculate",type="primary"):
    if "Add" in operation:
        result, symbol = num1 + num2 , "+"
    elif "Subtract" in operation:
        result, symbol = num1 - num2, "-"
    elif "Multiply" in operation:
        result, symbol = num1 * num2, "*"
    else:
        if num2 == 0:
            st.error("Can not divided by zero!")
            st.stop()
        result , symbol = num1 / num2 , "/"

    if show_steps:
        st.info(f"Step : {num1} {symbol} {num2} = ?")

    st.success(f"Answer : {num1} {symbol} {num2} = **{result}**")