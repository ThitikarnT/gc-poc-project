# ใช้ภาพพื้นฐานที่ปลอดภัยและเบา
FROM python:3.9-slim

# ตั้งค่าโฟลเดอร์ทำงาน
WORKDIR /app

# ก๊อปปี้ไฟล์ทั้งหมดเข้าเครื่อง Server
COPY . .

# ติดตั้ง Library
RUN pip install --no-cache-dir -r requirements.txt

# เปิด Port 8080 สำหรับ Cloud Run
EXPOSE 8080

# คำสั่งรันแอป
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]