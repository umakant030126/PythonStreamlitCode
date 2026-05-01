import streamlit as st

# ── MUST be the FIRST st.* call in your script ─────────────
st.set_page_config(
    page_title="QA Dashboard",          # Browser tab title
    page_icon="🛡️",                    # Favicon — emoji or image path
    layout="wide",                      # "centered" (default) or "wide"
    initial_sidebar_state="expanded",  # "expanded" or "collapsed"
    menu_items={                         # Custom hamburger menu items
        'Get Help': 'https://streamlit.io/docs',
        'About': "QA Dashboard built by Umakant Pandey"
    }
)

# Now the rest of your app code goes below
st.title("🛡️ QA Dashboard")

st.title("📊 QA KPI Dashboard")

# ── Three metric cards side by side ───────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Tests",
        value="52",
        delta="+8 from last sprint"   # Green arrow up
    )

with col2:
    st.metric(
        label="Tests Passed",
        value="47",
        delta="+5"   # Positive = green arrow ▲
    )

with col3:
    st.metric(
        label="Tests Failed",
        value="3",
        delta="-2",              # Negative = red arrow ▼
        delta_color="red"   # "inverse" = down is GOOD here! / "red" = mark in red color
    )

with col4:
    st.metric(
        label="Pass Rate",
        value="90.4%",
        delta="2.1%",
        delta_color="normal"    # "normal" (default), "inverse", "off"
    )