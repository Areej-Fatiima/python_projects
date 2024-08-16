import qrcode

url = 'QR_generator' 

# Generate the QR code
code_image = qrcode.make(url)

save_path = 'E:/QR_Codes/my_qr_code.png'  

# Save the QR code image
code_image.save(save_path)

print(f"QR code saved as {save_path}")
