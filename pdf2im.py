import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import os

# Judul aplikasi
st.title("PDF to JPG Converter")

# Fungsi untuk menyimpan gambar
def save_image(pages):
    if not os.path.exists('output_images'):
        os.makedirs('output_images')
    
    # Gabungkan dua halaman menjadi satu gambar
    widths, heights = zip(*(i.size for i in pages))
    total_width = max(widths)
    total_height = sum(heights)

    new_image = Image.new('RGB', (total_width, total_height))

    y_offset = 0
    for page in pages:
        new_image.paste(page, (0, y_offset))
        y_offset += page.size[1]

    new_image.save('output_images/combined_image.jpg', 'JPEG')
    st.success("Image saved successfully in 'output_images' folder as combined_image.jpg")

# Unggah file PDF
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Simpan file PDF yang diunggah ke disk
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Tampilkan tombol untuk mengonversi PDF
    if st.button("Convert PDF to JPG"):
        pages = convert_from_path('temp.pdf', first_page=1, last_page=2)
        save_image(pages)
        st.write("Conversion done!")
