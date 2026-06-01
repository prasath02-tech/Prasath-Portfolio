import streamlit as st
import pathlib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Prasath A | Portfolio",
    page_icon="⚡",
    layout="wide"
)

# Path helper
BASE_DIR = pathlib.Path(__file__).resolve().parent

# Load CSS from root folder
def load_local_css(path):
    try:
        path = pathlib.Path(path)
        if path.exists():
            css = path.read_text(encoding="utf-8")
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except Exception:
        pass

load_local_css(BASE_DIR / "styles.css")

# ---------------- HERO SECTION ----------------
col1, col2 = st.columns([1, 3])

with col1:
    try:
        st.image("Profile.jpeg", width=220)
    except Exception:
        st.warning("Profile image not found.")
with col2:
    st.title("Prasath A")
    st.markdown("### Electronics & Communication Engineering Student")
    st.write("⚡ Embedded Systems | IoT | Networking | PCB Design")

    st.write("📧 prasatharivazhagan02@gmail.com")
    st.write("📱 8015341541")
    st.write("📍 Tamil Nadu, India")

    st.markdown(
        "<div class='social-links'>"
        "<a href='https://github.com/' target='_blank'>🌐 GitHub</a>"
        "<a href='https://www.linkedin.com/' target='_blank'>💼 LinkedIn</a>"
        "<a href='mailto:prasatharivazhagan02@gmail.com'>✉️ Email</a>"
        "</div>",
        unsafe_allow_html=True,
    )

# ---------------- ABOUT ----------------
st.markdown("---")
st.header("👨‍💻 About Me")

st.info("""
Passionate Electronics and Communication Engineering student with interests in
Embedded Systems, IoT, Networking, Software Testing, and Electronics Manufacturing.
Focused on building innovative technology solutions through practical engineering
and research-driven projects.
""")

# ---------------- SKILLS ----------------
st.markdown("---")
st.header("🛠 Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Languages")
    st.write("• C")
    st.write("• MATLAB")

    st.subheader("Hardware")
    st.write("• Arduino")
    st.write("• Raspberry Pi")
    st.write("• 8051 Microcontroller")
    st.write("• PCB Assembly")

with col2:
    st.subheader("Tools & Platforms")
    st.write("• MATLAB")
    st.write("• Simulink")
    st.write("• Proteus")
    st.write("• Tinkercad")

    st.subheader("Domains")
    st.write("• Embedded Systems")
    st.write("• IoT")
    st.write("• DSP")
    st.write("• Communication Systems")

st.subheader("Skill Levels")

st.write("Embedded Systems")
st.progress(90)

st.write("IoT Development")
st.progress(85)

st.write("Networking")
st.progress(80)

st.write("MATLAB & Simulink")
st.progress(75)

# ---------------- EDUCATION ----------------
st.markdown("---")
st.header("🎓 Education")

st.markdown("""
### Velalar College of Engineering and Technology
**B.Tech Electronics and Communication Engineering**

CGPA: **7.0**

2022 – 2026

### JKKN Matric Higher Secondary School

Science (PCMC)

Percentage: **70.6%**
""")

# ---------------- PROJECTS ----------------
st.markdown("---")
st.header("🚀 Projects")

with st.expander("🏥 SDN-Enabled Priority Aware Traffic Management"):
    st.write("""
    • Architected an SDN-based healthcare traffic management system.

    • Implemented priority-based routing for critical patient data.

    • Improved remote patient monitoring through low-latency transmission.
    """)

with st.expander("📢 Smart Digital Announcement Board"):
    st.write("""
    • Developed an IoT-based wireless digital notice board.

    • Built a web/mobile interface for remote updates.

    • Replaced traditional notice boards with an automated communication system.
    """)

# ---------------- INTERNSHIPS ----------------
st.markdown("---")
st.header("💼 Internships & Training")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    IIT Madras

    Advanced Electronics Manufacturing

    Power Electronics Fundamentals

    PCB Fundamentals
    """)

with col2:
    st.info("""
    Infosys Foundation

    Software Testing

    Quality Assurance

    Test Case Design
    """)

with col3:
    st.info("""
    Codebind Technologies

    HTML

    CSS

    JavaScript

    UI/UX Design
    """)

# ---------------- ACHIEVEMENTS ----------------
st.markdown("---")
st.header("🏆 Achievements")

st.success("Winner – Internal Smart India Hackathon (SIH) 2025")

st.success("Runner-Up – Project Expo 2024")

st.success("Published Research Paper at NIT Puducherry")

st.success("Presented Technical Papers at PSG iTech, Sona College of Technology and Karpagam College of Engineering")

# ---------------- CERTIFICATIONS ----------------
st.markdown("---")
st.header("📜 Certifications")

st.write("✔ Advanced Electronics Manufacturing (NCRF Level 5.5) – IIT Madras")

st.write("✔ Test Engineer Certification – Infosys Foundation")

st.write("✔ Web Development Training – Codebind Technologies")

# ---------------- LEADERSHIP ----------------
st.markdown("---")
st.header("🤝 Leadership & Extracurricular")

st.write("• Volunteer – Drone Challenge 2025")

st.write("• Volunteer – VCET Intramural Sports Fest")

# ---------------- PORTFOLIO STATS ----------------
st.markdown("---")
st.header("📊 Portfolio Highlights")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Projects", "2+")
c2.metric("Internships", "3")
c3.metric("Research Papers", "1")
c4.metric("Hackathons", "1")

# ---------------- CONTACT ----------------
st.markdown("---")
st.header("📬 Contact")

st.write("📧 prasatharivazhagan02@gmail.com")
st.write("📱 8015341541")
st.write("📍 Tamil Nadu, India")

# ---------------- RESUME DOWNLOAD ----------------
st.markdown("---")
st.header("📄 Resume")

try:
    with open("Prasath A_resume.pdf", "rb") as pdf_file:
        st.download_button(
            label="📄 Download Resume",
            data=pdf_file,
            file_name="Prasath_A_Resume.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.error("Resume file not found.")
