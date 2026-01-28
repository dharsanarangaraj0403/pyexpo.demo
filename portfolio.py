import streamlit as st

# Page config
st.set_page_config(
    page_title="INNO_CORES Portfolio",
    page_icon="🌟",
    layout="centered"
)

# Sidebar
st.sidebar.title("🚀 Navigation")
menu = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "🙋 About", "🛠 Projects", "📞 Contact"]
)

# ---------------- HOME ----------------
if menu == "🏠 Home":
    st.title("👩‍💻 INNO_CORES")
    st.subheader("Aspiring Full Stack Developer")
    st.write(
        """
        Welcome to my **personal portfolio app** built using **Streamlit** 🚀  
        Here you can know about me, my projects, and contact me easily.
        """
    )

    st.info("💡 Built with Python & Streamlit")

# ---------------- ABOUT ----------------
elif menu == "🙋 About":
    st.header("📌 About Me")

    col1, col2 = st.columns(2)

    with col1:
        st.write("""
        - 🎓 Student & Beginner Full Stack Developer  
        - 🐍 Learning Python, C, Streamlit  
        - 🌐 Interested in Web & App Development  
        """)

    with col2:
        st.write("""
        **Skills**
        - Python  
        - C Programming  
        - Streamlit  
        - Basics of Git & GitHub  
        """)

# ---------------- PROJECTS ----------------
elif menu == "🛠 Projects":
    st.header("🛠 My Projects")

    st.markdown("### 🔹 Student Feedback System")
    st.write("A system to collect and analyze student feedback digitally.")

    st.markdown("### 🔹 Travel Content App")
    st.write("An app that displays travel places and content interactively.")

    st.markdown("### 🔹 GitHub Portfolio Website")
    st.write("A personal portfolio hosted using GitHub.")

# ---------------- CONTACT ----------------
elif menu == "📞 Contact":
    st.header("📞 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        msg = st.text_area("Your Message")

        submit = st.form_submit_button("Send Message")

        if submit:
            if name and email and msg:
                st.success("✅ Message sent successfully!")
            else:
                st.warning("⚠ Please fill all the fields.")
