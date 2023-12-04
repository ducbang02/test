import streamlit as st
import pickle
import numpy as np

# Load the model
model_path = 'test.pkl'  # Thay đổi đường dẫn đến file model của bạn
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit app

st.title("Ứng Dụng Dự Đoán Điabetes")

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
    prediction = classifier.diabetes(input_data)
    # Hiển thị kết quả
    st.write("Kết quả dự đoán:")
    if (prediction[0] == 0):
      st.write('The person is not diabetic')
    else:
      st.write('The person is diabetic')
    
else:
    st.warning("Hãy nhập đủ số lượng.")

