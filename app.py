import streamlit as st

st.set_page_config(page_title="GC POC-GC: DevSecOps Dashboard", layout="wide")

st.title("🚀 GC Strategic Dashboard (DevSecOps POC)")
st.subheader("ระบบนี้ถูกตรวจสอบความปลอดภัยแบบ Automated 100%")

col1, col2 = st.columns(2)

with col1:
    st.info("🛡️ Security Status: Scanned by SonarQube & Trivy")
    st.success("✅ No Critical Vulnerabilities Found")

with col2:
    st.info("📦 Deployment: Google Cloud Run")
    st.write("Infrastructure as Code Ready")

user_name = st.text_input("กรุณาระบุชื่อผู้เข้าชมเพื่อทดสอบระบบ:")
if user_name:
    st.balloons()
    st.write(f"สวัสดีครับคุณ {user_name} ยินดีต้อนรับสู่ระบบต้นแบบของ GC")