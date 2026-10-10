"""
Comprehensive B1 Article Generator (Makale 1 - 250).
Generates 10 categories with 25 articles each.
Outputs: data/articles_b1.json
"""

import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.common import extract_vocab_from_text

def get_cat1():
    # Makale 1 - 25: Modern Ofis ve İş Hayatına Giriş
    name = "Modern Ofis ve İş Hayatına Giriş"
    items = [
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
    return name, items

def get_cat2():
    # Makale 26 - 50: Üniversite Yaşamı ve Kampüs
    name = "Üniversite Yaşamı ve Kampüs"
    items = [
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
    return name, items

def get_cat3():
    # Makale 51 - 75: Şehir Yaşamı, Ulaşım ve Altyapı
    name = "Şehir Yaşamı, Ulaşım ve Altyapı"
    items = [
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
    return name, items

def build_all_b1():
    all_arts = []
    
    getters = [get_cat1, get_cat2, get_cat3]
    for getter in getters:
        cat_name, items = getter()
        for title_tr, title_en, text in items:
            idx = len(all_arts) + 1
            vocab = extract_vocab_from_text(text)
            all_arts.append({
                "id": idx,
                "level": "B1",
                "category": cat_name,
                "title_tr": title_tr,
                "title_en": title_en,
                "text": text,
                "vocab": vocab
            })
            
    return all_arts

if __name__ == "__main__":
    arts = build_all_b1()
    print(f"Total B1 generated so far: {len(arts)}")
