"""
Complete Builder for Level B1 (Articles 1 - 250).
Generates 10 categories with 25 articles each.
Saves to data/articles_b1.json.
"""

import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.common import extract_vocab_from_text

def get_b1_categories():
    categories = [
        # Cat 1: Modern Ofis ve İş Hayatına Giriş (1 - 25)
        {
            "name": "Modern Ofis ve İş Hayatına Giriş",
            "items": [
                ("Ofiste İlk Çalışma Alanı", "First Day at the Workstation",
                 "42 numaralı masa, botanik bahçesine bakan geniş bir cam kenarında yer alıyordu. Alex ergonomik koltuğu (chair) çekip oturduğunda içinde anında bir gurur hissetti. Tertemiz masanın (desk) üzerinde yeni bir gümüş dizüstü bilgisayar, yanında kablosuz bir klavye (keyboard) ve ergonomik bir fare (mouse) duruyordu. Sol tarafta, küçük metal bir raf (shelf), düzgün bir boş yazıcı kağıdı (paper) destesi ve yepyeni spiralli bir not defteri (notebook) barındırıyordu. Sarah monitörün yanına pürüzsüz mavi bir tükenmez kalem (pen) bıraktı: ‘Günün ilk görevi: sistemi başlatmak ve güvenli bir şifre (password) belirlemek.’ Alex açma düğmesine dokundu. Canlı 4K ekran (screen) hafif bir ışıltıyla canlandı. Harf ve simgeler içeren güçlü bir parola yazdıktan sonra şirket portalı tatlı bir sesle açıldı. Alex koltuğuna yaslandı. Gerekli tüm araçlar hazırdı; öğrenme ve katkı sağlama serüveni artık resmen başlamıştı."),
                ("Sabah Karşılaması ve Güvenlik Protokolü", "Morning Arrival and Security Protocol",
                 "Alex sabah erkenden şirket merkezine vardı (arrive). Güler yüzlü güvenlik görevlisi (guard) onu ana girişte (entrance) karşıladı ve manyetik kimlik kartını (badge) teslim etti. Geniş resepsiyon (reception) salonunda mermer zeminler parlıyordu. Danışma personeli, binanın düzenini anlatan bir rehber (guide) kitapçık uzattı. Alex asansöre (elevator) yönelirken turnikelerden kartını okuttu (scan) ve aydınlık lobiye (lobby) adım attı."),
                ("Ekip Tanışma Toplantısı", "Team Introduction Meeting",
                 "Saat tam onda tüm departman konferans salonunda toplandı (gather). Takım lideri haftalık toplantıyı (meeting) başlattı ve şirketin çeyrek hedefini (goal) detaylandırdı. Her çalışma arkadaşı (colleague) kendini samimiyetle tanıttı ve masadaki gündem (agenda) maddelerine odaklandı. Alex ekibin yapıcı tavrından cesaret (courage) aldı; herkes ortak bir işbirliği (cooperation) ile yeni görevi (assignment) başarıyla tamamlamaya söz verdi."),
                ("Kurumsal E-posta İletişimi", "Corporate Email Communication",
                 "Alex ilk resmi şirket e-postasını (email) dikkatlice kaleme aldı. Gönderilmeden önce hazırlanan taslak (draft) metin, projenin konu başlığını (subject) ve ekli dosyayı (attachment) net biçimde açıklıyordu. Mesajı göndermek (send) üzereyken alıcı (recipient) listesini tekrar kontrol etti. Kibar (polite) bir selamlama ifadesi kullanarak departman yöneticisinden gelecek yanıtı (reply) beklemeye başladı."),
                ("Kahve Molası ve Sosyalleşme", "Coffee Break and Socializing",
                 "Yoğun geçen sabah saatlerinin ardından Alex kısa bir mola (break) verdi. Modern kahve makinesi (coffee machine) taze çekirdek kokularıyla dolup taşan ofis mutfağında (kitchen) yer alıyordu. Yeni meslektaşlarıyla sohbet etti (chat) ve onların dostça (friendly) karşılamalarından memnun oldu. Sıcak bir fincan kahve eşliğinde rahatladı (relax), deneyimli kıdemlilerin verdiği tavsiyeleri (advice) dinleyerek resmi olmayan (casual) bir ortamda kaynaştı."),
                ("Yazıcı Arızası ve Çözüm", "Printer Issue and Resolution",
                 "Departmandaki lazer yazıcı (printer) beklenmedik bir kağıt sıkışması (paper jam) uyarısı verdi. Görevli teknisyen (technician) hızla müdahale etti ve biten siyah toneri (toner) yeniledi. Alex önemli bir sözleşmenin kopyasını (copy) alması gerektiğini belirtti. Parçayı dikkatle değiştirmek (replace) sorunu kökünden giderdi ve Alex teknik ekibin problemi anında çözme (solve) hızına hayran kaldı."),
                ("Dosyalama ve Arşiv Düzeni", "Filing and Archiving System",
                 "Ofisin düzenini sağlamak için tüm evraklar kalın bir klasör (folder) içine yerleştirildi. Tarihi belgeler güvenli şirket arşivinde (archive) saklanıyordu. Her resmi belge (document) çelik bir dolap (cabinet) rafına yerleştirildi. Dosyaları alfabetik sıraya göre düzenlemek (organize) gerekiyordu; Alex aranan her kaydın (record) doğru çekmecede (drawer) bulunabilmesi için titizlikle çalıştı."),
                ("Haftalık Takvim Planlaması", "Weekly Calendar Planning",
                 "Pazartesi sabahı ilk iş dijital takvimi (calendar) gözden geçirmekti. Alex yöneticisiyle önemli bir randevu (appointment) ayarladı ve sisteme otomatik bir hatırlatıcı (reminder) ekledi. Kritik projenin son teslim tarihi (deadline) yaklaşıyordu; bu yüzden gereksiz işleri ertelemek (postpone) ve öncelikleri belirlemek (prioritize) şarttı. Toplantı saatini teyit etti (confirm) ve yoğun (busy) haftaya odaklandı."),
                ("Müşteri Telefon Görüşmesi", "Customer Phone Call",
                 "Masanın üzerindeki kurumsal telefon (phone) çaldığında Alex profesyonel bir ses tonuyla yanıt verdi. Arayan sadık bir müşteriydi (client) ve yeni hizmet paketiyle ilgili bir soru (inquiry) yöneltti. Alex kısa bir not mesajı (message) aldıktan sonra çağrıyı ilgili uzmana aktarmak (transfer) istedi. Her soruya kibarca cevap verdi (answer) ve kullanıcının endişelerini hızla çözüme kavuşturdu (resolve)."),
                ("Ofis Malzemeleri Siparişi", "Office Supplies Order",
                 "Tükenen kırtasiye malzemeleri (stationery) için idari işler sorumlusu yeni malzemeler (supplies) listesi hazırladı. Çevrim içi sistemden resmi bir sipariş vermek (order) gerekiyordu. Listede keskin bir makas (scissors), kutu kutu zımba telleri (staples) ve renkli zarflar bulunuyordu. Sipariş edilen ürünlerin hızlı teslimatı (delivery) sağlandı ve muhasebe departmanına ödeme faturası (invoice) iletildi."),
                ("Beyin Fırtınası Oturumu", "Brainstorming Session",
                 "Yaratıcı ekip büyük beyaz tahta (whiteboard) önünde bir araya geldi. Herkes renkli bir tahta kalemi (marker) alarak yeni ürün kampanyası için parlak bir fikir (idea) öne sürdü. Yaratıcı (creative) öneriler tahtaya sıralandı; her öneri (suggestion) tarafsızca değerlendirildi. Ekip üyeleri en uygulanabilir çözümü seçmek (select) amacıyla alternatif stratejileri derinlemesine tartıştı (discuss)."),
                ("Yeni Yazılım Eğitimi", "New Software Training",
                 "Şirket genelinde başlayan teknik eğitim (training), yeni kurumsal yazılımın (software) kullanımını kapsıyordu. İnteraktif öğretici kılavuz (tutorial) sayesinde her çalışan adım adım pratik yaptı. Başlangıç seviyesindeki bir acemi (beginner) bile sunulan güçlü dijital aracı (tool) kolayca kavrayabiliyordu. Alex pratik yaparak (practice) sistem becerisini (skill) geliştirdi ve kullanım yönergelerini (guideline) dikkatle izledi."),
                ("Şirket Yemekhanesi", "Company Cafeteria",
                 "Öğle saati geldiğinde çalışanlar geniş şirket yemekhanesine (cafeteria) indi. Günün doyurucu öğle yemeği (lunch) için tepsi (tray) alıp sıraya giren Alex, zengin menüyü (menu) inceledi. Tatlı (dessert) yerine taze mevsim sebzesi (vegetable) ve ızgara tavuk seçerek sağlıklı (healthy) beslenmeyi tercih etti. Ferah masada tabağını seçti (choose) ve arkadaşlarıyla keyifle oturdu."),
                ("Acil Durum Yangın Tatbikatı", "Emergency Fire Drill",
                 "Öğleden sonra aniden çalan yüksek sesli acil durum tatbikatı (drill) alarmı herkesi harekete geçirdi. Çalışanlar en yakın acil çıkış (exit) kapısına yöneldi ve asansör yerine yangın merdivenlerini (stairs) kullandı. Bina dışındaki belirlenmiş toplanma alanına (assembly) ulaşıldığında güvenlik (safety) amiri yoklama yaptı. Verilen güvenlik talimatlarını (instruction) harfiyen uygulayan ekip, süreci tamamen sakin (calm) kalarak yönetti."),
                ("İlk Performans Geri Bildirimi", "First Performance Feedback",
                 "İlk ayın sonunda yönetici, Alex'e kapsamlı bir geri bildirim (feedback) oturumu sağladı. Gösterilen kayda değer ilerleme (progress) takdirle karşılandı. Yönetici, Alex'in güçlü yönlerini değerlendirdi (evaluate) ve analitik düşünme gücünü (strength) övdü. Sürekli kendini geliştirmek (improve) için yüksek motivasyon (motivation) aşıladı; kıymetli profesyonel tavsiyeler vererek Alex'i daha özgüvenli (confident) kıldı."),
                ("İstemci Sunumu Hazırlığı", "Client Presentation Preparation",
                 "Önemli bir müşteri toplantısı öncesinde renkli slaytlar (slides) hazırlandı. Sunuma dikkat çekici grafikler (graphics) ve net bir taslak çerçeve (outline) eklendi. Hedef dinleyici kitlesinin (audience) beklentilerini karşılamak amacıyla Alex ekibiyle prova yaptı (practice). Madde imleri (bullet point) kullanarak karmaşık detayları basitleştirdi, ana mesajı netleştirdi (clarify) ve sunumunu tekrar tekrar prova etti (rehearse)."),
                ("İş Seyahati Rezervasyonu", "Business Trip Booking",
                 "Gelecek ay düzenlenecek uluslararası fuar için erken uçuş (flight) bileti rezerve edildi. Şehir merkezindeki modern bir otelde konaklama (hotel) ayarlandı ve kesin rezervasyon (reservation) belgesi alındı. Yolculuk için hafif bir bagaj (baggage) hazırlayan temsilci, tüm yol masraflarını (expense) şirket kartıyla ödedi. Alınan ödeme makbuzu (receipt) seyahat programına (itinerary) eklenerek onaylandı."),
                ("Şirket İçi Ağ Sorunları", "Internal Network Issues",
                 "Öğleden sonra ofisteki yerel bilgisayar ağı (network) yavaşladı ve bazı birimlerde internet bağlantısı (connection) koptu. Bilgi işlem sorumlusu ana yönlendiriciyi (router) kontrol etti ve yönetici şifresini (password) güncelledi. Kısa süreliğine sistemden kopmak (disconnect) çalışanları duraksattı; ancak sunucuyu yeniden başlatmak (reboot) güçlü sinyali (signal) geri getirdi ve ağ kararlı (stable) hale geldi."),
                ("Proje Teslimi ve Kutlama", "Project Completion and Celebration",
                 "Haftalardır üzerinde çalışılan büyük projenin son teslim günü (deadline) başarıyla tamamlandı (complete). Ekiplerin elde ettiği muazzam başarı (success) ofiste coşkulu bir kutlama (celebration) ile taçlandırıldı. Masaya getirilen leziz pasta (cake) eşliğinde herkes tebriklerini iletti (congratulations). Harcanan olağanüstü çaba (effort) karşılığını bulmuştu; ekip üyeleri ortaya çıkan eserle gururlu (proud) hissediyordu."),
                ("Hafta Sonu Fazla Mesaisi", "Weekend Overtime",
                 "Yaklaşan lansman öncesinde birkaç gönüllü çalışan hafta sonu fazla mesaisine (overtime) kaldı. Hafta içi kalabalığından uzak, son derece sessiz (quiet) bir ofis ortamı vardı. Alex derin bir odaklanma (focus) sağlayarak yarım kalan raporları toparladı. Kritik teslim tarihine (deadline) yetişmek için harcanan bu ekstra (extra) emek, adil bir ücret tazminatı (compensation) ile ödüllendirildi; ekip verimli (productive) bir çalışma sonunda işleri bitirdi (finish)."),
                ("Yeni Çalışma Arkadaşına Mentorluk", "Mentoring a New Colleague",
                 "Deneyimli bir kıdemli uzman, ofise yeni başlayan gence rehber bir mentor (mentor) olarak atandı. Acemi yeni gelene (newcomer) ofisin temel işleyiş kuralları sabırla açıklandı (explain). Süreçler adım adım (step-by-step) gösterildi ve sonsuz bir sabır (patience) ile yaklaşıldı. Sorulan tüm meraklı sorular (questions) yanıtlandı; görevler bizzat uygulanarak gösterildi (demonstrate) ve sürekli kurumsal destek (support) sağlandı."),
                ("Ofis Ergonomisi ve Sağlık", "Office Ergonomics and Health",
                 "Uzun süre masa başında çalışmanın getirdiği sırt ağrısını (back pain) önlemek için ergonomi (ergonomics) ilkeleri uygulandı. Doğru bir oturma duruşu (posture) geliştirmek amacıyla ayarlanabilir bir monitör kolu (monitor arm) monte edildi. Saat başı ayağa kalkıp kasları esnetmek (stretch) ve doğal gün ışığı alan bir aydınlatma (lighting) sağlamak yorgunluğu azalttı. Düzenli dinlenme molası (rest) vermek sağlıklı (healthy) kalmanın anahtarıydı."),
                ("Çevre Dostu Ofis Girişimi", "Green Office Initiative",
                 "Şirket yönetimi sürdürülebilir bir gelecek için kağıtsız ofis (paperless) politikasını benimsedi. Çöpleri titizlikle geri dönüştürmek (recycle) ve plastik atıkları azaltmak (reduce) temel kural haline geldi. Enerji tasarrufu sağlamak için mesai bitiminde bilgisayarları kapatmak (switch off) zorunlu kılındı. Tek kullanımlık bardaklar yerine tekrar kullanılabilir (reusable) kupa (cup) dağıtıldı; tüm çalışanlar yeşil (green) bir çevre bilinci kazandı."),
                ("Şirket Bülteni Hazırlığı", "Company Newsletter Preparation",
                 "Kurumsal iletişim ekibi aylık şirket bültenini (newsletter) hazırlamak için toplandı. Ayın en başarılı projesini anlatan etkileyici bir makale (article) yazıldı ve departman müdürüyle özel bir röportaj (interview) yapıldı. Sayfaya yüksek çözünürlüklü bir fotoğraf (photograph) yerleştirildi ve dikkat çeken çarpıcı bir manşet (headline) belirlendi. Bülteni dijital ortamda yayımlamak (publish) ve tüm personele dağıtmak (distribute) geniş bir okuyucu kitlesine (readership) ulaştı."),
                ("Yıl Sonu Değerlendirme Raporu", "Annual Performance Review",
                 "Aralık ayının son haftasında şirketin yıllık (annual) faaliyet raporu hazırlandı. Yönetim kurulu için detaylı bir özet (summary) sunumu yapıldı ve yıl boyunca ulaşılan her büyük başarı (achievement) tek tek listelendi. Yeni yıl için iddialı bir büyüme hedefi (goal) belirlendi. Kapsamlı bir performans değerlendirmesi (review) sonucunda başarılı personelin maaşına (salary) zam yapıldı ve beklenen terfi (promotion) Alex'e derin bir içsel düşünme ve gurur (reflection) anı yaşattı.")
            ]
        },

        # Cat 2: Üniversite Yaşamı ve Kampüs (26 - 50)
        {
            "name": "Üniversite Yaşamı ve Kampüs",
            "items": [
                ("Üniversite Kayıt Günü", "University Registration Day",
                 "Yeni akademik yılın ilk sabahı kampüs (campus) girişinde büyük bir kalabalık toplandı. Öğrenci işleri bürosunda resmi kayıt (registration) işlemleri başladı. Görevli memur, kimlik belgesini ve harç (tuition) dekontunu kontrol etti. Fakülte (faculty) sekreteri, yeni öğrencilere ders programını ve dönemlik ders kataloğunu (syllabus) dağıttı. Kampüs rehberi eşliğinde ana binayı gezen öğrenciler, geleceğe büyük bir umut ve heyecanla adım attı."),
                ("Büyük Amfide İlk Teori Dersi", "First Theory Lecture in the Main Hall",
                 "Yüzlerce öğrenci tarihi binadaki büyük amfi (lecture hall) sıralarına yerleşti. Kürsüye çıkan kıdemli profesör (professor), dönemin ilk teorik dersini (lecture) etkileyici bir hitabetle başlattı. Tahtaya temel kavramları yazarken öğrencilerin dikkatle dinlemesini ve not tutmasını istedi. Dersin genel çerçevesini ve sınav değerlendirme kriterlerini açıkladıktan sonra öğrencilerin sorularına tek tek kapsamlı yanıtlar verdi."),
                ("Merkezi Kütüphanede Kaynak Taraması", "Literature Search in the Central Library",
                 "Ders bitiminde öğrenciler sessizliğin hakim olduğu devasa merkezi kütüphaneye (library) yöneldi. Sayısız rafın (shelf) arasında yüz binlerce nadide kitap (book) ve süreli akademik dergi yer alıyordu. Kütüphaneci, dijital katalog tarama sisteminin nasıl kullanılacağını anlattı. Öğrenciler dönem projesi için güvenilir bilimsel kaynakları seçti ve sessiz çalışma salonlarında saatlerce araştırma yaptı."),
                ("Öğrenci Yurdunda İlk Akşam", "First Evening at the Student Dormitory",
                 "Farklı şehirlerden gelen gençler kampüs içindeki modern öğrenci yurduna (dormitory) yerleşti. Dört kişilik ferah odada her öğrenciye özel bir yatak, elbise dolabı ve çalışma masası tahsis edilmişti. Oda arkadaşları ilk akşam bir araya gelerek ortak yaşam kurallarını konuştu ve temizlik nöbeti takvimi hazırladı. Samimi sohbetler eşliğinde sıcak bir çay içildi ve kalıcı dostlukların ilk temeli atıldı."),
                ("Vize Haftası ve Çalışma Grupları", "Midterm Week and Study Groups",
                 "Dönemin ortasına gelindiğinde herkesi saran sınav (exam) stresi kampüs havasını değiştirdi. Zorlu vize sınavlarına hazırlanmak amacıyla küçük bir çalışma grubu (study group) kuruldu. Öğrenciler anlaşılması güç konuları birbirlerine anlatarak eksiklerini giderdi. Çözümlü eski sınav soruları incelendi, önemli formüller özetlendi ve birlikte çalışmanın getirdiği dayanışma sayesinde sınav kaygısı hafifletildi."),
                ("Laboratuvar Deneyi ve Güvenlik Kuralları", "Laboratory Experiment and Safety Guidelines",
                 "Fen fakültesindeki modern araştırma laboratuvarı (laboratory) hassas kimyasal deneyler için hazırlandı. Beyaz önlüklerini ve koruyucu gözlüklerini takan öğrenciler, asistanın verdiği güvenlik talimatlarını dikkatle dinledi. Planlanan kimyasal deney (experiment) titizlikle uygulandı; test tüpleri ve mikroskoplar yardımıyla hücresel değişimler gözlemlendi ve elde edilen tüm veriler laboratuvar defterine kaydedildi."),
                ("Başarı Bursu Mülakatı", "Merit Scholarship Interview",
                 "Yüksek not ortalamasına sahip adaylar için üniversite vakfının sunduğu başarı bursu (scholarship) mülakatları başladı. Mülakat odasına giren öğrenci, akademik hedeflerini ve toplumsal projelere yaptığı katkıları özgüvenle ifade etti. Değerlendirme jürisi, adayın vizyonunu ve öğrenme tutkusunu takdir ederek tam eğitim bursunu onayladı. Bu destek, öğrencinin araştırmalarına odaklanması için büyük bir maddi güvence oldu."),
                ("Kampüs Kafeteryasında Entelektüel Münazara", "Intellectual Debate at the Campus Cafe",
                 "Ders aralarında öğrenci kulüpleri kampüs kafeteryasında bir araya gelerek güncel konuları tartıştı. Felsefe kulübü üyeleri modern etik ve yapay zeka üzerine hararetli bir münazara (debate) düzenledi. Her konuşmacı kendi tezini mantıksal argümanlarla savundu ve karşıt görüşleri saygıyla dinledi. Farklı bakış açılarının serbestçe ifade edildiği bu ortam, üniversitenin çoğulcu kültürünü zenginleştirdi."),
                ("Dönem Sonu Araştırma Tezi Yazımı", "Writing the Term Research Thesis",
                 "Mezuniyet aşamasındaki son sınıf öğrencisi, aylar süren araştırmasını kapsamlı bir bitirme tezi (thesis) haline getirdi. Hipotezin belirlenmesinden anket verilerinin toplanmasına kadar her aşama akademik titizlikle yürütüldü. Kaynakça ve alıntılar uluslararası kurallara göre biçimlendirildi. Danışman hocanın onayından geçen metin, ciltlenerek enstitü sekreterliğine teslim edildi."),
                ("Öğrenci Kulüpleri Festivali", "Student Clubs Festival",
                 "Baharın gelişiyle birlikte üniversitenin geniş yeşil meydanında yıllık kulüp festivali coşkuyla başladı. Müzikten dağcılığa, robotikten tiyatroya kadar onlarca öğrenci kulübü renkli tanıtım stantları kurdu. Yeni üyeler ilgi duydukları topluluklara kayıt yaptırdı. Canlı müzik dinletileri, dans gösterileri ve eğlenceli yarışmalar eşliğinde tüm kampüs bayram yerine döndü."),
                ("Akademik Danışman ile Dönem Planlaması", "Semester Planning with the Academic Advisor",
                 "Her öğrenci dönem başında kendine atanan akademik danışman (advisor) ile birebir görüşme yaptı. Geçmiş dönemlerin transkripti incelenerek zorunlu ve seçmeli derslerin dağılımı planlandı. Danışman hoca, öğrencinin kariyer hedeflerine en uygun dersleri önerdi ve kredi yükünü dengeledi. Yapılan yapıcı yönlendirmeler sayesinde öğrenci dönem hedeflerini netleştirdi."),
                ("Uluslararası Değişim Programı Başvurusu", "International Exchange Program Application",
                 "Avrupa'daki prestijli bir üniversitede bir dönem eğitim görmek isteyen aday, öğrenci değişim programına (exchange program) başvurdu. Gerekli dil yeterlilik belgeleri, niyet mektubu ve onaylı transkript eksiksiz sisteme yüklendi. Yabancı dilde yapılan sözlü mülakatı başarıyla geçen öğrenci, farklı bir kültürü deneyimleme ve küresel bir bakış açısı kazanma fırsatını elde etti."),
                ("Final Sınavları Öncesi Kütüphane Sabahlaması", "All-Nighter at the Library Before Finals",
                 "Final haftasının zorlu temposunda üniversite kütüphanesi 24 saat boyunca kapılarını açık tuttu. Yüzlerce öğrenci gece boyunca kahve eşliğinde kalın ders kitaplarını (textbook) satır satır taradı. Sessiz koridorlarda sadece çevrilen sayfaların ve klavye seslerinin yankısı duyuluyordu. Güneşin ilk ışıkları pencerelerden süzülürken öğrenciler son tekrarlarını tamamlayıp sınav salonlarına doğru yola çıktı."),
                ("Mezuniyet Töreni ve Kep Atma Coşkusu", "Graduation Ceremony and Cap Toss",
                 "Yıllar süren yoğun emeğin ve uykusuz gecelerin ardından büyük mezuniyet töreni (graduation) günü geldi. Ailelerin ve akademisyenlerin alkışları arasında sahneye çıkan mezunlara diplomaları takdim edildi. Fakülte birincisi yaptığı duygu dolu konuşmada üniversitenin kendilerine kattığı vizyonu anlattı. Törenin sonunda yüzlerce kep gökyüzüne fırlatıldı ve büyük bir sevinç yaşandı."),
                ("Kariyer Fuarında İlk Şirket Görüşmeleri", "First Company Interviews at the Career Fair",
                 "Üniversitenin kapalı spor salonunda düzenlenen yıllık kariyer fuarına (career fair) uluslararası onlarca büyük şirket katıldı. Şık takım elbiselerini giyen son sınıf öğrencileri, ellerinde düzgünce basılmış özgeçmişleriyle şirket stantlarını ziyaret etti. İnsan kaynakları uzmanlarıyla doğrudan tanışma imkanı bulan gençler, geleceğe yönelik staj ve iş fırsatları hakkında değerli bilgiler aldı."),
                ("Bilimsel Makale İnceleme ve Eleştirel Okuma", "Scientific Article Review and Critical Reading",
                 "Yüksek lisans seminerinde öğrenciler hakemli bir bilimsel makale (article) üzerinde detaylı inceleme yaptı. Araştırmanın yöntemi, örneklem büyüklüğü ve elde edilen istatistiksel sonuçlar eleştirel bir gözle tartışıldı. Hipotezin geçerliliği ve literatüre sağladığı özgün katkı değerlendirildi. Bu çalışma, öğrencilerin analitik düşünme ve bilimsel araştırma değerlendirme becerilerini keskinleştirdi."),
                ("Öğrenci Temsilciliği Seçim Heyecanı", "Student Council Election Excitement",
                 "Kampüs genelinde öğrenci haklarını savunacak öğrenci konseyi (student council) seçimleri için hararetli bir kampanya dönemi yaşandı. Adaylar yemekhane fiyatlarının indirilmesi, kütüphane olanaklarının genişletilmesi ve kampüs içi ulaşımın ücretsiz olması gibi somut vaatlerle öğrencilerden oy istedi. Şeffaf sandıklarda yapılan oylama sonucunda yeni temsilciler belirlendi."),
                ("Üniversite Spor Tesisleri ve Şampiyona", "University Sports Facilities and Championship",
                 "Kampüsteki yarı olimpik yüzme havuzu, kapalı basketbol sahaları ve tenis kortları öğrencilerin sağlıklı yaşamına büyük katkı sağladı. Fakülteler arası voleybol şampiyonasında tribünler coşkulu tezahüratlarla inledi. Final maçını kazanan mühendislik takımı şampiyonluk kupasını havaya kaldırırken, sporun birleştirici gücü tüm kampüse neşe kattı."),
                ("Yaz Okulu ile Kredi Tamamlama", "Summer School for Credit Completion",
                 "Normal dönemde verilemeyen zor dersleri telafi etmek isteyenler için üniversite bünyesinde yoğunlaştırılmış yaz okulu (summer school) açıldı. Altı haftalık kısa sürede dersler hızlı bir tempoyla işlendi. Sınıfların daha küçük olması profesörle birebir iletişimi artırdı. Öğrenciler dönemi başarıyla tamamlayarak mezuniyet sürecindeki eksik kredilerini kapattı."),
                ("Tasarım Atölyesinde Maket Üretimi", "Scale Model Production in the Design Studio",
                 "Mimarlık fakültesi atölyesinde sabahlayan öğrenciler, jüri sunumu öncesinde üç boyutlu bina maketlerini tamamlamak için titizlikle çalıştı. Lazer kesim makineleri, ahşap plakalar ve özel yapıştırıcılar kullanılarak modern kentsel tasarımlar somutlaştırıldı. Projelerini jüri üyelerine savunan geleceğin mimarları, yenilikçi malzeme kullanımı ve estetik dengeleriyle tam not aldı."),
                ("Bitirme Tezi Sözlü Savunması", "Oral Defense of the Thesis",
                 "Büyük gün gelip çattığında öğrenci, beş profesörden oluşan tarafsız bir akademik jürinin karşısına çıktı. Yaptığı slayt sunumunda araştırmanın kuramsal temelini, bulgularını ve kısıtlılıklarını kırk dakika boyunca savundu. Jürinin yönelttiği zorlu metodolojik sorulara soğukkanlılıkla ve bilimsel kanıtlarla yanıt veren aday, oy birliğiyle tez savunmasını başarıyla tamamladı."),
                ("Ortak Öğrenci Evinde Yaşam Dinamikleri", "Dynamics of Living in a Shared Student Flat",
                 "Yurttan ayrılarak üç arkadaşıyla kampüs yakınında kiralık bir daireye çıkan öğrenciler, bağımsız yetişkin yaşamına ilk adımı attı. Kira, elektrik ve internet faturalarının eşit paylaşılması için bir bütçe panosu hazırlandı. Akşam yemeklerini sırayla pişiren ve mutfağı temiz tutmaya özen gösteren gençler, hem sorumluluk duygularını pekiştirdi hem de unutulmaz anılar biriktirdi."),
                ("Yabancı Dil Hazırlık Sınıfı Eğitimi", "Foreign Language Preparatory Class Education",
                 "Lisans programına başlamadan önce yoğun bir yabancı dil hazırlık eğitimine tabi tutulan öğrenciler, modern dil laboratuvarlarında eğitim gördü. Ana dili İngilizce olan eğitmenler eşliğinde konuşma, dinleme ve akademik yazma pratikleri yapıldı. Günlük dil sınavları ve sunum ödevleri sayesinde öğrenciler uluslararası akademik yayınları rahatlıkla takip edebilecek seviyeye ulaştı."),
                ("Mezunlar Derneği Yıllık Buluşması", "Alumni Association Annual Reunion",
                 "Üniversitenin yemyeşil bahçesinde düzenlenen geleneksel mezunlar günü, farklı kuşaklardan binlerce mezunu bir araya getirdi. Yıllar önce aynı sıralarda okumuş olan eski dostlar anılarını tazeledi; iş dünyasında önemli konumlara gelmiş deneyimli mezunlar ise yeni mezunlara mentorluk desteği vermeyi taahhüt etti."),
                ("Kampüs Radyosu ve Canlı Yayın", "Campus Radio and Live Broadcasting",
                 "İletişim fakültesi stüdyosunda faaliyet gösteren öğrenci radyosu, gün boyunca kampüs içi haberleri, müzik listelerini ve akademisyenlerle yapılan röportajları dinleyicilere ulaştırdı. Öğrenciler bizzat ses mikserini yönetti, canlı yayın programlarını sundu ve medya dünyasına adım atmadan önce paha biçilmez bir pratik deneyimi kazandı.")
            ]
        },

        # Cat 3: Şehir Yaşamı, Ulaşım ve Altyapı (51 - 75)
        {
            "name": "Şehir Yaşamı, Ulaşım ve Altyapı",
            "items": [
                ("Sabahın Erken Saatlerinde Metro Yolculuğu", "Early Morning Metro Commute",
                 "Şehrin batı yakasından merkeze gitmek isteyen binlerce yolcu (passenger) sabah saatlerinde yeraltı metro (subway) istasyonuna akın etti. Turnikelerden elektronik bilet (ticket) okutularak geniş perona (platform) inildi. Birkaç dakika arayla gelen modern trenler yolcuları hızla taşıyordu. Sabahın yoğun işe gidiş saatinde (rush hour) vagonlar tıklım tıklım dolsa da tren raylar üzerinde sarsıntısızca ilerleyerek trafiğe takılmadan merkeze ulaştı."),
                ("Otobüs Durağında Bekleyiş ve Dijital Hat Bilgisi", "Waiting at the Bus Stop and Digital Transit Info",
                 "Geniş caddedeki otobüs durağında (bus stop) bekleyen kent sakinleri, dijital ekrandan gelecek olan aracın tahmini varış süresini takip etti. Şehir içi toplu taşıma filosu temiz elektrikli araçlarla yenilenmişti. Yolcular düzenli bir sıra oluşturarak otobüse bindi, şoför güler yüzle selam verdi ve engelli yolcular için özel iniş rampası alçaltıldı."),
                ("Şehir İçi Bisiklet Yolları ve Çevre Dostu Ulaşım", "Urban Bicycle Lanes and Eco-Friendly Transit",
                 "Belediyenin inşa ettiği modern bisiklet yolu (bicycle lane) ağı, kent içi ulaşımda büyük bir rahatlama sağladı. Trafik sıkışıklığından (traffic jam) bunalan çalışanlar, kiralık akıllı bisikletlerle işlerine gitmeye başladı. Kaskını takan bisikletliler özel sinyalizasyon lambalarını takip ederek güvenle pedal çevirdi; hem karbon salımı azaldı hem de hareketli bir yaşam teşvik edildi."),
                ("Yaya Geçidi ve Trafik Güvenliği Standartları", "Pedestrian Crossing and Traffic Safety Standards",
                 "Yoğun ana arter üzerindeki yaya geçidi (pedestrian crossing) zemin boyaları ve parlak LED ışıklarıyla yenilendi. Karşıdan karşıya geçen yayalara (pedestrian) öncelik vermeyen sürücülere yönelik denetimler artırıldı. Okul önlerinde hız kesici kasisler yerleştirildi ve trafik polisleri öğrencilerin güvenli geçişini sağladı. Bu tedbirler sayesinde cadde üzerindeki kaza riski önemli ölçüde düştü."),
                ("Tarihi Asma Köprü ve Şehir Silueti", "Historic Suspension Bridge and City Skyline",
                 "İki yakayı birbirine bağlayan devasa asma köprü (bridge), kentin en görkemli mimari simgelerinden biridir. Altından geçen yük gemileri ve martı sesleri eşliğinde köprüden yürüyen yayalar, akşam güneşinin batışını hayranlıkla izledi. Işıklandırılan çelik halatlar gece kentin silüetine büyüleyici bir zarafet katıyordu."),
                ("Dağ Altından Geçen Modern Karayolu Tüneli", "Modern Highway Tunnel Under the Mountain",
                 "Şehrin iki büyük vadisini birleştiren çift tüplü karayolu tüneli (tunnel), sürücülerin yolculuk süresini kırk beş dakikadan yedi dakikaya indirdi. Tünel içindeki gelişmiş havalandırma fanları, acil durum kaçış kapıları ve yüksek çözünürlüklü güvenlik kameraları kesintisiz bir sürüş güvenliği sağladı. Modern altyapı sayesinde kışın buzlanan dağ yollarının tehlikesi tamamen ortadan kalktı."),
                ("Merkezi Tren Garı ve Şehirlerarası Seferler", "Central Railway Station and Intercity Routes",
                 "Tarihi merkezi tren garı (railway station), yüksek tavanlı görkemli mimarisiyle yolcuları karşıladı. Elektronik panolarda şehirlerarası hızlı tren sefer saatleri ve gecikme (delay) bilgileri anlık olarak güncelleniyordu. Yolcular kafeteryalarda kahvelerini yudumlarken, anons sesiyle birlikte perondaki modern trenlere yöneldi."),
                ("Uluslararası Havalimanı Terminali ve Bagaj İşlemleri", "International Airport Terminal and Baggage Handling",
                 "Günde yüz binden fazla yolcuya hizmet veren devasa havalimanı terminali (terminal), son teknoloji otomasyon sistemleriyle donatılmıştı. Yolcular self-servis kiosklarında biniş kartlarını bastı ve bagajlarını otomatik teslim noktalarına bıraktı. Pasaport kontrol noktalarındaki hızlı geçiş kapıları sayesinde kuyruklar dakikalar içinde eridi."),
                ("Akıllı Şehir Taksi Durağı ve Mobil Çağrı", "Smart City Taxi Stand and Mobile Hailing",
                 "Şehrin ana meydanında yer alan taksi durağı, mobil uygulama entegrasyonuyla modernize edildi. Cep telefonundan tek bir dokunuşla çağrılan elektrikli taksi, konum bilgisini takip ederek dakikalar içinde kapıya ulaştı. Şeffaf tarife ve dijital ödeme imkanı sayesinde yolcular nakit para aramadan konforlu bir yolculuk yaptı."),
                ("Geniş Şehir Meydanı ve Kamusal Yaşam", "Expansive City Square and Public Life",
                 "Kentin kalbinde yer alan geniş şehir meydanı (city square), tarihi heykeller, fıskiyeli havuzlar ve gölgeli banklarla çevrilidir. Hafta sonları yerel müzisyenlerin konser verdiği meydan, her yaştan insanın nefes aldığı, buluştuğu ve sosyalleştiği canlı bir kamusal alana dönüşür."),
                ("Sakin Bir Şehir Parkında Pazar Yürüyüşü", "Sunday Walk in a Peaceful City Park",
                 "Gökdelenlerin ve yoğun caddelerin hemen ardında uzanan yemyeşil şehir parkı, kentin akciğeri görevini görür. Asırlık ağaçların gölgesinde uzanan yürüyüş parkurlarında koşan sporcular, çocuk oyun alanlarında neşeyle oynayan minikler ve gölet kenarında kitap okuyanlar doğanın huzurunu yaşar."),
                ("Tarihi Şehir Anıtı ve Kültürel Miras", "Historic City Monument and Cultural Heritage",
                 "Eski kentin merkezinde yükselen taş anıt (monument), geçmiş yüzyılların kahramanlıklarını ve tarihi zaferlerini simgeler. Dünyanın dört bir yanından gelen turistler rehberlerin anlattığı tarihi hikayeleri dinleyerek anıtın önünde hatıra fotoğrafları çektirir."),
                ("Gece Yarısı Yol Bakım ve Onarım Çalışması", "Midnight Road Maintenance and Repair Work",
                 "Trafiğin en aza indiği gece saatlerinde belediye ekipleri ana bulvar üzerinde kapsamlı bir yol onarım (road repair) çalışması başlattı. Eski asfalt kazındı, yeni sıcak asfalt serildi ve yol çizgileri fosforlu boyalarla yeniden çizildi. Sabahın ilk ışıklarına kadar tamamlanan çalışma sayesinde sürücüler pürüzsüz bir yolda güvenle seyahat etti."),
                ("Akıllı Navigasyon ve Alternatif Güzergahlar", "Smart Navigation and Alternative Routes",
                 "İşe gitmek için direksiyon başına geçen sürücü, akıllı navigasyon (navigation) sistemini açtı. Uygulama, ana köprüdeki kaza nedeniyle oluşan yoğunluğu tespit ederek sürücüyü daha sakin bir yan yola ve alternatif güzergaha yönlendirdi. Böylece yarım saatlik zaman kaybı önlendi."),
                ("Geniş Yaya Yolu ve Alışveriş Caddesi", "Wide Pedestrianized Street and Shopping Avenue",
                 "Araç trafiğine tamamen kapatılan geniş alışveriş caddesi, gün boyu yerli ve yabancı ziyaretçilerle dolup taştı. Yol boyunca sıralanan şık kafeler, tarihi vitrinler ve sokak lezzetleri caddenin canlı atmosferini besledi. İnsanlar vitrinleri rahatça inceleyerek güvenli bir şekilde alışveriş yaptı."),
                ("Otomatik Bilet Satış Makineleri", "Automated Ticket Vending Machines",
                 "İstasyon girişlerindeki dokunmatik bilet satış otomatları, yolculara saniyeler içinde seyahat kartı yükleme imkanı sundu. Farklı dilleri destekleyen çok dilli arayüz sayesinde yabancı turistler bile zorlanmadan şehir içi ulaşım biletlerini temin etti."),
                ("Engelsiz Ulaşım ve Altyapı Düzenlemeleri", "Accessible Transit and Infrastructure Regulations",
                 "Şehir genelinde kaldırımlar görme engelliler için kabartmalı sarı kılavuz çizgilerle donatıldı. Tüm otobüs duraklarına sesli anons sistemleri yerleştirildi ve metro girişlerindeki engelli asansörleri düzenli bakıma alındı. Bu altyapı adımları, engelli vatandaşların kentsel yaşama eşit ve bağımsız katılımını sağladı."),
                ("Deniz Ulaşımı ve Şehir İçi Vapurlar", "Maritime Transport and Urban Passenger Ferries",
                 "Sahil kentinde deniz yoluyla yapılan vapur yolculuğu, hem en huzurlu hem de en ekonomik ulaşım alternatifidir. Güvertede esen serin deniz rüzgarı eşliğinde simit yiyip martıları besleyen yolcular, kara trafiğinin stresinden uzaklaşarak karşı kıyıya keyifle ulaştı."),
                ("Kentsel Dönüşüm ve Güvenli Konutlar", "Urban Regeneration and Safe Housing",
                 "Deprem riskine karşı başlatılan kentsel dönüşüm projesiyle eski ve dayanıksız binalar kontrollü şekilde yıkıldı. Yerlerine çevre dostu, enerji tasarruflu ve depreme dayanıklı modern konut kompleksleri inşa edildi. Geniş otoparkları ve çocuk parklarıyla yenilenen mahalleler modern bir görünüme kavuştu."),
                ("Akıllı Sokak Aydınlatması ve Enerji Tasarrufu", "Smart Street Lighting and Energy Conservation",
                 "Şehrin sokak lambaları hareket sensörlü ve güneş panelli akıllı LED sistemlerle değiştirildi. Gece yarısından sonra sokakta kimse yokken ışık seviyesini düşüren sistem, bir yaya veya araç yaklaştığında aydınlatmayı otomatik olarak artırdı. Bu uygulama ile belediye bütçesinde milyonlarca liralık enerji tasarrufu sağlandı."),
                ("Katlı Otoparklar ve Park Sorunu Çözümü", "Multi-Storey Car Parks and Parking Solutions",
                 "Şehir merkezindeki otopark sıkıntısını gidermek amacıyla tam otomatik katlı otoparklar hizmete açıldı. Sürücüler araçlarını giriş platformuna bıraktıktan sonra robotik sistemler aracı güvenli boş alana taşıdı. Bu teknoloji sayesinde sokak aralarındaki düzensiz parklar engellendi ve caddeler rahat nefes aldı."),
                ("Hızlı Şarj İstasyonları ve Elektrikli Araçlar", "Fast Charging Stations and Electric Vehicles",
                 "Elektrikli otomobil kullanımının hızla yaygınlaşmasıyla birlikte kentin ana arterlerine ve benzin istasyonlarına yüksek hızlı şarj üniteleri kuruldu. Araç bataryasını yirmi dakikada yüzde seksen doluluğa ulaştıran istasyonlar, temiz enerjili taşımacılığın benimsenmesini hızlandırdı."),
                ("Şehir İçi Hız Kontrolü ve Radar Denetimi", "Urban Speed Control and Speed Radar Enforcement",
                 "Trafik kazalarını önlemek amacıyla ana caddelere elektronik hız denetim sistemleri ve otomatik radarlar yerleştirildi. Belirlenen hız sınırını aşan sürücülere anında ceza bildirimi iletildi. Caydırıcı cezalar ve sıkı denetimler sayesinde sürücüler hız kurallarına uymaya başladı."),
                ("Kanalizasyon ve Yağmur Suyu Altyapısı", "Sewage and Stormwater Infrastructure",
                 "Aşırı yağışlarda meydana gelen su baskınlarını engellemek için yer altına devasa yağmur suyu tahliye kanalları inşa edildi. Kanalizasyon hatları modern borularla yenilenerek şehir atıkları arıtma tesislerine yönlendirildi. Bu güçlü altyapı yatırımı, kentin afetlere karşı direncini artırdı."),
                ("Haftalık Semt Pazarı ve Mahalle Kültürü", "Weekly Local Market and Neighborhood Culture",
                 "Her perşembe günü kurulan geleneksel semt pazarı, taze meyve ve sebzelerin rengarenk tezgahlarıyla mahalleyi şenlendirdi. Yerel üreticiler doğal ürünlerini doğrudan tüketiciye sundu. Komşuların pazar arabalarıyla karşılaşıp sohbet ettiği bu gelenek, modern kent yaşamında sıcak bir mahalle dayanışmasını yaşatmaya devam etti.")
            ]
        }
    ]

    # Dynamically generate remaining categories (Cat 4 to 10) with 25 distinct scenarios each
    b1_extra_categories = [
        # Cat 4: Sağlık, Spor ve Beslenme (76 - 100)
        ("Sağlık, Spor ve Beslenme", [
            ("Doktor Muayenesi ve Teşhis", "Doctor Consultation and Diagnosis", "hastane (hospital)", "doktor (doctor)", "belirti (symptom)", "muayene (examination)", "reçete (prescription)", "ilaç (medicine)"),
            ("Eczaneden İlaç Temini", "Obtaining Medicine from the Pharmacy", "eczane (pharmacy)", "eczacı (pharmacist)", "doz (dose)", "hap (pill)", "ağrı kesici (painkiller)", "şurup (syrup)"),
            ("Dengeli Beslenme ve Öğün Düzeni", "Balanced Nutrition and Meal Routine", "diyet (diet)", "öğün (meal)", "protein (protein)", "karbonhidrat (carbohydrate)", "lif (fiber)", "taze (fresh)"),
            ("Vitamin Takviyesi ve Mineral Desteği", "Vitamin Supplements and Mineral Support", "vitamin (vitamin)", "mineral (mineral)", "bağışıklık (immunity)", "kan testi (blood test)", "kalsiyum (calcium)", "demir (iron)"),
            ("Sabah Koşusu ve Kardiyo Egzersizi", "Morning Run and Cardio Exercise", "koşu (jogging)", "egzersiz (exercise)", "kalp atışı (heart rate)", "nefes (breath)", "enerji (energy)", "kondisyon (stamina)"),
            ("Fitness Salonunda Ağırlık Antrenmanı", "Weight Training at the Fitness Gym", "antrenman (workout)", "ağırlık (weight)", "kas (muscle)", "antrenör (trainer)", "güç (strength)", "esneme (stretching)"),
            ("Yeterli Su Tüketimi ve Hidrasyon", "Adequate Water Intake and Hydration", "su tüketimi (hydration)", "sıvı (fluid)", "böbrek (kidney)", "hücre (cell)", "toksin (toxin)", "canlılık (vitality)"),
            ("Kaliteli Uyku ve Biyolojik Saat", "Quality Sleep and Biological Clock", "uyku (sleep)", "yastık (pillow)", "dinlenme (rest)", "rüya (dream)", "melatonin (melatonin)", "yorgunluk (fatigue)"),
            ("Stres Yönetimi ve Rahatlama Teknikleri", "Stress Management and Relaxation Techniques", "stres (stress)", "kaygı (anxiety)", "meditasyon (meditation)", "sakinlik (calmness)", "terapi (therapy)", "denge (balance)"),
            ("Ruh Sağlığı ve Psikolojik Dayanıklılık", "Mental Health and Psychological Resilience", "ruh sağlığı (mental health)", "psikolog (psychologist)", "motivasyon (motivation)", "duygu (emotion)", "huzur (peace)", "özsaygı (self-esteem)"),
            ("Diş Hekimi Kontrolü ve Ağız Hijyeni", "Dental Checkup and Oral Hygiene", "diş hekimi (dentist)", "diş fırçası (toothbrush)", "macun (toothpaste)", "çürük (cavity)", "temizleme (cleaning)", "diş eti (gum)"),
            ("Kalp ve Damar Sağlığı Taraması", "Cardiovascular Health Screening", "tansiyon (blood pressure)", "damar (artery)", "kolesterol (cholesterol)", "nabız (pulse)", "dolaşım (circulation)", "önlem (prevention)"),
            ("Spor Sonrası Kas Toparlanması", "Post-Workout Muscle Recovery", "toparlanma (recovery)", "masaj (massage)", "protein tozu (protein powder)", "buz tedavisi (ice therapy)", "dinlenme (rest)", "esneklik (flexibility)"),
            ("Mevsimsel Alerjiler ve Korunma", "Seasonal Allergies and Prevention", "alerji (allergy)", "polen (pollen)", "hapşırma (sneezing)", "kaşıntı (itching)", "bağışıklık (immune)", "antihistaminik (antihistamine)"),
            ("Doğru Oturma Duruşu ve Omurga Sağlığı", "Proper Sitting Posture and Spinal Health", "duruş (posture)", "omurga (spine)", "sırt (back)", "bel ağrısı (lower back pain)", "ergonomi (ergonomics)", "fizik tedavi (physical therapy)"),
            ("İlk Yardım Bilgisi ve Acil Müdahale", "First Aid Knowledge and Emergency Response", "ilk yardım (first aid)", "pansuman (dressing)", "bandaj (bandage)", "yara (wound)", "yanık (burn)", "ambulans (ambulance)"),
            ("Organik Gıdalar ve Doğal Beslenme", "Organic Foods and Natural Nutrition", "organik (organic)", "doğal (natural)", "pestisit (pesticide)", "katkısız (additive-free)", "pazar (market)", "lezzet (taste)"),
            ("Göz Muayenesi ve Görme Netliği", "Eye Examination and Visual Clarity", "göz doktoru (ophthalmologist)", "gözlük (glasses)", "lens (contact lens)", "görme (vision)", "bulanıklık (blurriness)", "odak (focus)"),
            ("Açık Havada Yürüyüş ve Zindelik", "Outdoor Walking and Vitality", "yürüyüş (hiking)", "patika (trail)", "temiz hava (fresh air)", "doğa (nature)", "adım (step)", "zindelik (wellness)"),
            ("Sağlıklı Kilo Kontrolü ve Metabolizma", "Healthy Weight Management and Metabolism", "kilo (weight)", "metabolizma (metabolism)", "kalori (calorie)", "hedef (target)", "ölçüm (measurement)", "disiplin (discipline)"),
            ("Masa Başı Çalışanlar İçin Egzersizler", "Exercises for Desk Workers", "ofis (office)", "hareketsizlik (inactivity)", "esneme (stretch)", "eklem (joint)", "mola (break)", "canlılık (alertness)"),
            ("Bağışıklık Sistemini Güçlendiren Çaylar", "Teas That Strengthen the Immune System", "bitki çayı (herbal tea)", "zencefil (ginger)", "bal (honey)", "limon (lemon)", "antioksidan (antioxidant)", "şifa (healing)"),
            ("Sağlık Ocağında Yıllık Genel Kontrol", "Annual General Checkup at the Health Clinic", "sağlık ocağı (clinic)", "tahlil (analysis)", "hekim (physician)", "rapor (report)", "tarama (screening)", "sağlık (health)"),
            ("Güneş Işığı ve D Vitamini Sentezi", "Sunlight and Vitamin D Synthesis", "güneş ışığı (sunlight)", "kemik (bone)", "güneş kremi (sunscreen)", "emilim (absorption)", "canlılık (vitality)", "açık hava (outdoors)"),
            ("Bilinçli Tüketici ve Besin Etiketleri", "Conscious Consumer and Food Labels", "etiket (label)", "içindekiler (ingredients)", "şeker (sugar)", "tuz (sodium)", "katkı maddesi (preservative)", "bilinç (awareness)")
        ]),

        # Cat 5: Çevre, Doğa ve Geri Dönüşüm (101 - 125)
        ("Çevre, Doğa ve Geri Dönüşüm", [
            ("Evde Çöp Ayrıştırma ve Geri Dönüşüm", "Household Waste Sorting and Recycling", "geri dönüşüm (recycling)", "atık (waste)", "plastik (plastic)", "cam (glass)", "kağıt (paper)", "kutu (bin)"),
            ("Plastik Tüketimini Azaltma Hareketi", "Movement to Reduce Plastic Consumption", "tek kullanımlık (disposable)", "bez çanta (tote bag)", "matara (flask)", "kirlilik (pollution)", "tüketim (consumption)", "çevre (environment)"),
            ("Güneş Enerjisi Panelleri ve Temiz Elektrik", "Solar Panels and Clean Electricity", "güneş paneli (solar panel)", "yenilenebilir (renewable)", "elektrik (electricity)", "çatı (roof)", "tasarruf (savings)", "temiz (clean)"),
            ("Rüzgar Türbinleri ve Doğal Güç", "Wind Turbines and Natural Power", "rüzgar türbini (wind turbine)", "kanat (blade)", "rüzgar (wind)", "enerji santrali (power plant)", "sürdürülebilir (sustainable)", "jeneratör (generator)"),
            ("Orman Koruma ve Ağaçlandırma Seferberliği", "Forest Protection and Afforestation Campaign", "orman (forest)", "fidan (sapling)", "dikim (planting)", "ağaç (tree)", "yeşil alan (green space)", "oksijen (oxygen)"),
            ("Tatlı Su Kaynaklarının Korunması", "Conservation of Freshwater Resources", "su kaynağı (water source)", "tatlı su (freshwater)", "baraj (dam)", "tasarruf (conservation)", "kuraklık (drought)", "israf (waste)"),
            ("İklim Değişikliği ve Küresel Isınma", "Climate Change and Global Warming", "iklim değişikliği (climate change)", "küresel ısınma (global warming)", "sıcaklık (temperature)", "buzul (glacier)", "atmosfer (atmosphere)", "etki (impact)"),
            ("Organik Kompost ve Toprak Verimliliği", "Organic Compost and Soil Fertility", "kompost (compost)", "gübre (fertilizer)", "toprak (soil)", "organik atık (organic waste)", "verimlilik (fertility)", "bahçe (garden)"),
            ("Nesli Tehlikedeki Hayvanları Koruma", "Protecting Endangered Animals", "nesli tükenmekte (endangered)", "vahşi yaşam (wildlife)", "koruma alanı (sanctuary)", "biyoçeşitlilik (biodiversity)", "avlanma (poaching)", "tür (species)"),
            ("Okyanuslardaki Plastik Adaları Temizleme", "Cleaning Ocean Plastic Patches", "okyanus (ocean)", "deniz (sea)", "mikroplastik (microplastic)", "mercan (coral)", "balık (fish)", "temizlik (cleanup)"),
            ("Hava Kalitesi Ölçümü ve Temiz Gökyüzü", "Air Quality Measurement and Clean Skies", "hava kalitesi (air quality)", "duman (smoke)", "emisyon (emission)", "filtre (filter)", "zehirli gaz (toxic gas)", "solunum (respiratory)"),
            ("Milli Parklar ve Doğal Yaşam Alanları", "National Parks and Natural Habitats", "milli park (national park)", "habitat (habitat)", "koruma (conservation)", "flora (flora)", "fauna (fauna)", "gözlem (observation)"),
            ("Yağmur Suyu Hasadı ve Bahçe Sulama", "Rainwater Harvesting and Garden Irrigation", "yağmur suyu (rainwater)", "depolama (storage)", "sulama (irrigation)", "sarnıç (cistern)", "tasarruf (efficiency)", "bitki (plant)"),
            ("Karbon Ayak İzi ve Kişisel Sorumluluk", "Carbon Footprint and Personal Responsibility", "karbon ayak izi (carbon footprint)", "hesaplama (calculation)", "toplu taşıma (transit)", "azaltım (reduction)", "yaşam tarzı (lifestyle)", "sorumluluk (responsibility)"),
            ("Doğa Dostu Temizlik Maddeleri", "Eco-Friendly Cleaning Products", "sirke (vinegar)", "karbonat (baking soda)", "kimyasal (chemical)", "çevre dostu (eco-friendly)", "biyolojik (biodegradable)", "hijyen (hygiene)"),
            ("Kuş Gözlemciliği ve Doğal Denge", "Birdwatching and Natural Balance", "kuş (bird)", "dürbün (binoculars)", "göç (migration)", "sulak alan (wetland)", "doğal denge (ecological balance)", "rehber (guide)"),
            ("Deniz Kıyısı Çöp Toplama Etkinliği", "Beach Cleanup Activity", "sahil (beach)", "kıyı (coastline)", "gönüllü (volunteer)", "çöp torbası (trash bag)", "farkındalık (awareness)", "dayanışma (solidarity)"),
            ("E-Atıkların Geri Kazanımı", "E-Waste Recovery and Recycling", "elektronik atık (e-waste)", "eski telefon (old phone)", "batarya (battery)", "geri kazanım (recovery)", "ağır metal (heavy metal)", "toplama merkezi (drop-off center)"),
            ("Sürdürülebilir Tarım ve Yerel Üretim", "Sustainable Agriculture and Local Farming", "tarım (agriculture)", "çiftçi (farmer)", "hasat (harvest)", "mevsimsel (seasonal)", "yerel ürün (local produce)", "doğal (natural)"),
            ("Şehir İçi Yeşil Çatılar ve Dikey Bahçeler", "Urban Green Roofs and Vertical Gardens", "yeşil çatı (green roof)", "dikey bahçe (vertical garden)", "yalıtım (insulation)", "soğutma (cooling)", "şehir (city)", "bitki örtüsü (vegetation)"),
            ("Yeniden Kullanılabilir Ürünlerin Gücü", "Power of Reusable Products", "tekrar kullanılabilir (reusable)", "kahve bardağı (tumbler)", "cam kavanoz (glass jar)", "alışkanlık (habit)", "çöp (garbage)", "kültür (culture)"),
            ("Nehir Kirliliği ve Su Arıtma", "River Pollution and Water Purification", "nehir (river)", "akarsu (stream)", "arıtma tesisi (treatment plant)", "kanal (canal)", "duruluk (clarity)", "yaşam (life)"),
            ("Enerji Tasarruflu Ev Aletleri", "Energy-Efficient Home Appliances", "enerji sınıfı (energy rating)", "tasarruf (conservation)", "buzdolabı (refrigerator)", "çamaşır makinesi (washing machine)", "fatura (bill)", "verimlilik (efficiency)"),
            ("Ekolojik Ayak İzi ve Gezegenin Limitleri", "Ecological Footprint and Planetary Limits", "ekolojik (ecological)", "kaynak (resource)", "tükenme (depletion)", "dünya (earth)", "gelecek nesiller (future generations)", "koruma (protection)"),
            ("Çevre Eğitiminin Çocuklara Aşılanması", "Instilling Environmental Education in Children", "çevre eğitimi (environmental education)", "okul (school)", "çocuk (child)", "farkındalık (awareness)", "ağaç sevgisi (love of trees)", "doğa yürüyüşü (nature walk)")
        ]),

        # Cat 6: Temel Teknoloji, Dijital Araçlar ve İnternet (126 - 150)
        ("Temel Teknoloji, Dijital Araçlar ve İnternet", [
            ("Akıllı Telefonun Günlük Hayattaki Yeri", "Smartphones in Everyday Life", "akıllı telefon (smartphone)", "dokunmatik ekran (touchscreen)", "uygulama (app)", "mesajlaşma (messaging)", "bağlantı (connectivity)", "kamera (camera)"),
            ("Kablosuz İnternet ve Wi-Fi Erişimi", "Wireless Internet and Wi-Fi Access", "kablosuz (wireless)", "bağlantı (connection)", "şifre (password)", "yönlendirici (router)", "hız (speed)", "internet (internet)"),
            ("Bulut Depolama ve Dosya Güvenliği", "Cloud Storage and File Security", "bulut depolama (cloud storage)", "sunucu (server)", "yedekleme (backup)", "erişim (access)", "senkronizasyon (sync)", "güvenlik (security)"),
            ("Sosyal Medya ve Dijital İletişim", "Social Media and Digital Communication", "sosyal medya (social media)", "profil (profile)", "beğeni (like)", "takipçi (follower)", "paylaşım (post)", "etkileşim (engagement)"),
            ("Güçlü Parolalar ve Siber Güvenlik", "Strong Passwords and Cyber Security", "parola (password)", "siber güvenlik (cybersecurity)", "şifreleme (encryption)", "bilgisayar korsanı (hacker)", "güvenlik (safety)", "hesap (account)"),
            ("Dizüstü Bilgisayar ve Taşınabilir Güç", "Laptops and Portable Computing", "dizüstü bilgisayar (laptop)", "batarya (battery)", "şarj cihazı (charger)", "hafif (lightweight)", "taşınabilir (portable)", "performans (performance)"),
            ("Arama Motorları ve Bilgiye Hızlı Erişim", "Search Engines and Fast Access to Information", "arama motoru (search engine)", "anahtar kelime (keyword)", "sonuç (result)", "tarayıcı (browser)", "web sitesi (website)", "arama (search)"),
            ("Çevrim İçi Bankacılık ve Güvenli Ödemeler", "Online Banking and Secure Payments", "çevrim içi bankacılık (online banking)", "transfer (transfer)", "fatura ödeme (bill payment)", "güvenlik kodu (security code)", "bakiye (balance)", "mobil (mobile)"),
            ("Görüntülü Arama ve Uzaktan Toplantılar", "Video Calls and Remote Meetings", "görüntülü görüşme (video call)", "kamera (webcam)", "mikrofon (microphone)", "kulaklık (headphones)", "bağlantı (link)", "toplantı (conference)"),
            ("E-Kitap Okuyucuları ve Dijital Kütüphane", "E-Book Readers and Digital Libraries", "e-kitap (e-book)", "dijital (digital)", "ekran (screen)", "indirme (download)", "yazı tipi (font)", "okuma (reading)"),
            ("Yapay Zeka Asistanları ve Sesli Komutlar", "Artificial Intelligence Assistants and Voice Commands", "yapay zeka (artificial intelligence)", "sesli komut (voice command)", "akıllı asistan (smart assistant)", "cevap (answer)", "otomasyon (automation)", "algoritma (algorithm)"),
            ("Akıllı Saatler ve Sağlık Takibi", "Smartwatches and Health Tracking", "akıllı saat (smartwatch)", "nabız ölçer (heart rate monitor)", "adım sayar (pedometer)", "bildirim (notification)", "bileklik (wristband)", "sağlık (fitness)"),
            ("Harici Sabit Disk ve Veri Yedekleme", "External Hard Drives and Data Backup", "harici disk (external drive)", "veri (data)", "kapasite (capacity)", "dosya aktarımı (file transfer)", "yedek (backup)", "depolama (storage)"),
            ("İnternet Tarayıcı Eklentileri ve Verimlilik", "Browser Extensions and Productivity", "tarayıcı eklentisi (browser extension)", "reklam engelleyici (ad blocker)", "sekme (tab)", "verimlilik (productivity)", "ayarlar (settings)", "araç (tool)"),
            ("Kablosuz Kulaklıklar ve Ses Kalitesi", "Wireless Earbuds and Sound Quality", "kablosuz kulaklık (wireless earbuds)", "ses kalitesi (sound quality)", "gürültü engelleme (noise cancellation)", "şarj kutusu (charging case)", "müzik (music)", "mikrofon (microphone)"),
            ("Akıllı Ev Sistemleri ve Uzaktan Kontrol", "Smart Home Systems and Remote Control", "akıllı ev (smart home)", "termostat (thermostat)", "akıllı lamba (smart bulb)", "sensör (sensor)", "uzaktan kontrol (remote control)", "konfor (convenience)"),
            ("Yazılım Güncellemeleri ve Hata Düzeltmeleri", "Software Updates and Bug Fixes", "güncelleme (update)", "yazılım (software)", "hata düzeltmesi (bug fix)", "yama (patch)", "yükleme (install)", "kararlılık (stability)"),
            ("Dijital Fotoğrafçılık ve Düzenleme Araçları", "Digital Photography and Editing Tools", "dijital kamera (digital camera)", "çözünürlük (resolution)", "filtre (filter)", "düzenleme (editing)", "parlaklık (brightness)", "galeri (gallery)"),
            ("E-Posta Spam Filtreleri ve İstenmeyen İletiler", "Email Spam Filters and Unwanted Messages", "istenmeyen posta (spam)", "filtre (filter)", "gelen kutusu (inbox)", "engelleme (block)", "güvenilir (trusted)", "dolandırıcılık (phishing)"),
            ("Çevrim İçi Dosya Paylaşımı ve İndirme", "Online File Sharing and Downloading", "dosya paylaşımı (file sharing)", "indirme (download)", "yükleme (upload)", "bağlantı (url)", "sıkıştırılmış dosya (zip file)", "hız (bandwidth)"),
            ("Sanal Gerçeklik Gözlükleri ve Yeni Deneyimler", "Virtual Reality Headsets and New Experiences", "sanal gerçeklik (virtual reality)", "gözlük (headset)", "simülasyon (simulation)", "etkileşim (interaction)", "oyun (gaming)", "üç boyutlu (3D)"),
            ("Mobil Güç Kaynakları ve Powerbank Kullanımı", "Mobile Power Banks and Battery Backup", "taşınabilir şarj cihazı (power bank)", "kablo (cable)", "kapasite (capacity)", "hızlı şarj (fast charging)", "seyahat (travel)", "enerji (power)"),
            ("Çevrim İçi Haritalar ve Konum Paylaşımı", "Online Maps and Location Sharing", "harita (map)", "konum (location)", "rota (route)", "uydu görüntüsü (satellite view)", "trafik (traffic)", "işaretçi (pin)"),
            ("Tablet Bilgisayarlar ve Çizim Kalemleri", "Tablet Computers and Stylus Pens", "tablet (tablet)", "çizim kalemi (stylus)", "grafik (graphics)", "not alma (note taking)", "ekran (display)", "yaratıcılık (creativity)"),
            ("Dijital Ayak İzi ve Kişisel Gizlilik", "Digital Footprint and Personal Privacy", "dijital ayak izi (digital footprint)", "gizlilik (privacy)", "çerezler (cookies)", "tarama geçmişi (browsing history)", "güvenlik (security)", "izinler (permissions)")
        ]),

        # Cat 7: Seyahat, Dünya Kültürleri ve Turizm (151 - 175)
        ("Seyahat, Dünya Kültürleri ve Turizm", [
            ("Pasaport Çıkartma ve Vize Başvurusu", "Passport Issuance and Visa Application", "pasaport (passport)", "vize (visa)", "konsolosluk (consulate)", "başvuru formu (application form)", "fotoğraf (biometric photo)", "onay (approval)"),
            ("Havalimanında Güvenlik ve Uçağa Biniş", "Airport Security and Flight Boarding", "havalimanı (airport)", "güvenlik kontrolü (security check)", "biniş kartı (boarding pass)", "kapı (gate)", "anons (announcement)", "uçak (airplane)"),
            ("Bagaj Hazırlığı ve Seyahat Çantası", "Luggage Preparation and Travel Bag", "bavul (suitcase)", "sırt çantası (backpack)", "ağırlık limiti (weight limit)", "etiket (luggage tag)", "fermuar (zipper)", "kıyafet (clothing)"),
            ("Otel Girişi ve Rezervasyon Teyidi", "Hotel Check-In and Reservation Confirmation", "otel (hotel)", "rezervasyon (reservation)", "oda anahtarı (room key)", "kahvaltı (breakfast)", "lobi (lobby)", "giriş saati (check-in)"),
            ("Tarihi Şehir Turu ve Yerel Rehber", "Historic City Tour and Local Tour Guide", "turist (tourist)", "tur rehberi (tour guide)", "tarihi eser (historical monument)", "müze (museum)", "rehber kitap (guidebook)", "keşif (discovery)"),
            ("Yerel Mutfak Lezzetleri ve Yemek Kültürü", "Local Culinary Delights and Food Culture", "yerel lezzet (local cuisine)", "geleneksel yemek (traditional dish)", "baharat (spice)", "restoran (restaurant)", "garson (waiter)", "tatma (tasting)"),
            ("Döviz Bürosunda Para Bozdurma", "Currency Exchange at the Bureau", "döviz (foreign currency)", "kur (exchange rate)", "komisyon (fee)", "banknot (banknote)", "para bozdurma (money exchange)", "nakit (cash)"),
            ("Hediyelik Eşya Dükkanında Hatıralar", "Memories in the Souvenir Shop", "hediyelik eşya (souvenir)", "kartpostal (postcard)", "magnet (magnet)", "el işi (handicraft)", "pazarlık (bargaining)", "anı (keepsake)"),
            ("Uluslararası Tren Yolculuğu ve Manzaralar", "International Train Journey and Landscapes", "tren (train)", "kompartıman (compartment)", "pencere (window)", "manzara (scenery)", "istasyon (station)", "bilet kondüktörü (conductor)"),
            ("Sırt Çantalı Gezginler ve Hosteller", "Backpackers and Youth Hostels", "gezgin (backpacker)", "hostel (hostel)", "ranza (bunk bed)", "ortak mutfak (shared kitchen)", "macera (adventure)", "yeni arkadaşlar (new friends)"),
            ("Farklı Kültürler ve Selamlaşma Adetleri", "Diverse Cultures and Greeting Customs", "kültür (culture)", "gelenek (tradition)", "selamlaşma (greeting)", "saygı (respect)", "jest (gesture)", "farklılık (diversity)"),
            ("Tropikal Bir Sahilde Güneş ve Deniz", "Sun and Sea on a Tropical Beach", "kumsal (sandy beach)", "palmiye (palm tree)", "güneş şemsiyesi (sun umbrella)", "dalga (wave)", "yüzme (swimming)", "deniz kabuğu (seashell)"),
            ("Kırsal Dağ Köyünde Eko-Turizm", "Eco-Tourism in a Rural Mountain Village", "köy (village)", "dağ evi (chalet)", "organik kahvaltı (farm breakfast)", "huzur (peace)", "doğal güzellik (scenic beauty)", "misafirperverlik (hospitality)"),
            ("Gümrük Kapısında Kontrol Süreci", "Inspection Process at the Customs Checkpoint", "gümrük (customs)", "beyanname (declaration form)", "memur (officer)", "pul (stamp)", "sınır (border)", "vergi (duty)"),
            ("Şehir İçi Hop-on Hop-off Tur Otobüsü", "Hop-On Hop-Off City Sightseeing Bus", "tur otobüsü (sightseeing bus)", "açık üst kat (open-top deck)", "kulaklık (audio guide)", "durak (stop)", "manzara (sight)", "şehir turu (city tour)"),
            ("Seyahat Sigortası ve Acil Durum Teminatı", "Travel Insurance and Emergency Coverage", "seyahat sigortası (travel insurance)", "sağlık poliçesi (health policy)", "teminat (coverage)", "tazminat (claim)", "acil yardım (emergency assistance)", "güvence (guarantee)"),
            ("Eski Bir Kalede Zamanda Yolculuk", "Journey Through Time in an Ancient Castle", "kale (castle)", "sur (fortress wall)", "kule (tower)", "zindan (dungeon)", "tarih (history)", "orta çağ (middle ages)"),
            ("Antik Kalıntılar ve Arkeolojik Kazılar", "Ancient Ruins and Archaeological Excavations", "antik kent (ancient city)", "harabe (ruins)", "sütun (column)", "arkeolog (archaeologist)", "kazı (excavation)", "medeniyet (civilization)"),
            ("Gemi Turu ve Açık Deniz Seyahati", "Cruise Ship Tour and Open Sea Voyage", "kruvaziyer gemisi (cruise ship)", "kabin (cabin)", "güverte (deck)", "liman (port)", "deniz yolculuğu (voyage)", "kaptan (captain)"),
            ("Yabancı Dilde İletişim Kurma Çabası", "Effort to Communicate in a Foreign Language", "yabancı dil (foreign language)", "sözlük (dictionary)", "çeviri uygulaması (translation app)", "iletişim (communication)", "gülümseme (smile)", "pratik (practice)"),
            ("Kutup Işıklarını İzleme Macerası", "Adventure Watching the Northern Lights", "kuzey ışıkları (aurora borealis)", "gökyüzü (night sky)", "kar (snow)", "kızak (sled)", "soğuk hava (freezing weather)", "büyüleyici (breathtaking)"),
            ("Çölde Safari ve Deve Turu", "Desert Safari and Camel Tour", "çöl (desert)", "kum tepesi (sand dune)", "deve (camel)", "gün batımı (sunset)", "çadır (tent)", "kamp ateşi (campfire)"),
            ("Uzak Doğu Tapınaklarında Sessizlik", "Silence in Far Eastern Temples", "tapınak (temple)", "tütsü (incense)", "çan sesi (bell chime)", "saygı (reverence)", "avlu (courtyard)", "maneviyat (spirituality)"),
            ("Adrenalin Dolu Doğa Sporları", "Adrenaline-Filled Extreme Outdoor Sports", "rafting (whitewater rafting)", "yamaç paraşütü (paragliding)", "kask (helmet)", "can yeleği (life jacket)", "adrenalin (adrenaline)", "rehber (instructor)"),
            ("Eve Dönüş Yolu ve Biriken Hatıralar", "Journey Home and Accumulated Memories", "dönüş bileti (return ticket)", "uçuş (flight)", "hatıra defteri (travel diary)", "fotoğraf albümü (photo album)", "özlem (nostalgia)", "yolculuk (journey)")
        ]),

        # Cat 8: Sanat, Müzik, Sinema ve Eğlence (176 - 200)
        ("Sanat, Müzik, Sinema ve Eğlence", [
            ("Modern Sanat Galerisinde Sergi Açılışı", "Exhibition Opening at the Modern Art Gallery", "sanat galerisi (art gallery)", "sergi (exhibition)", "ressam (painter)", "tablo (painting)", "tuval (canvas)", "küratör (curator)"),
            ("Klasik Müzik Konseri ve Senfoni Orkestrası", "Classical Music Concert and Symphony Orchestra", "orkestra (orchestra)", "şef (conductor)", "keman (violin)", "piyano (piano)", "senfoni (symphony)", "alkış (applause)"),
            ("Tiyatro Salonunda Sahnelenen Oyun", "Play Staged in the Theater Hall", "tiyatro (theater)", "oyuncu (actor)", "sahne (stage)", "kostüm (costume)", "perde (curtain)", "senaryo (script)"),
            ("Sinemada Hafta Sonu Film Gösterimi", "Weekend Movie Screening at the Cinema", "sinema (cinema)", "film (movie)", "bilet (ticket)", "patlamış mısır (popcorn)", "koltuk (seat)", "beyaz perde (silver screen)"),
            ("Film Festivali ve Ödül Töreni", "Film Festival and Award Ceremony", "festival (festival)", "yönetmen (director)", "ödül (award)", "kırmızı halı (red carpet)", "jüri (jury)", "aday (nominee)"),
            ("Akustik Gitar ile Canlı Sokak Müziği", "Live Street Music with Acoustic Guitar", "gitar (guitar)", "müzisyen (musician)", "melodi (melody)", "ritim (rhythm)", "sokak (street)", "dinleyici (listener)"),
            ("Heykel Atölyesinde Kil ve Mermer", "Clay and Marble in the Sculpture Studio", "heykel (sculpture)", "heykeltıraş (sculptor)", "kil (clay)", "mermer (marble)", "keski (chisel)", "form (shape)"),
            ("Fotoğraf Sergisinde Siyah Beyaz Kareler", "Black and White Frames in the Photo Exhibition", "fotoğraf (photograph)", "ışık (lighting)", "kare (frame)", "mercek (lens)", "gölge (shadow)", "ifade (expression)"),
            ("Müzikal Tiyatroda Dans ve Şarkı", "Dance and Song in Musical Theater", "müzikal (musical)", "dansçı (dancer)", "koreografi (choreography)", "şarkı (song)", "canlı performans (live performance)", "coşku (enthusiasm)"),
            ("Popüler Müzik Albümü ve Stüdyo Kaydı", "Popular Music Album and Studio Recording", "albüm (album)", "stüdyo (studio)", "kayıt (recording)", "şarkıcı (singer)", "nakarat (chorus)", "yapımcı (producer)"),
            ("Geleneksel Halk Dansları Gösterisi", "Traditional Folk Dance Performance", "halk dansı (folk dance)", "yöresel kıyafet (traditional costume)", "davul (drum)", "zurna (folk flute)", "motif (pattern)", "kültürel miras (heritage)"),
            ("Çocuklar İçin Kukla Tiyatrosu", "Puppet Theater for Children", "kukla (puppet)", "kuklacı (puppeteer)", "ip (string)", "masal (fairytale)", "çocuk (child)", "kahkaha (laughter)"),
            ("Stand-Up Komedi Gecesi ve Mizah", "Stand-Up Comedy Night and Humor", "komedyen (comedian)", "mizah (humor)", "şaka (joke)", "mikrofon (microphone)", "seyirci (audience)", "eğlence (entertainment)"),
            ("Bale Gösterisi ve Zarif Figürler", "Ballet Performance and Graceful Movements", "bale (ballet)", "balerin (ballerina)", "tütü (tutu)", "zarafet (grace)", "müzik (music)", "adım (step)"),
            ("Doğa Belgeseli ve Seslendirme", "Nature Documentary and Voiceover", "belgesel (documentary)", "yaban hayatı (wildlife)", "seslendirme (voiceover)", "çekim (footage)", "doğa (nature)", "bilgi (knowledge)"),
            ("Çizgi Roman Fuarı ve Karakter Tasarımı", "Comic Con and Character Design", "çizgi roman (comic book)", "illüstrasyon (illustration)", "çizer (artist)", "kostüm (cosplay)", "çizgi (drawing)", "karakter (character)"),
            ("Müzede Rehber Eşliğinde Tarih Gezisi", "Guided History Tour at the Museum", "müze (museum)", "tarihi eser (artifact)", "cam vitrin (display case)", "açıklama (caption)", "rehber (guide)", "ziyaretçi (visitor)"),
            ("Caz Kulübünde Gece Dinletisi", "Night Performance at the Jazz Club", "caz (jazz)", "saksafon (saxophone)", "kontrbas (double bass)", "doğaçlama (improvisation)", "atmosfer (atmosphere)", "trompet (trumpet)"),
            ("Edebiyat Söyleşisi ve İmza Günü", "Literature Talk and Book Signing Event", "yazar (author)", "roman (novel)", "imza (signature)", "okur (reader)", "söyleşi (interview)", "kitapçı (bookstore)"),
            ("Sokak Sanatı ve Renkli Grafitiler", "Street Art and Colorful Graffiti", "grafiti (graffiti)", "sprey boya (spray paint)", "duvar (wall)", "sokak sanatı (street art)", "renk (color)", "mesaj (message)"),
            ("Açık Hava Sineması ve Yaz Akşamları", "Open-Air Cinema on Summer Evenings", "açık hava sineması (open-air cinema)", "yıldızlar (stars)", "minder (cushion)", "yaz gecesi (summer night)", "nostalji (nostalgia)", "film (film)"),
            ("Seramik Atölyesinde Çömlek Yapımı", "Pottery Making in the Ceramic Studio", "seramik (ceramics)", "çömlekçi çarkı (potter's wheel)", "çamur (clay)", "fırın (kiln)", "vazo (vase)", "sırlama (glazing)"),
            ("Gölge Oyunu ve Geleneksel Karagöz", "Shadow Play and Traditional Karagoz", "gölge oyunu (shadow play)", "perde (screen)", "tasvir (leather figure)", "ışık (light)", "nükte (wit)", "gelenek (tradition)"),
            ("Müzik Enstrümanı Çalmayı Öğrenme", "Learning to Play a Musical Instrument", "enstrüman (instrument)", "nota (music note)", "akor (chord)", "öğretmen (instructor)", "ders (lesson)", "pratik (practice)"),
            ("Sanat Eleştirisi ve Sergi Değerlendirmesi", "Art Criticism and Exhibition Review", "eleştiri (review)", "sanat eleştirmeni (art critic)", "yorum (commentary)", "estetik (aesthetics)", "dergi (magazine)", "başarı (success)")
        ]),

        # Cat 9: Kişisel Finans, Alışveriş ve Bütçe (201 - 225)
        ("Kişisel Finans, Alışveriş ve Bütçe", [
            ("Banka Hesabı Açtırma ve Banka Kartı", "Opening a Bank Account and Debit Card", "banka (bank)", "hesap (account)", "banka kartı (debit card)", "şube (branch)", "imza (signature)", "şifre (PIN)"),
            ("Aylık Ev Bütçesi ve Gider Planlaması", "Monthly Household Budget and Expense Planning", "bütçe (budget)", "gelir (income)", "gider (expense)", "kira (rent)", "tasarruf (savings)", "hesaplama (calculation)"),
            ("Süpermarkette Haftalık Mutfak Alışverişi", "Weekly Grocery Shopping at the Supermarket", "süpermarket (supermarket)", "alışveriş arabası (shopping cart)", "reyon (aisle)", "fiyat etiketi (price tag)", "kasa (cash register)", "fiş (receipt)"),
            ("Kredi Kartı Kullanımı ve Ekstre Kontrolü", "Credit Card Usage and Statement Check", "kredi kartı (credit card)", "ekstre (statement)", "limit (credit limit)", "asgari ödeme (minimum payment)", "borç (debt)", "taksit (installment)"),
            ("İndirim Sezonu ve Fırsat Ürünleri", "Discount Season and Bargain Items", "indirim (discount)", "kampanya (promotion)", "yüzde (percentage)", "etiket (label)", "fırsat (bargain)", "mağaza (store)"),
            ("Birikim Hesabı ve Faiz Getirisi", "Savings Account and Interest Earnings", "birikim hesabı (savings account)", "faiz (interest)", "mevduat (deposit)", "gelecek güvencesi (future security)", "fon (fund)", "para (money)"),
            ("Çevrim İçi Alışveriş ve Güvenli Ödeme", "Online Shopping and Secure Checkout", "çevrim içi alışveriş (online shopping)", "sepet (cart)", "kargo (shipping)", "güvenli ödeme (secure payment)", "teslimat (delivery)", "sipariş (order)"),
            ("Kusurlu Ürün İadesi ve Tüketici Hakları", "Defective Product Return and Consumer Rights", "iade (refund)", "değişim (exchange)", "kusurlu mal (defective good)", "tüketici hakkı (consumer rights)", "fatura (invoice)", "garanti belgesi (warranty)"),
            ("Acil Durum Fonu ve Beklenmedik Masraflar", "Emergency Fund and Unexpected Expenses", "acil durum fonu (emergency fund)", "beklenmedik masraf (unexpected expense)", "onarım (repair)", "tedbir (precaution)", "güvence (safety net)", "finansal (financial)"),
            ("Mobil Bankacılık ile Havale ve EFT", "Wire Transfer and EFT via Mobile Banking", "mobil bankacılık (mobile banking)", "havale (wire transfer)", "EFT (EFT transfer)", "IBAN (IBAN number)", "komisyon (transaction fee)", "dekont (receipt)"),
            ("Tasarruf Alışkanlığı ve Kumbara Kültürü", "Saving Habit and Money Box Culture", "kumbara (piggy bank)", "bozuk para (coins)", "tutumlu (thrifty)", "alışkanlık (habit)", "hedef (target)", "birikim (savings)"),
            ("Elektronik Ürünlerde Garanti Süresi", "Warranty Period in Electronic Products", "garanti süresi (warranty period)", "teknik servis (technical service)", "onarım (repair)", "yedek parça (spare part)", "ücretsiz (free of charge)", "belge (document)"),
            ("Bütçe Takip Uygulamaları ile Harcama Analizi", "Expense Analysis with Budget Tracking Apps", "bütçe uygulaması (budget app)", "kategori (category)", "harcama (spending)", "grafik (chart)", "limit (limit)", "kontrol (control)"),
            ("Semt Pazarında Taze Ürün Alışverişi", "Fresh Produce Shopping at the Local Bazaar", "pazar tezgahı (market stall)", "kilo (kilogram)", "taze sebze (fresh vegetable)", "para üstü (change)", "esnaf (vendor)", "pazarlık (haggling)"),
            ("Borç Yönetimi ve Düzenli Geri Ödeme", "Debt Management and Regular Repayment", "borç (debt)", "taksit (installment)", "ödeme planı (payment plan)", "vade (due date)", "kredi (loan)", "finansal özgürlük (financial freedom)"),
            ("Fatura Tasarrufu ve Elektrik Su Kullanımı", "Utility Bill Savings and Water-Electricity Use", "fatura (utility bill)", "elektrik (electricity)", "su sayacı (water meter)", "tasarruf (conservation)", "tüketim (consumption)", "ödeme (payment)"),
            ("Kasa Kuyruğu ve Temassız Ödeme", "Checkout Queue and Contactless Payment", "kasa (checkout counter)", "temassız ödeme (contactless payment)", "kart okuyucu (card reader)", "kasiyer (cashier)", "hızlı (quick)", "işlem (transaction)"),
            ("İkinci El Alışveriş ve Eşya Değerlendirme", "Second-Hand Shopping and Upcycling", "ikinci el (second-hand)", "uygun fiyat (affordable price)", "yenileme (upcycling)", "kullanılmış (pre-owned)", "tasarruf (economy)", "pazar (flea market)"),
            ("Yatırım Temelleri ve Altın Hesabı", "Investment Basics and Gold Accounts", "yatırım (investment)", "altın (gold)", "değer kazanma (appreciation)", "enflasyon (inflation)", "portföy (portfolio)", "güvenli liman (safe haven)"),
            ("Market Fiyatlarını Karşılaştırma", "Comparing Grocery Prices Across Markets", "fiyat karşılaştırması (price comparison)", "kalite (quality)", "hesaplı (economical)", "tercih (choice)", "indirim kataloğu (flyer)", "tasarruf (savings)"),
            ("Maaş Günü ve Finansal Öncelikler", "Payday and Financial Priorities", "maaş günü (payday)", "ücret (wage)", "dağıtım (allocation)", "kira (rent)", "temel ihtiyaç (basic need)", "rahatlama (relief)"),
            ("Sigorta Poliçeleri ve Risk Güvencesi", "Insurance Policies and Risk Coverage", "sigorta poliçesi (insurance policy)", "kasko (car insurance)", "prim (premium)", "risk (risk)", "güvence (protection)", "sözleşme (contract)"),
            ("Çocuklara Para Yönetimi Öğretme", "Teaching Money Management to Children", "harçlık (allowance)", "para yönetimi (money management)", "sorumluluk (responsibility)", "seçim (choice)", "biriktirme (saving)", "sabır (patience)"),
            ("Gereksiz Harcamaları Kesme ve Sadakat Programı", "Cutting Unnecessary Expenses and Loyalty Programs", "sadakat kartı (loyalty card)", "puan kazanma (earning points)", "gereksiz harcama (wasteful spending)", "fayda (benefit)", "ödül (reward)", "denge (balance)"),
            ("Yıllık Finansal Değerlendirme ve Gelecek Planı", "Annual Financial Review and Future Planning", "yıllık bilanço (annual balance)", "finansal hedef (financial goal)", "özet (summary)", "varlık (asset)", "gelecek planı (future plan)", "başarı (milestone)")
        ]),

        # Cat 10: Sosyal İlişkiler, Aile ve Topluluk (226 - 250)
        ("Sosyal İlişkiler, Aile ve Topluluk", [
            ("Eski Dostlarla Akşam Yemeği Buluşması", "Dinner Reunion with Old Friends", "arkadaşlık (friendship)", "akşam yemeği (dinner)", "sohbet (conversation)", "kahkaha (laughter)", "eski anılar (old memories)", "samimiyet (warmth)"),
            ("Geleneksel Aile Kahvaltısı ve Pazar Keyfi", "Traditional Family Breakfast and Sunday Pleasure", "aile (family)", "kahvaltı (breakfast)", "büyükanne (grandmother)", "torun (grandchild)", "çay (tea)", "birlik (togetherness)"),
            ("Yeni Taşınan Komşuyu Ziyaret Etme", "Visiting the Newly Moved Neighbor", "komşu (neighbor)", "ziyaret (visit)", "hoş geldin hediyesi (welcome gift)", "tanışma (introduction)", "nezaket (courtesy)", "yardımlaşma (neighborly help)"),
            ("Mahalle Gönüllüleri ve Park Temizliği", "Neighborhood Volunteers and Park Cleanup", "gönüllü (volunteer)", "topluluk (community)", "park (park)", "dayanışma (solidarity)", "temizlik (cleanup)", "ortak alan (common space)"),
            ("Empati Kurma ve Aktif Dinleme Sanatı", "Practicing Empathy and Active Listening", "empati (empathy)", "aktif dinleme (active listening)", "anlayış (understanding)", "iletişim (communication)", "destek (support)", "saygı (respect)"),
            ("Doğum Günü Sürpriz Partisi Hazırlığı", "Birthday Surprise Party Preparation", "doğum günü (birthday)", "sürpriz (surprise)", "pasta (cake)", "balon (balloon)", "hediye (present)", "kutlama (celebration)"),
            ("Fikir Ayrılıklarını Barışçıl Çözme", "Peacefully Resolving Disagreements", "anlaşmazlık (disagreement)", "çözüm (resolution)", "uzlaşma (compromise)", "hoşgörü (tolerance)", "sabır (patience)", "diyalog (dialogue)"),
            ("Kuşaklararası İletişim ve Yaşlılara Saygı", "Intergenerational Communication and Respect for the Elderly", "kuşak (generation)", "yaşlı (elderly)", "tecrübe (experience)", "saygı (reverence)", "öğüt (wisdom)", "ilgi (care)"),
            ("Zor Zamanlarda Dost Desteği", "Friendship Support in Difficult Times", "zor gün (tough time)", "moral (morale)", "omuz verme (support)", "teselli (comfort)", "vefa (loyalty)", "güven (trust)"),
            ("Sokak Hayvanlarını Besleme ve Koruma", "Feeding and Caring for Stray Animals", "sokak hayvanı (stray animal)", "mama (pet food)", "su kabı (water bowl)", "merhamet (compassion)", "veteriner (veterinarian)", "barınak (shelter)"),
            ("Düğün Töreni ve Evlilik Coşkusu", "Wedding Ceremony and Marriage Celebration", "düğün (wedding)", "gelin (bride)", "damat (groom)", "nikah (marriage vow)", "tebrik (congratulations)", "mutluluk (happiness)"),
            ("Bebek Ziyareti ve Yeni Doğan Sevinci", "Visiting a Newborn Baby", "yeni doğan (newborn)", "bebek (baby)", "beşik (crib)", "ziyaret (visit)", "sağlık dileği (well wishes)", "sevinç (joy)"),
            ("Kütüphanede Kitap Kulübü Toplantısı", "Book Club Meeting at the Library", "kitap kulübü (book club)", "roman (novel)", "tahlil (analysis)", "tartışma (discussion)", "fikir alışverişi (exchange of ideas)", "okuma (reading)"),
            ("Hasta Ziyareti ve Şifa Dilekleri", "Visiting the Sick and Wishing Healing", "hasta ziyareti (hospital visit)", "çiçek (flowers)", "geçmiş olsun (get well soon)", "moral verme (cheering up)", "şifa (recovery)", "dostluk (friendship)"),
            ("Apartman Yıllık Sakinler Toplantısı", "Annual Apartment Residents Meeting", "apartman toplantısı (residents meeting)", "yönetici (building manager)", "aidat (maintenance dues)", "ortak karar (joint decision)", "huzur (harmony)", "düzen (order)"),
            ("Huzurevi Ziyareti ve Sevgi Bağı", "Nursing Home Visit and Bonds of Affection", "huzurevi (nursing home)", "sohbet (chat)", "gönül alma (touching hearts)", "yalnızlık (loneliness)", "vefa (gratitude)", "sevgi (affection)"),
            ("Bayramlaşma Geleneği ve Ziyaretler", "Holiday Greeting Tradition and Visits", "bayram (holiday)", "ziyaret (visit)", "el öpme (hand-kissing)", "şeker (candy)", "kavuşma (reunion)", "gelenek (tradition)"),
            ("İş Arkadaşının Terfisini Kutlama", "Celebrating a Colleague's Promotion", "terfi (promotion)", "kutlama (celebration)", "tebrik kartı (congratulations card)", "ekip ruhu (team spirit)", "başarı (success)", "destek (support)"),
            ("Taziye Evi Ziyareti ve Paylaşılan Acı", "Condolence Visit and Shared Sorrow", "taziye (condolence)", "başsağlığı (sympathy)", "sabır dileği (wishing patience)", "dayanışma (solidarity)", "paylaşma (sharing)", "vefa (remembrance)"),
            ("Fidan Dikme Etkinliğinde Mahalle İmecesi", "Neighborhood Collective Work in Tree Planting", "imece (collective work)", "fidan dikimi (tree planting)", "kürek (shovel)", "dayanışma (cooperation)", "gelecek (future)", "yeşil (green)"),
            ("Okul Aile Birliği Kermesi", "Parent-Teacher Association Charity Fair", "kermes (charity bazaar)", "ev yapımı börek (homemade pastry)", "bağış (donation)", "öğrenci yararına (for students benefit)", "dayanışma (collaboration)", "okul (school)"),
            ("Çocukluk Arkadaşıyla Yıllar Sonra Karşılaşma", "Meeting a Childhood Friend Years Later", "çocukluk arkadaşı (childhood friend)", "tesadüf (coincidence)", "özlem (longing)", "nostalji (nostalgia)", "sarılma (embrace)", "anı (memory)"),
            ("Toplu Piknik ve Doğa İçinde Oyunlar", "Group Picnic and Games in Nature", "piknik (picnic)", "örtü (blanket)", "top oyunu (ball game)", "temiz hava (fresh air)", "neşeli sesler (cheerful voices)", "birliktelik (togetherness)"),
            ("Komşular Arasında Yemek Paylaşımı", "Food Sharing Among Neighbors", "bir tabak yemek (plate of food)", "ikram (treat)", "komşuluk hakkı (neighbor's right)", "sıcaklık (warmth)", "bereket (abundance)", "sevgi (love)"),
            ("Topluluk Ruhunun Gücü ve Birliktelik", "Power of Community Spirit and Unity", "topluluk ruhu (community spirit)", "birlik (unity)", "ortak gelecek (common future)", "huzur (peace)", "aidiyet (belonging)", "güven (safety)")
        ])
    ]

    return categories, b1_extra_categories

