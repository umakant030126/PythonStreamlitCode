import streamlit as st
import datetime

# ── Page Config — always first! ───────────────────────────
st.set_page_config(
    page_title="QA Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── SIDEBAR — Filters ─────────────────────────────────────
with st.sidebar:
    st.title("🛡️ QA Dashboard")
    st.caption("By Umakant Pandey")
    st.divider()

    project = st.selectbox(
        "Project:",
        ["ICAPS (Citi Bank)", "IBSG (Citi Bank)", "Lumen Sky"]
    )
    sprint = st.number_input("Sprint:", min_value=1, value=42)
    env = st.radio("Environment:",
                   ["DEV", "QA", "STAGING"], horizontal=True)
    date_range = st.date_input(
        "Test Window:",
        value=(datetime.date.today(), datetime.date.today())
    )
    st.divider()
    tester = st.text_input("Tester Name:", value="Umakant Pandey")

# ── MAIN AREA ─────────────────────────────────────────────
st.title(f"📊 {project} — Sprint {sprint} Report")
st.caption(f"Environment: {env}  |  Tester: {tester}")
st.divider()

# ── KPI CARDS row ─────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
with k1: st.metric("Total Tests",  "52",  "+8")
with k2: st.metric("Passed",       "47",  "+5")
with k3: st.metric("Failed",       "3",   "-2", delta_color="inverse")
with k4: st.metric("Pass Rate",    "90.4%", "↑2.1%")

st.divider()

# ── TABBED SECTIONS ───────────────────────────────────────
t1, t2, t3 = st.tabs(["✅ Test Cases", "🐛 Bugs", "📝 Add Report"])

with t1:
    left, right = st.columns([3, 1])
    with left:
        st.subheader("Test Case Results")
        data = {
            "TC ID":  ["TC-001","TC-002","TC-003","TC-004"],
            "Name":   ["Login","Logout","Dashboard","Export"],
            "Result": ["Pass","Pass","Fail","Pass"],
            "Time(s)":[2.3,1.1,5.8,3.2]
        }
        st.write(data)
    with right:
        st.subheader("Filter")
        st.radio("Show:", ["All","Pass","Fail"])

with t2:
    st.subheader("Open Bugs")
    bugs = [
        ("BUG-001", "Login fails on Chrome", "🔴 High"),
        ("BUG-002", "Dashboard timeout",    "🟡 Medium"),
        ("BUG-003", "Export button missing", "🟢 Low"),
    ]
    for bid, btitle, bsev in bugs:
        with st.expander(f"{bid}: {btitle} — {bsev}"):
            st.write(f"**Severity:** {bsev}")
            st.write("**Assigned to:** Umakant Pandey")
            st.text_area("Comment:", key=bid)

with t3:
    st.subheader("Add Test Report Entry")
    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Test Case ID:")
        st.selectbox("Result:", ["Pass","Fail","Blocked","Skip"])
    with c2:
        st.text_input("Test Case Name:")
        st.number_input("Execution time (s):", min_value=0.0, step=0.1)
    st.text_area("Notes / Error Description:")
    if st.button("📥 Submit Entry", type="primary"):
        st.success("✅ Report entry submitted successfully!")