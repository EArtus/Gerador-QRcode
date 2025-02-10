import qrcode.constants
import streamlit as st
import qrcode 
from PIL import Image 
import io 


st.title('Gerador de QR code')
url = st.text_input('Cole sua Url aqui', placeholder='http://exemplo.com')

if url:
    qr = qrcode.QRCode(
        version= 1, 
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill__color="black", back_color="white")
    pill_img = img.get_image()

    st.image(pill_img, caption="Seu QRcode", use_container_width =True)

    buf = io.BytesIO()
    pill_img.save(buf, format="PNG")
    byte_im= buf.getvalue()

    st.download_button(
        label="Baixar QRcode",
        data= byte_im,
        file_name="qrcode.png",
        mime="Image/png",
    )