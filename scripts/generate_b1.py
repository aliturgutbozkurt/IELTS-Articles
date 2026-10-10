"""
Generator for Level B1 (Articles 1 - 250).
Covers 10 Categories x 25 Articles = 250 Articles.
"""

import os
import json

def generate_b1():
    categories = [
        {
            "id": 1,
            "name": "Modern Ofis ve İş Hayatına Giriş",
            "start": 1,
            "count": 25,
            "scenarios": [
                # 1
                ("Ofiste İlk Çalışma Alanı", "First Day at the Workstation",
                 "42 numaralı masa, botanik bahçesine bakan geniş bir cam kenarında yer alıyordu. Alex ergonomik koltuğu (chair) çekip oturduğunda içinde anında bir gurur hissetti. Tertemiz masanın (desk) üzerinde yeni bir gümüş dizüstü bilgisayar, yanında kablosuz bir klavye (keyboard) ve ergonomik bir fare (mouse) duruyordu. Sol tarafta, küçük metal bir raf (shelf), düzgün bir boş yazıcı kağıdı (paper) destesi ve yepyeni spiralli bir not defteri (notebook) barındırıyordu. Sarah monitörün yanına pürüzsüz mavi bir tükenmez kalem (pen) bıraktı: ‘Günün ilk görevi: sistemi başlatmak ve güvenli bir şifre (password) belirlemek.’ Alex açma düğmesine dokundu. Canlı 4K ekran (screen) hafif bir ışıltıyla canlandı. Harf ve simgeler içeren güçlü bir parola yazdıktan sonra şirket portalı tatlı bir sesle açıldı. Alex koltuğuna yaslandı. Gerekli tüm araçlar hazırdı; öğrenme ve katkı sağlama serüveni artık resmen başlamıştı."),
                # 2
                ("Sabah Karşılaması ve Güvenlik Protokolü", "Morning Arrival and Security Protocol",
                 "Alex sabah erkenden şirket merkezine vardı (arrive). Güler yüzlü güvenlik görevlisi (guard) onu ana girişte (entrance) karşıladı ve manyetik kimlik kartını (badge) teslim etti. Geniş resepsiyon (reception) salonunda mermer zeminler parlıyordu. Danışma personeli, binanın düzenini anlatan bir rehber (guide) kitapçık uzattı. Alex asansöre (elevator) yönelirken turnikelerden kartını okuttu (scan) ve aydınlık lobiye (lobby) adım attı."),
                # 3
                ("Ekip Tanışma Toplantısı", "Team Introduction Meeting",
                 "Saat tam onda tüm departman konferans salonunda toplandı (gather). Takım lideri haftalık toplantıyı (meeting) başlattı ve şirketin çeyrek hedefini (goal) detaylandırdı. Her çalışma arkadaşı (colleague) kendini samimiyetle tanıttı ve masadaki gündem (agenda) maddelerine odaklandı. Alex ekibin yapıcı tavrından cesaret (courage) aldı; herkes ortak bir işbirliği (cooperation) ile yeni görevi (assignment) başarıyla tamamlamaya söz verdi."),
                # 4
                ("Kurumsal E-posta İletişimi", "Corporate Email Communication",
                 "Alex ilk resmi şirket e-postasını (email) dikkatlice kaleme aldı. Gönderilmeden önce hazırlanan taslak (draft) metin, projenin konu başlığını (subject) ve ekli dosyayı (attachment) net biçimde açıklıyordu. Mesajı göndermek (send) üzereyken alıcı (recipient) listesini tekrar kontrol etti. Kibar (polite) bir selamlama ifadesi kullanarak departman yöneticisinden gelecek yanıtı (reply) beklemeye başladı."),
                # 5
                ("Kahve Molası ve Sosyalleşme", "Coffee Break and Socializing",
                 "Yoğun geçen sabah saatlerinin ardından Alex kısa bir mola (break) verdi. Modern kahve makinesi (coffee machine) taze çekirdek kokularıyla dolup taşan ofis mutfağında (kitchen) yer alıyordu. Yeni meslektaşlarıyla sohbet etti (chat) ve onların dostça (friendly) karşılamalarından memnun oldu. Sıcak bir fincan kahve eşliğinde rahatladı (relax), deneyimli kıdemlilerin verdiği tavsiyeleri (advice) dinleyerek resmi olmayan (casual) bir ortamda kaynaştı."),
                # 6
                ("Yazıcı Arızası ve Çözüm", "Printer Issue and Resolution",
                 "Departmandaki lazer yazıcı (printer) beklenmedik bir kağıt sıkışması (paper jam) uyarısı verdi. Görevli teknisyen (technician) hızla müdahale etti ve biten siyah toneri (toner) yeniledi. Alex önemli bir sözleşmenin kopyasını (copy) alması gerektiğini belirtti. Parçayı dikkatle değiştirmek (replace) sorunu kökünden giderdi ve Alex teknik ekibin problemi anında çözme (solve) hızına hayran kaldı."),
                # 7
                ("Dosyalama ve Arşiv Düzeni", "Filing and Archiving System",
                 "Ofisin düzenini sağlamak için tüm evraklar kalın bir klasör (folder) içine yerleştirildi. Tarihi belgeler güvenli şirket arşivinde (archive) saklanıyordu. Her resmi belge (document) çelik bir dolap (cabinet) rafına yerleştirildi. Dosyaları alfabetik sıraya göre düzenlemek (organize) gerekiyordu; Alex aranan her kaydın (record) doğru çekmecede (drawer) bulunabilmesi için titizlikle çalıştı."),
                # 8
                ("Haftalık Takvim Planlaması", "Weekly Calendar Planning",
                 "Pazartesi sabahı ilk iş dijital takvimi (calendar) gözden geçirmekti. Alex yöneticisiyle önemli bir randevu (appointment) ayarladı ve sisteme otomatik bir hatırlatıcı (reminder) ekledi. Kritik projenin son teslim tarihi (deadline) yaklaşıyordu; bu yüzden gereksiz işleri ertelemek (postpone) ve öncelikleri belirlemek (prioritize) şarttı. Toplantı saatini teyit etti (confirm) ve yoğun (busy) haftaya odaklandı."),
                # 9
                ("Müşteri Telefon Görüşmesi", "Customer Phone Call",
                 "Masanın üzerindeki kurumsal telefon (phone) çaldığında Alex profesyonel bir ses tonuyla yanıt verdi. Arayan sadık bir müşteriydi (client) ve yeni hizmet paketiyle ilgili bir soru (inquiry) yöneltti. Alex kısa bir not mesajı (message) aldıktan sonra çağrıyı ilgili uzmana aktarmak (transfer) istedi. Her soruya kibarca cevap verdi (answer) ve kullanıcının endişelerini hızla çözüme kavuşturdu (resolve)."),
                # 10
                ("Ofis Malzemeleri Siparişi", "Office Supplies Order",
                 "Tükenen kırtasiye malzemeleri (stationery) için idari işler sorumlusu yeni malzemeler (supplies) listesi hazırladı. Çevrim içi sistemden resmi bir sipariş vermek (order) gerekiyordu. Listede keskin bir makas (scissors), kutu kutu zımba telleri (staples) ve renkli zarflar bulunuyordu. Sipariş edilen ürünlerin hızlı teslimatı (delivery) sağlandı ve muhasebe departmanına ödeme faturası (invoice) iletildi."),
                # 11
                ("Beyin Fırtınası Oturumu", "Brainstorming Session",
                 "Yaratıcı ekip büyük beyaz tahta (whiteboard) önünde bir araya geldi. Herkes renkli bir tahta kalemi (marker) alarak yeni ürün kampanyası için parlak bir fikir (idea) öne sürdü. Yaratıcı (creative) öneriler tahtaya sıralandı; her öneri (suggestion) tarafsızca değerlendirildi. Ekip üyeleri en uygulanabilir çözümü seçmek (select) amacıyla alternatif stratejileri derinlemesine tartıştı (discuss)."),
                # 12
                ("Yeni Yazılım Eğitimi", "New Software Training",
                 "Şirket genelinde başlayan teknik eğitim (training), yeni kurumsal yazılımın (software) kullanımını kapsıyordu. İnteraktif öğretici kılavuz (tutorial) sayesinde her çalışan adım adım pratik yaptı. Başlangıç seviyesindeki bir acemi (beginner) bile sunulan güçlü dijital aracı (tool) kolayca kavrayabiliyordu. Alex pratik yaparak (practice) sistem becerisini (skill) geliştirdi ve kullanım yönergelerini (guideline) dikkatle izledi."),
                # 13
                ("Şirket Yemekhanesi", "Company Cafeteria",
                 "Öğle saati geldiğinde çalışanlar geniş şirket yemekhanesine (cafeteria) indi. Günün doyurucu öğle yemeği (lunch) için tepsi (tray) alıp sıraya giren Alex, zengin menüyü (menu) inceledi. Tatlı (dessert) yerine taze mevsim sebzesi (vegetable) ve ızgara tavuk seçerek sağlıklı (healthy) beslenmeyi tercih etti. Ferah masada tabağını seçti (choose) ve arkadaşlarıyla keyifle oturdu."),
                # 14
                ("Acil Durum Yangın Tatbikatı", "Emergency Fire Drill",
                 "Öğleden sonra aniden çalan yüksek sesli acil durum tatbikatı (drill) alarmı herkesi harekete geçirdi. Çalışanlar en yakın acil çıkış (exit) kapısına yöneldi ve asansör yerine yangın merdivenlerini (stairs) kullandı. Bina dışındaki belirlenmiş toplanma alanına (assembly) ulaşıldığında güvenlik (safety) amiri yoklama yaptı. Verilen güvenlik talimatlarını (instruction) harfiyen uygulayan ekip, süreci tamamen sakin (calm) kalarak yönetti."),
                # 15
                ("İlk Performans Geri Bildirimi", "First Performance Feedback",
                 "İlk ayın sonunda yönetici, Alex'e kapsamlı bir geri bildirim (feedback) oturumu sağladı. Gösterilen kayda değer ilerleme (progress) takdirle karşılandı. Yönetici, Alex'in güçlü yönlerini değerlendirdi (evaluate) ve analitik düşünme gücünü (strength) övdü. Sürekli kendini geliştirmek (improve) için yüksek motivasyon (motivation) aşıladı; kıymetli profesyonel tavsiyeler vererek Alex'i daha özgüvenli (confident) kıldı."),
                # 16
                ("İstemci Sunumu Hazırlığı", "Client Presentation Preparation",
                 "Önemli bir müşteri toplantısı öncesinde renkli slaytlar (slides) hazırlandı. Sunuma dikkat çekici grafikler (graphics) ve net bir taslak çerçeve (outline) eklendi. Hedef dinleyici kitlesinin (audience) beklentilerini karşılamak amacıyla Alex ekibiyle prova yaptı (practice). Madde imleri (bullet point) kullanarak karmaşık detayları basitleştirdi, ana mesajı netleştirdi (clarify) ve sunumunu tekrar tekrar prova etti (rehearse)."),
                # 17
                ("İş Seyahati Rezervasyonu", "Business Trip Booking",
                 "Gelecek ay düzenlenecek uluslararası fuar için erken uçuş (flight) bileti rezerve edildi. Şehir merkezindeki modern bir otelde konaklama (hotel) ayarlandı ve kesin rezervasyon (reservation) belgesi alındı. Yolculuk için hafif bir bagaj (baggage) hazırlayan temsilci, tüm yol masraflarını (expense) şirket kartıyla ödedi. Alınan ödeme makbuzu (receipt) seyahat programına (itinerary) eklenerek onaylandı."),
                # 18
                ("Şirket İçi Ağ Sorunları", "Internal Network Issues",
                 "Öğleden sonra ofisteki yerel bilgisayar ağı (network) yavaşladı ve bazı birimlerde internet bağlantısı (connection) koptu. Bilgi işlem sorumlusu ana yönlendiriciyi (router) kontrol etti ve yönetici şifresini (password) güncelledi. Kısa süreliğine sistemden kopmak (disconnect) çalışanları duraksattı; ancak sunucuyu yeniden başlatmak (reboot) güçlü sinyali (signal) geri getirdi ve ağ kararlı (stable) hale geldi."),
                # 19
                ("Proje Teslimi ve Kutlama", "Project Completion and Celebration",
                 "Haftalardır üzerinde çalışılan büyük projenin son teslim günü (deadline) başarıyla tamamlandı (complete). Ekiplerin elde ettiği muazzam başarı (success) ofiste coşkulu bir kutlama (celebration) ile taçlandırıldı. Masaya getirilen leziz pasta (cake) eşliğinde herkes tebriklerini iletti (congratulations). Harcanan olağanüstü çaba (effort) karşılığını bulmuştu; ekip üyeleri ortaya çıkan eserle gururlu (proud) hissediyordu."),
                # 20
                ("Hafta Sonu Fazla Mesaisi", "Weekend Overtime",
                 "Yaklaşan lansman öncesinde birkaç gönüllü çalışan hafta sonu fazla mesaisine (overtime) kaldı. Hafta içi kalabalığından uzak, son derece sessiz (quiet) bir ofis ortamı vardı. Alex derin bir odaklanma (focus) sağlayarak yarım kalan raporları toparladı. Kritik teslim tarihine (deadline) yetişmek için harcanan bu ekstra (extra) emek, adil bir ücret tazminatı (compensation) ile ödüllendirildi; ekip verimli (productive) bir çalışma sonunda işleri bitirdi (finish)."),
                # 21
                ("Yeni Çalışma Arkadaşına Mentorluk", "Mentoring a New Colleague",
                 "Deneyimli bir kıdemli uzman, ofise yeni başlayan gence rehber bir mentor (mentor) olarak atandı. Acemi yeni gelene (newcomer) ofisin temel işleyiş kuralları sabırla açıklandı (explain). Süreçler adım adım (step-by-step) gösterildi ve sonsuz bir sabır (patience) ile yaklaşıldı. Sorulan tüm meraklı sorular (questions) yanıtlandı; görevler bizzat uygulanarak gösterildi (demonstrate) ve sürekli kurumsal destek (support) sağlandı."),
                # 22
                ("Ofis Ergonomisi ve Sağlık", "Office Ergonomics and Health",
                 "Uzun süre masa başında çalışmanın getirdiği sırt ağrısını (back pain) önlemek için ergonomi (ergonomics) ilkeleri uygulandı. Doğru bir oturma duruşu (posture) geliştirmek amacıyla ayarlanabilir bir monitör kolu (monitor arm) monte edildi. Saat başı ayağa kalkıp kasları esnetmek (stretch) ve doğal gün ışığı alan bir aydınlatma (lighting) sağlamak yorgunluğu azalttı. Düzenli dinlenme molası (rest) vermek sağlıklı (healthy) kalmanın anahtarıydı."),
                # 23
                ("Çevre Dostu Ofis Girişimi", "Green Office Initiative",
                 "Şirket yönetimi sürdürülebilir bir gelecek için kağıtsız ofis (paperless) politikasını benimsedi. Çöpleri titizlikle geri dönüştürmek (recycle) ve plastik atıkları azaltmak (reduce) temel kural haline geldi. Enerji tasarrufu sağlamak için mesai bitiminde bilgisayarları kapatmak (switch off) zorunlu kılındı. Tek kullanımlık bardaklar yerine tekrar kullanılabilir (reusable) kupa (cup) dağıtıldı; tüm çalışanlar yeşil (green) bir çevre bilinci kazandı."),
                # 24
                ("Şirket Bülteni Hazırlığı", "Company Newsletter Preparation",
                 "Kurumsal iletişim ekibi aylık şirket bültenini (newsletter) hazırlamak için toplandı. Ayın en başarılı projesini anlatan etkileyici bir makale (article) yazıldı ve departman müdürüyle özel bir röportaj (interview) yapıldı. Sayfaya yüksek çözünürlüklü bir fotoğraf (photograph) yerleştirildi ve dikkat çeken çarpıcı bir manşet (headline) belirlendi. Bülteni dijital ortamda yayımlamak (publish) ve tüm personele dağıtmak (distribute) geniş bir okuyucu kitlesine (readership) ulaştı."),
                # 25
                ("Yıl Sonu Değerlendirme Raporu", "Annual Performance Review",
                 "Aralık ayının son haftasında şirketin yıllık (annual) faaliyet raporu hazırlandı. Yönetim kurulu için detaylı bir özet (summary) sunumu yapıldı ve yıl boyunca ulaşılan her büyük başarı (achievement) tek tek listelendi. Yeni yıl için iddialı bir büyüme hedefi (goal) belirlendi. Kapsamlı bir performans değerlendirmesi (review) sonucunda başarılı personelin maaşına (salary) zam yapıldı ve beklenen terfi (promotion) Alex'e derin bir içsel düşünme ve gurur (reflection) anı yaşattı.")
            ]
        }
    ]
    return categories
