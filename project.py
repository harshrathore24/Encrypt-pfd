import pikepdf
old_pdf =pikepdf.Pdf.open("harsh.pdf")
no_extr =pikepdf.Permissions(extract=False)
old_pdf.save("harsh1.pdf", encryption=pikepdf.Encryption(user="2411",
                                                         owner="wscude",
                                                         allow=no_extr))