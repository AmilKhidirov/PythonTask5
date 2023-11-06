from datetime import datetime

def yas_hesabla(dogum_tarixi):

    indiki_tarix = datetime.now()

    dogum_tarixi = datetime.strptime(dogum_tarixi, '%d-%m-%Y')

    fərq = indiki_tarix - dogum_tarixi

    il = fərq.days // 365
    ay = fərq.days // 30
    gun = fərq.days
    saat = fərq.days * 24
    deqiqe = fərq.days * 1140


    print(f"Siz heyatda  {il} il, {ay} ay, {gun} gün, {saat} saat, {deqiqe} dəqiqədir ki, movcudsunuz ve sizin {il} yasiniz var")


dogum_tarixi = input("Dogum tarixinizi 'DD-MM-YYYY' formatında daxil edin: ")


yas_hesabla(dogum_tarixi)