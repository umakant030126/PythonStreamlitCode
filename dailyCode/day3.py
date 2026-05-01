import time
import streamlit as st


st.header("Day three code of Streamlit leaning")
st.divider()

# st.columns() , st.sidebar() , st.expander() , st.tabs() , st.container() , st.empty()
st.title("Columns Code")

col1 , col2 , col3 =st.columns(3)
with col1:
    st.header("Column 1")
    st.write("Column one data")
    st.button("Button in Col1")

with col2:
    st.header("Column 2")
    st.write("Column two data")
    st.slider("A Slider :", 0,100,50)

with col3:
    st.header("Column 3")
    st.write("Column Three data")
    st.selectbox("Pick : ", ["A","B","C"])

st.divider()

# ── UNEQUAL columns using a list ──────────────────────────
# [2, 1] means left column is TWICE as wide as right column
# [1, 3, 1] means middle is 3x wider than the sides
left, right = st.columns([2, 1])

with left:
    st.subheader("Main Content (2x wide)")
    st.write("This column gets 2/3 of the page width.")

with right:
    st.subheader("Side Panel (1x)")
    st.write("This gets 1/3 of the page.")

st.divider()

# ── GAP parameter — adds space BETWEEN columns ────────────
c1, c2 = st.columns(2, gap="large")
# gap options: "small" (default), "medium", "large"

with c1:
    st.write("Left side with large gap")
with c2:
    st.write("Right side with large gap")

st.divider()
st.divider()

st.header("Side Bar demo")
with st.sidebar:
    st.header("Filters")
    st.divider()

    Project = st.selectbox("Select Project :", ["ICAPS", "IBSG", "Lumen Sky"])
    Env = st.selectbox("Select Env :", ["Dev" , "SIT" , "PROD"])
    show_passed = st.checkbox("Show Pass Tests", value = True)
    show_failed = st.checkbox("Show Failed Tests", value = True)

    st.divider()
    st.caption("QA Dash Board V1 | Umakant Pandey")

st.subheader(f"Result for {Project} and {Env}")
st.write(f"Showing Passed TC : {show_passed}")
st.write(f"Showing Failed TC : {show_failed}")

st.divider()

sprint = st.sidebar.number_input("Sprint number:", min_value=1, value=10)
st.write(f"Currently viewing Sprint {sprint}")


st.title("Expander Demo")
st.write("Main visible content is here. Expand sections below for details.")

# ── Basic expander — closed by default ────────────────────
with st.expander("📋 Click to see Test Steps"):
    st.write("Step 1: Login to application")
    st.write("Step 2: Navigate to dashboard")
    st.write("Step 3: Verify KPI cards display correctly")
    st.write("Step 4: Logout")

# ── Expander open by default using expanded=True ──────────
with st.expander("📊 Test Results Summary", expanded=True):
    st.success("✅ 47 tests Passed")
    st.error("❌ 3 tests Failed")
    st.warning("⚠️ 2 tests Blocked")

# ── Multiple expanders act like an accordion ───────────────
bugs = [
    {"id": "BUG-001", "title": "Login fails on Chrome", "severity": "High"},
    {"id": "BUG-002", "title": "Dashboard timeout",    "severity": "Medium"},
    {"id": "BUG-003", "title": "Export button missing", "severity": "Low"},
]

st.subheader("🐛 Bug Details")
for bug in bugs:
    with st.expander(f"{bug['id']} — {bug['title']}"):
        st.write(f"**Severity:** {bug['severity']}")
        st.write("**Status:** Open")
        st.write("**Assigned to:** Umakant Pandey")
        st.text_area("Add comment:", key=bug["id"])


st.title("🗂️ QA Report — Tabbed View")

# st.tabs() takes a list of tab names
# Returns a list of tab objects — unpack them!
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Summary",
    "🐛 Bug Report",
    "✅ Test Cases",
    "⚙️ Settings"
])

with tab1:
    st.header("Test Execution Summary")
    st.success("Total Tests: 52 | Passed: 47 | Failed: 3 | Blocked: 2")
    st.write("Overall pass rate: 90.4%")

with tab2:
    st.header("Bug Report")
    st.error("3 open bugs found in this sprint")
    st.write("• BUG-001: Login fails on Chrome — HIGH")
    st.write("• BUG-002: Dashboard timeout — MEDIUM")
    st.write("• BUG-003: Export button missing — LOW")

with tab3:
    st.header("Test Case List")
    tc_data = {
        "Test ID": ["TC-001", "TC-002", "TC-003"],
        "Name":    ["Login Test", "Logout Test", "Dashboard Load"],
        "Status":  ["Pass", "Pass", "Fail"]
    }
    st.write(tc_data)   # st.write shows dicts as a nice table!

with tab4:
    st.header("Settings")
    st.selectbox("Theme:", ["Light", "Dark"])
    st.checkbox("Email notifications", value=True)
    st.text_input("Your email:")



st.title("Container Demo")

# ── Use case 1: Logical grouping ──────────────────────────
with st.container():
    st.subheader("Section A — Inputs")
    st.text_input("Name:")
    st.number_input("Age:", value=25)

with st.container():
    st.subheader("Section B — Options")
    st.selectbox("Role:", ["QA Engineer", "Developer"])
    st.checkbox("Active employee")

st.divider()

# ── Use case 2: Add border around a container ─────────────
# border=True draws a visible box around the container
with st.container(border=True):
    st.subheader("🧪 Test Run #42")
    st.write("Environment: QA")
    st.write("Status: In Progress")
    st.progress(0.65)  # Shows a 65% filled progress bar

st.divider()

# ── Use case 3: Out-of-order writing ─────────────────────
# Create a container FIRST, then fill it LATER in the code!
result_box = st.container()  # Reserve the spot at the top

st.write("This line appears BELOW the result box on screen.")
name = st.text_input("Type your name:")

# Write INTO the container (appears at top, even though code is at bottom!)
with result_box:
    st.success(f"👋 Hello, {name or 'stranger'}!")


st.title("Empty Placeholder Demo")

# ── Use case 1: Dynamic status message ────────────────────
status = st.empty()   # Reserve a spot
status.info("⏳ Ready to start...")  # Initial state

if st.button("Run Test Suite"):
    status.warning("🔄 Tests running...")
    time.sleep(2)   # Simulate test execution
    status.success("✅ All tests complete!")

st.divider()

# ── Use case 2: Countdown timer ───────────────────────────
if st.button("Start 5-second countdown"):
    placeholder = st.empty()
    for i in range(5, 0, -1):
        placeholder.metric("Countdown", f"{i} seconds")
        time.sleep(1)
    placeholder.success("🚀 Launch!")

st.divider()

# ── Use case 3: Clear a message ───────────────────────────
msg = st.empty()
if st.button("Show message"):
    msg.success("Hello!")
if st.button("Clear message"):
    msg.empty()  # Call .empty() on it to CLEAR the content