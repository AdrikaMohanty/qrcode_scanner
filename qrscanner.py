import qrcode
features = qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data("https://adrikamohanty.github.io/Adrika_Portfolio/")
features.make(fit=True)
generate_img = features.make_image(fill_color="black",back_color="white")
#myqr = qrcode.make("https://www.simplilearn.com/")
#myqr.save("myqr.png",scale = 8)

generate_img.save('image1.png')