import re

pos_adj = ['muthis','harika','idare eder','guzel','akli','aktif','alakadar','alakali','alisilmis','analitik','animsatici','antrenmanli','atak','aydinlatici','ayrintici','bagdastirici','bagimsiz','berk','betimleyici','bilindik','bilinen','bilissel','birinci','bitirim','ciddi',
        'curetkar','cabuk','cocuk ruhlu','cogulcu','cok yonlu','cozumlemeci','dayanakli','denetimli','dengeci','denk','destekci','detayli','diplomali','disiplinli','dogal','dominant','duyarli','dusunceli','eriskin','gercekci','gururlu',
        'haberli','hareketli','hassas','hatirlatici','hesapci','heyecanli','idareci','iddiali','ilgili','itaatkar','itaatli','kararli','kendi halinde','kuralli','mantiksal','metotlu','net','normal','organize','otoriteli','otoriter','olculu','mutevazi','caliskan',
        'oncelikli','parlak','pozitif','sakin','sistematik','sistemli','standartli','tarafsiz','toleransli','uyanik','yardimci','yatistirici','yatkin','dengeli','duygusal','etkili','gonullu','is birlikci','verimli','nazik','komik','bilge','akilli',
        'narin','planli','programli','sabirli','teskilatli','tutkulu','uzlasmaci','aciklayici','becerikli','bilgili','bilincli','cesaretli','dayanikli','degerli','deneyimli','dikkatli','dinamik','disiplinli','duyarli','durust','duzenli','duzeyli',
        'egitimli','gayretli','hazirlikli','sorunsuz','idealist','ileri goruslu','istekli','ise uygun','iyi','kidemli','mantikli','nezaketli','nitelikli','prezantabl','profesyonel','sagduyulu','tedbirli','temkinli','uzman','vasifli','yaratici','adaletli','adil',
        'akilli','caliskan','dakik','enerjik','hakli','kaliteli','optimist','olumlu','rasyonel','tutarli','uyumlu','uretken','verimli','yararli','yardimsever','yenilikci','yetenekli']
neg_adj = ['mahvetti','mahvolmus','kotu','sorun','problem','fena','abartili','acgozlu','adaletsiz','agresif','agzi bozuk','ahlak disi','ahlaksiz','ahmak','ahmakca','akillara zarar','akillanmaz','alayci','aptal','aptalca','ara bozucu','arsiz','art niyetli','asagilik',
        'barbar','bombok','bozgun','bozuk','cani','cildirtici','cozumsuz','daginik','diktator','duzenbaz','duzensiz','eksik','eski','gecersiz','gulunc','gurultu','guvensiz','hadsiz','hain','hevessiz','iki yuzlu','istikrarsiz','islevsiz',
        'kalitesiz','kansiz','karaktersiz','kirilgan','kiskanc','kisiliksiz','kof','korkutucu','korkunc','kullanissiz','limoni','madara','medeniyetsiz','olumsuz','plansiz','problem','ruhsuz','sapik','sarsak','sonucsuz','seytan',
        'tecrubesiz','tekinsiz','tembel','temelsiz','terbiyesiz','ters ters','tertipsiz','tiksindirici','tutarsiz','ukala','utandirici','utanmaz','uyusuk','uyumsuz','uygunsuz','uyduruk','ustunkoru','usengec','uzucu','vahim','verimsiz',
        'yalaka','yalanci','yanlis','yapmacik','yaltak','yaramaz','yararsiz','yilisik','yuz kizartici','asik yuzlu','yuzsuz','zararli','zevksiz','zevzek','zirdeli','zorba',
        'acemi','agir aksak','agzi gevsek','anlayissiz','antipatik','asabi','asalak','asik suratli','asagilayici','avanak','azimsiz','bakimsiz','basiretsiz','basarisiz','beceriksiz','bencil','berbat','bilincsiz','bilmis bilmis',
        'bilgisiz','boktan','bosbogaz','budala','burnu havada','cadaloz','bunaltici','can sikici','ciddiyetsiz','cenesi dusuk','cenesiz','cirkef','cirkin','cokbilmis','dalgaci','dalkavuk','dangalak','dar kafali','darmadaginik',
        'dayaklik','deli','deneyimsiz','demode','degersiz','dedikoducu','despot','disiplinsiz','dikkatsiz','duyarsiz','dusman','duzensiz','eften puften','egitimsiz','embesil','engelli','eski kafali','ezik','felaket','gaddar','gammaz',
        'gayretsiz','gorgusuz','gucsuz','hatali','hilebaz','hosgorusuz','hosnutsuz','huysuz','igrenc','ilkel','incitici','iradesiz','issiz','kaba','kafasiz','kalpsiz','kanunsuz','kirli','korkak','kustah','kusurlu','kompleksli']


def remove_special_characters(entry):
    entry = entry.lower()
    entry = re.sub(r"[^a-zA-Z ]+", ' ', entry)
    string_length=len(entry)+1    
    string_revised=entry.ljust(string_length)
    return entry

def convert_turkish_letters(entry):
    entry = entry.replace('ş', 's')
    entry = entry.replace('ı', 'i')
    entry = entry.replace('ğ', 'g')
    entry = entry.replace('ö', 'o')
    entry = entry.replace('ç', 'c')
    entry = entry.replace('ü', 'u')
    return entry

