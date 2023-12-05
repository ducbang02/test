import streamlit as st
import joblib as jl
import numpy as np
###
st.title("Ứng Dụng Dự Đoán Điabetes")

# Load the model
model_path = 'diabetes.joblib'  # Đã sửa lại thành đuôi joblib
try:
    with open(model_path, 'rb') as input:
        model = jl.load(input)
    st.success("Mô hình đã được tải thành công!")
except Exception as e:
    st.error(f"Không thể tải mô hình. Lỗi: {e}")

# Tạo 8 text fields và lưu giá trị vào mảng input_data
input_data = []
for i in range(1, 9):
    value = st.text_input(f"Nhập giá trị {i}:", key=f"value{i}")
    if value:
        input_data.append(float(value))

# Kiểm tra nếu đã nhập đủ 8 giá trị
if len(input_data) == 8:
    st.success("Đã nhập đủ số lượng.")
    input_data = np.asarray(input_data).reshape(1, -1)  # Reshape thành mảng 2 chiều
    # Thực hiện dự đoán
    prediction = model.predict(input_data)
    # Hiển thị kết quả
    st.write("Kết quả dự đoán:")
    if prediction[0] == 0:
        st.write('The person is not diabetic')
    else:
        st.write('The person is diabetic')
else:
    st.warning("Hãy nhập đủ số lượng.")
