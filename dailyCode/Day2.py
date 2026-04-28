import datetime

import streamlit as st
st.title("Welcome to Umakant Pandey world..  :-)")
st.divider()
st.header("We are learning Python here : DAY 2")
# st.markdown("**Here are** `hello world` **program**" )
# st.code('''def greet(username):
# print(f"Hello {username}")
# ''')
#
# st.divider()
# st.divider()
# st.header("Here are few details about Widget.")
# user_val = st.some_widget("Label shown here")
# st.write("You choose :",user_val)

clicked = st.button("Click me")
if clicked:
    st.write("You clicked here...!")
else:
    st.write("Not clicked yet...!")

# type="primary" makes it a bold coloured button
if st.button("Submit Report", type="primary"):
    st.success("✅ Report submitted successfully!")

st.button("I am disabled", disabled=True)

st.divider()

name  = st.text_input("Enter you name here : ")
if name:
    st.write(f"Hello , {name}")
else:
    st.write("Enter your name above...!")

# With value (pre-filled default) and placeholder (hint text)
city = st.text_input(
    "Your city:",
    value="New Delhi",           # Already filled on load
    placeholder="Type city name...", # Grey hint text
    max_chars=50                 # Can't type more than 50 chars
)
st.write("City entered:", city)

# Password field — hides what the user types!
password = st.text_input("Enter password:", type="password")
if password:
    st.write("Password length:", len(password), "characters")

st.divider()

st.title("Text Area Demo")

feedback = st.text_area(
    "Write your feedback:",
    placeholder="Tell us what you think...",
    height=150   # Height of the text box in pixels
)

if feedback:
    word_count = len(feedback.split())
    char_count = len(feedback)
    st.write(f"Words: {word_count}  |  Characters: {char_count}")
    st.info(feedback)  # Show feedback in a blue box

st.title("Number Input Demo")

# Integer number
age = st.number_input(
    "Enter your age:",
    min_value=1,       # Can't go below 1
    max_value=120,     # Can't go above 120
    value=25,          # Default value
    step=1             # Each arrow click adds/subtracts 1
)
st.write(f"You are {age} years old.")

st.divider()

# Float (decimal) number
salary = st.number_input(
    "Monthly salary (INR):",
    min_value=0.0,
    value=50000.0,
    step=1000.0,
    format="%.2f"    # Show exactly 2 decimal places
)
annual = salary * 12
st.write(f"Annual CTC: ₹{annual:,.0f}")

st.title("Slider Demo")

# Single value slider
# Arguments in order: label, min, max, default value
age = st.slider("Select your age:", 1, 100, 25)
st.write(f"Age: {age}")

st.divider()

# Range slider — pass a TUPLE as default value!
# Returns a tuple (low, high) — two handles appear
salary_range = st.slider(
    "Expected salary range (₹K):",
    min_value=10,
    max_value=200,
    value=(30, 80)   # Tuple = range slider with 2 handles!
)
st.write(f"Looking for: ₹{salary_range[0]}K to ₹{salary_range[1]}K")

st.divider()

# Float slider with step
rating = st.slider("Rate this course:", 0.0, 5.0, 4.5, 0.5)
#                   label,             min,  max,  default, step
st.write(f"Rating: {'⭐' * int(rating)} ({rating}/5)")


st.title("Selectbox Demo")

# Pass a list of options
dept = st.selectbox(
    "Choose your department:",
    ["QA Testing", "Development", "DevOps", "Management"]
)
st.write(f"You selected: {dept}")

st.divider()

# index=0 means first item is default
lang = st.selectbox(
    "Favourite programming language:",
    ["Python", "Java", "JavaScript", "SQL"],
    index=0
)

# Use selection in Python logic — like a switch/match!
tips = {
    "Python":     "Great for data, automation, and QA scripting!",
    "Java":       "Your Selenium scripts run on this!",
    "JavaScript": "King of the browser — used in web testing.",
    "SQL":        "Essential for database testing — you already know this!"
}
st.info(tips[lang])

st.title("Multiselect Demo")

skills = st.multiselect(
    "Select your QA skills:",
    ["Selenium", "Postman", "Jira", "SQL", "Jenkins", "Python", "TestNG"],
    default=["Selenium", "Postman"]  # Pre-selected items
)

# skills is ALWAYS a list
# Empty selection → skills = []
# 3 items picked → skills = ["Selenium", "SQL", "Python"]

if skills:
    st.write(f"You selected {len(skills)} skill(s):")
    for skill in skills:
        st.write(f"  ✅ {skill}")
else:
    st.warning("Please select at least one skill!")


st.title("Checkbox Demo")

# Unchecked by default (value defaults to False)
agree = st.checkbox("I agree to the terms and conditions")

if agree:
    st.success("✅ Thank you for agreeing!")
else:
    st.warning("⚠️ Please accept terms to continue.")

st.divider()

# Checked by default using value=True
show_details = st.checkbox("Show advanced details", value=True)

if show_details:
    st.write("🔍 Advanced details: Experience = 8+ years, Domain = Banking")

st.divider()

# Great use case: show/hide a section
show_raw = st.checkbox("Show raw data")
data = {"name": "Umakant", "exp": "8 years", "role": "QA Engineer"}
if show_raw:
    st.write(data)   # st.write can display dicts as a table!


st.title("Radio Button Demo")

experience = st.radio(
    "Your experience level:",
    ["Beginner (0-2 yrs)", "Intermediate (2-5 yrs)", "Senior (5+ yrs)"],
    index=2   # Default: 3rd option (Senior) selected
)
st.write(f"Level: {experience}")

st.divider()

# horizontal=True puts all options side by side in one row
result = st.radio(
    "Test result:",
    ["✅ Pass", "❌ Fail", "⏸️ Blocked"],
    horizontal=True
)
st.write("Result marked:", result)


st.title("Date and Time Demo")

dob = st.date_input("Date of Birth : ", value = datetime.date(1990,1,1),
                    min_value = datetime.date(1950,1,1),
                    max_value = datetime.date.today())
age_days = (datetime.date.today()-dob).days
st.write(f"You are {age_days//365} years old...!")

st.divider()

# Time picker
meeting_time = st.time_input(
    "Schedule standup meeting:",
    value=datetime.time(10, 0)   # Default: 10:00 AM
)
st.write(f"Meeting at: {meeting_time}")

st.divider()

# Date RANGE picker — pass a tuple as value!
date_range = st.date_input(
    "Test execution window:",
    value=(datetime.date.today(), datetime.date.today())
)
if len(date_range) == 2:
    st.write(f"Testing from {date_range[0]} to {date_range[1]}")