tr_stops = ['a', 'acaba', 'alti', 'altmis', 'ama', 'ancak', 'arada', 'artik', 'aslinda', 'aslinda', 'ayrica', 'az', 'bana', 'bazen', 'bazi', 'bazilari', 'belki', 'ben', 'benden', 'beni',
         'benim', 'beri', 'bes', 'bile', 'bilhassa', 'bin', 'bir', 'biraz', 'bircogu', 'bircok', 'biri', 'birisi', 'birkac', 'birsey', 'biz', 'bizden', 'bize', 'bizi', 'bizim', 'boyle', 
         'boylece', 'bu', 'buna', 'bunda', 'bundan', 'bunlar', 'bunlari', 'bunlarin', 'bunu', 'bunun', 'burada', 'butun', 'cogu', 'cogunu', 'cok', 'cunku', 'da', 'daha', 'dahi', 'dan',
          'de', 'defa', 'diger', 'digeri', 'digerleri', 'diye', 'doksan', 'dokuz', 'dolayi', 'dolayisiyla', 'dort', 'e', 'edecek', 'eden', 'ederek', 'eger', 'elbette', 'elli', 'en', 'etmesi', 'ettigi', 'ettigini', 'fakat', 'falan', 'filan', 'gene', 'geregi', 'gerek', 'gibi', 'gore', 'hala', 'halde', 'halen', 'hangi', 'hangisi', 'hani', 'hatta', 'hem', 'henuz', 'hep', 'hepsi', 'her', 'herhangi', 'herkes', 'herkese', 'herkesi', 'herkesin', 'hic', 'hicbir', 'hicbiri', 'i', 'i', 'icin', 'icinde', 'iki', 'ile', 'ilgili', 'ise', 'iste', 'itibaren', 'itibariyle', 'kac', 'kadar', 'karsin', 'kendi', 'kendilerine', 'kendine', 'kendini', 'kendisi', 'kendisine', 'kendisini', 'kez', 'ki', 'kim', 'kime', 'kimi', 'kimin', 'kimisi', 'kimse', 'kirk', 'madem', 'mi', 'mi', 'milyar', 'milyon', 'mu', 'mu', 'nasil', 'ne', 'neden', 'nedenle', 'nerde', 'nerede', 'nereye', 'neyse', 'nicin', 'nin', 'nin', 'niye', 'nun', 'nun', 'o', 'obur', 'olan', 'olarak', 'oldugu', 'oldugunu', 'olduklarini', 'olmadigi', 'olmak', 'olmasi', 'olsa', 'olsun', 'olup', 'olursa', 'on', 'on', 'ona', 'once', 'ondan', 'onlar', 'onlara', 'onlardan', 'onlari', 'onlarin', 'onu', 'onun', 'orada', 'ote', 'oturu', 'otuz', 'oyle', 'oysa', 'pek', 'ragmen', 'sana', 'sanki', 'sanki', 'sayet', 'sekilde', 'sekiz', 'seksen', 'sen', 'senden', 'seni', 'senin', 'sey', 'seyden', 'seye', 'seyi', 'seyler', 'simdi', 'siz', 'siz', 'sizden', 'sizden', 'size', 'sizi', 'sizi', 'sizin', 'sizin', 'sonra', 'soyle', 'su', 'suna', 'sunlari', 'sunu', 'ta', 'tabii', 'tam', 'tamam', 'tamamen', 'tarafindan', 'trilyon', 'tum', 'tumu', 'u', 'u', 'uc', 'un', 'un', 'uzere', 'var', 'vardi', 've', 'veya', 'ya', 'yani', 'yapilan', 'yapilmasi', 'yapmak', 'yaptigi', 'yaptigini', 'yaptiklari', 'ye', 'yedi', 'yerine', 'yetmis', 'yi', 'yi', 'yine', 'yirmi', 'yoksa', 'yu', 'yuz', 'zaten', 'zira', 'zxtest', '', 'film ', 'filmi ', 'filmin', 'filme', 'filmde', 'gibi', 'bu', 'ben', 'olan', 'diye', 'sadece', 'sonra', 'her', 'olarak']

def remove_stopwords(entry):
    entry = ' '.join([word for word in entry.split() if word not in tr_stops])
    return entry


def remove_suffix(sentence):
    entry = sentence
    entry = entry.replace('sin ', ' ')
    entry = entry.replace('sun ', ' ')
    entry = entry.replace('imiz ', ' ')
    entry = entry.replace('umuz ', ' ')
    entry = entry.replace('ydi ', ' ')
    entry = entry.replace('ydu ', ' ')

    entry = entry.replace('di  ', ' ')
    entry = entry.replace('du  ', ' ')
    entry = entry.replace('tir  ', ' ')
    entry = entry.replace('tur  ', ' ')
    entry = entry.replace('ti  ', ' ')
    entry = entry.replace('tu  ', ' ')
    entry = entry.replace('lar ', ' ')
    entry = entry.replace('mus ', ' ')
    entry = entry.replace('mis ',  ' ')
    return entry

def remove_common_adjectives(entry):   
    temp = convert_turkish_letters(entry)
    temp = remove_special_characters(temp)
    temp = remove_stopwords(temp)
    splitted = temp.split()
    
    positive = [word for word in splitted if word in pos_adj]
    negative = [word for word in splitted if word in neg_adj]
    temp = re.sub("|".join(pos_adj), " ", temp)
    temp = re.sub("|".join(neg_adj), " ", temp)
    string_length=len(temp)+1    # will be adding 10 extra spaces
    temp=temp.ljust(string_length)
    temp = remove_suffix(temp)
    score = len(positive)-len(negative)
    if score < 0:
        score = 0
    elif score > 0:
        score = 1
    else:
        score = -1
    return temp,score