def generate_full_b1():
    main_cats, extra_cats = get_b1_categories()
    articles = []

    # First process Cat 1, 2, 3
    for cat in main_cats:
        for title_tr, title_en, text in cat["items"]:
            idx = len(articles) + 1
            vocab = extract_vocab_from_text(text)
            articles.append({
                "id": idx,
                "level": "B1",
                "category": cat["name"],
                "title_tr": title_tr,
                "title_en": title_en,
                "text": text,
                "vocab": vocab
            })

    # Rich category narrative templates for Cat 4 to 10
    cat_templates = {
        "Sağlık, Spor ve Beslenme": lambda t, w: (
            f"Sağlıklı bir yaşam sürdürme hedefinde {w[0]} hayati bir rol oynadı. "
            f"Alanında uzman bir {w[1]}, kişide görülen {w[2]} durumunu titizlikle değerlendirdi ve kapsamlı bir {w[3]} gerçekleştirdi. "
            f"Tıbbi değerlendirme sonrasında hekim, vücut dengesini korumak için uygun bir {w[4]} hazırladı. "
            f"Düzenli {w[5]} kullanımının ve bilinçli yaşam alışkanlıklarının sağlığı korumadaki gücü bir kez daha kanıtlandı."
        ),
        "Çevre, Doğa ve Geri Dönüşüm": lambda t, w: (
            f"Gezegenin geleceğini koruma mücadelesinde {w[0]} bilinci büyük bir dönüm noktası oldu. "
            f"Gönüllüler, çevreye yayılan zararlı {w[1]} miktarını kontrol altına almak için toplumsal farkındalık yarattı. "
            f"Doğada yüzyıllarca çözünmeyen {w[2]} kullanımını azaltmak amacıyla alternatif olarak {w[3]} ve {w[4]} gibi sürdürülebilir malzemeler tercih edildi. "
            f"Mahallenin her köşesine yerleştirilen ayrıştırma {w[5]} üniteleri, doğal kaynakların korunmasına kalıcı bir katkı sağladı."
        ),
        "Temel Teknoloji, Dijital Araçlar ve İnternet": lambda t, w: (
            f"Dijital çağın merkezinde yer alan {w[0]} teknolojisi günlük iletişimi dönüştürdü. "
            f"Kullanıcılar cihazın hassas {w[1]} donanımına dokunarak en sevdikleri {w[2]} programını hızla başlattı. "
            f"Kesintisiz bir {w[3]} deneyimi sağlayan modern sistemler sayesinde dünya genelinde hızlı bir {w[4]} ağı kuruldu. "
            f"Yüksek çözünürlüklü {w[5]} entegrasyonu ise kullanıcıların her anını kolayca paylaşmasına olanak tanıdı."
        ),
        "Seyahat, Dünya Kültürleri ve Turizm": lambda t, w: (
            f"Yeni bir coğrafyayı keşfetme heyecanı, resmi {w[0]} hazırlıklarıyla başladı. "
            f"Seyahat severler sınır ötesine geçebilmek için yetkili makamlardan onaylı {w[1]} belgesini temin etti. "
            f"Şehir merkezindeki yetkili {w[2]} binasında tamamlanan işlemlerin ardından eksiksiz bir {w[3]} dolduruldu. "
            f"Sisteme yüklenen güncel {w[4]} sonrasında alınan seyahat {w[5]} belgesi, unutulmaz bir maceranın kapısını araladı."
        ),
        "Sanat, Müzik, Sinema ve Eğlence": lambda t, w: (
            f"Kentin kültürel dokusunu zenginleştiren yeni bir {w[0]}, sanatseverlerin ilgi odağı haline geldi. "
            f"Açılış akşamı düzenlenen büyüleyici {w[1]}, yüzlerce ziyaretçiyi bir araya getirdi. "
            f"Eserlerini gururla tanıtan yetenekli {w[2]}, hayranlıkla izlenen bir {w[3]} önünde sanat anlayışını anlattı. "
            f"Geniş {w[4]} üzerine işlenen ustalıklı fırça darbeleri derin bir estetik haz uyandırdı. "
            f"Deneyimli bir {w[5]} tarafından hazırlanan rehber metin ise sanatın dönüştürücü gücünü gözler önüne serdi."
        ),
        "Kişisel Finans, Alışveriş ve Bütçe": lambda t, w: (
            f"Finansal bağımsızlık ve güvence kazanma sürecinde köklü bir {w[0]} kuruluşuyla çalışmak önemli bir adımdı. "
            f"Bireyler birikimlerini değerlendirmek amacıyla yeni bir mevduat {w[1]} tanımladı ve işlemler için güvenli bir {w[2]} aldı. "
            f"Müşteri temsilcisinin hizmet verdiği aydınlık {w[3]} ortamında sözleşmeye atılan resmi {w[4]} süreci tamamladı. "
            f"İşlemleri yetkisiz erişimlere karşı korumak için belirlenen gizli {w[5]} ise hesap güvenliğinin temelini oluşturdu."
        ),
        "Sosyal İlişkiler, Aile ve Topluluk": lambda t, w: (
            f"İnsan hayatını anlamlı kılan en güçlü bağlardan biri samimi bir {w[0]} ilişkisidir. "
            f"Birlikte geçirilen neşeli bir {w[1]} vaktinde bir araya gelen sevdiklerimiz, derin bir {w[2]} ile birbirlerine bağlandı. "
            f"Odayı dolduran içten {w[3]} sesleri, paylaşılan güzel anların yarattığı sıcaklığı yansıttı. "
            f"Yıllar sonra hatırlanan tatlı {w[4]}, insanlar arasındaki bağın ne kadar güçlü ve köklü bir {w[5]} duygusuna dayandığını gösterdi."
        )
    }

    # Process Cat 4 to 10
    for cat_name, items in extra_cats:
        template_fn = cat_templates[cat_name]
        for item in items:
            title_tr, title_en = item[0], item[1]
            words = item[2:]
            
            idx = len(articles) + 1
            text = template_fn(title_tr, words)
            vocab = extract_vocab_from_text(text)
            
            articles.append({
                "id": idx,
                "level": "B1",
                "category": cat_name,
                "title_tr": title_tr,
                "title_en": title_en,
                "text": text,
                "vocab": vocab
            })


    return articles

if __name__ == "__main__":
    arts = generate_full_b1()
    print(f"Generated {len(arts)} B1 articles.")
    assert len(arts) == 250, f"Expected 250 articles, got {len(arts)}"
    
    out_file = os.path.join(os.path.dirname(__file__), "..", "data", "articles_b1.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(arts, f, ensure_ascii=False, indent=2)
    print(f"Successfully saved 250 B1 articles to {out_file}")
