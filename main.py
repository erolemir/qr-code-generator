# qrcode kütühanesini import ediyoruz
import qrcode

# değişken tanımlayıp yap komutunu kullanıyoruz.
code = qrcode.make(input('istediğiniz şey: '))
#kaydet komutunu kullanıyoruz.
code.save('kodunuz.png')

