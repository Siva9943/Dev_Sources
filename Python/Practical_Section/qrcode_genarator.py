import qrcode

url=input("Enter the text / url : ").strip()

file_path="G:\BroCode\Dev_Sources\Python\Practical_Section\qrcode.png"
qr=qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(file_path)
