import streamlit as st

st.title("Hello, World! 🌍")
st.write("I am Umakant and I am QA.")
st.write("Started learning Python stremlit along with Python.")


# ── TITLE: The biggest heading on the page ──────────────────
st.title("I am the Title — Big and Bold!")

# ── HEADER: Second level heading ────────────────────────────
st.header("I am a Header — Slightly Smaller")

# ── SUBHEADER: Third level heading ──────────────────────────
st.subheader("I am a Subheader — Even Smaller")

# ── WRITE: General purpose display ──────────────────────────
st.write("Hello! I can show text, numbers, even Python objects.")
st.write(42)                         # It shows the number 42
st.write([1, 2, 3])                  # It shows a list!

# ── TEXT: Plain text, no formatting ─────────────────────────
st.text("I am plain monospace text. Like a console output.")

# ── MARKDOWN: Write formatted text using Markdown syntax ────
st.markdown("**Bold text**, *italic text*, and `code text`")
st.markdown("## This is a Markdown Heading Level 2")
st.markdown("- Item 1\n- Item 2\n- Item 3")  # Bullet list!

# ── CAPTION: Small grey text, like footnotes ────────────────
st.caption("I am small grey text — good for footnotes or hints.")

# ── CODE: Shows code with syntax highlighting ───────────────
st.code("""
def greet(name):
    return f"Hello, {name}!"
""", language="python")

# ── DIVIDER: A horizontal line to separate sections ─────────
st.divider()   # Draws a horizontal line

# ── LATEX: For math formulas ─────────────────────────────────
st.latex(r"E = mc^2")  # Shows Einstein's formula beautifully!