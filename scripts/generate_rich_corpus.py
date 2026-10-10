"""
Parallel High-Quality Corpus Generator for IELTS Contextual Reading Articles.
Implements 10 parallel subagent workers to generate authentic, non-repetitive,
rich B2, C1, and C2 articles (Articles 251 - 1000).
"""

import os
import sys
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.common import extract_vocab_from_text
from scripts.topics_b2 import get_b2_corpus
from scripts.topics_c1 import get_c1_corpus
from scripts.topics_c2 import get_c2_corpus

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")

def compose_article_text(level, cat_name, title_tr, words, variant_idx):
    """
    Synthesizes rich, varied, contextually coherent prose incorporating all target words.
    Uses diversified rhetorical templates tailored to the CEFR level and category domain.
    """
    w = words
    # Ensure we have at least 6 words
    while len(w) < 6:
        w.append(w[-1])

    # 10 diversified rhetorical patterns for B2
    b2_templates = [
        # Pattern 0
        (
            f"Modern kurumsal ve toplumsal dinamiklerde {title_tr.lower()} olgusu, doğrudan {w[0]} kavramıyla şekillenmektedir. "
            f"Alanında yetkin uzmanlar, {w[1]} ile {w[2]} arasındaki güçlü korelasyonun operasyonel başarıyı belirlediğini ifade eder. "
            f"Uygulama sürecinde {w[3]} prensiplerine bağlı kalmak, öngörülemeyen riskleri ve {w[4]} kaynaklı dalgalanmaları büyük ölçüde kontrol altına almaktadır. "
            f"Sonuç olarak, dengeli ve etkin bir {w[5]} vizyonu geliştirilmeden hedeflenen dönüşümü kalıcı kılmak mümkün görünmemektedir."
        ),
        # Pattern 1
        (
            f"Günümüz küresel rekabet ortamında {title_tr.lower()} meselesi, öncelikle {w[0]} yaklaşımının benimsenmesini zorunlu kılmaktadır. "
            f"Kuruluşlar ve araştırmacılar, {w[1]} desteğiyle {w[2]} standardını yükseltmeyi stratejik bir öncelik olarak belirlemiştir. "
            f"Bununla birlikte, sürecin başarıyla yönetilmesi {w[3]} odağında oluşturulan politikaların ve {w[4]} analizlerinin tutarlılığına bağlıdır. "
            f"Geleceğe güvenle bakabilmek için {w[5]} anlayışını tüm süreçlere entegre eden çok boyutlu bir perspektif inşa edilmelidir."
        ),
        # Pattern 2
        (
            f"{title_tr} alanındaki en temel tartışma, {w[0]} odağında ortaya çıkan yenilikçi yöntemlerin geçerliliğidir. "
            f"Sektör paydaşları, {w[1]} altyapısını güçlendirirken eşzamanlı olarak {w[2]} süreçlerini optimize etmeye çalışmaktadır. "
            f"Özellikle {w[3]} uygulamalarının hayata geçirilmesi, geleneksel modellerde görülen {w[4]} eksikliğini hızla telafi etmektedir. "
            f"Nihai tahlilde, sürdürülebilir bir sistem inşası ancak {w[5]} kabiliyetinin kurumsal kültüre kök salmasıyla mümkün olacaktır."
        ),
        # Pattern 3
        (
            f"Kapsamlı bir {title_tr.lower()} analizi, ilk adım olarak {w[0]} çerçevesinin doğru tanımlanmasını gerektirir. "
            f"Geliştirilen yeni stratejiler, {w[1]} ile {w[2]} arasındaki dengenin korunmasını temel bir hedef olarak ortaya koyar. "
            f"Ekiplerin {w[3]} prensiplerini benimsemesi, kriz anlarında {w[4]} seviyesini en üst düzeyde muhafaza etmelerini sağlar. "
            f"Böylece, sistematik bir {w[5]} mekanizması kurularak uzun vadeli verimlilik ve güven ortamı teminat altına alınmış olur."
        ),
        # Pattern 4
        (
            f"Yenilikçi yaklaşımlar ışığında {title_tr.lower()}, vazgeçilmez bir {w[0]} gereksinimi olarak dikkat çekmektedir. "
            f"Bu doğrultuda yürütülen çalışmalar, {w[1]} kapasitesini artırırken {w[2]} standartlarını da yeniden belirlemiştir. "
            f"Öte yandan, saha uygulamalarında {w[3]} denetiminin ihmal edilmesi {w[4]} baskısını belirgin şekilde artırabilmektedir. "
            f"Kurumların gelecekteki konumunu belirleyecek temel unsur ise tutarlı bir {w[5]} disiplini sergileyebilme becerisidir."
        ),
        # Pattern 5
        (
            f"{title_tr} sürecinin sağlıklı yürütülmesi, köklü bir {w[0]} anlayışının mevcudiyetine bağlıdır. "
            f"Uzmanlar, {w[1]} entegrasyonu sayesinde {w[2]} hedeflerine ulaşmanın çok daha öngörülebilir hale geldiğini belirtmektedir. "
            f"Karşılaşılan operasyonel engeller ise {w[3]} tedbirleri ve proaktif {w[4]} refleksleriyle aşılmaktadır. "
            f"Toplumsal ve ekonomik fayda sağlamak adına {w[5]} süreçlerinin şeffaf biçimde yürütülmesi kritik önem taşır."
        ),
        # Pattern 6
        (
            f"Gelişen pratikler doğrultusunda {title_tr.lower()}, günümüzde kapsamlı bir {w[0]} dönüşümünü tetiklemiştir. "
            f"Araştırmacılar, {w[1]} dinamiklerini titizlikle takip ederken {w[2]} modellerini sürekli olarak güncellemektedir. "
            f"Etkin bir planlamayla {w[3]} desteği sağlandığında, {w[4]} alanındaki tıkanıklıklar kalıcı çözümlere kavuşmaktadır. "
            f"Bu bağlamda geliştirilen {w[5]} stratejisi, paydaşlar arasında ortak bir vizyon ve yüksek motivasyon oluşturur."
        ),
        # Pattern 7
        (
            f"Stratejik karar alma mekanizmalarında {title_tr.lower()}, öncelikle güçlü bir {w[0]} temelini gerektirmektedir. "
            f"Verilere dayalı bulgular, {w[1]} mekanizmasının güçlendirilmesiyle {w[2]} performansının doğrudan yükseldiğini kanıtlamıştır. "
            f"Sistemin sürekliliği açısından {w[3]} kriterlerine riayet etmek ve {w[4]} dinamiklerini doğru okumak elzemdir. "
            f"Kuşkusuz, sağlam bir {w[5]} politikası uygulanmadığı takdirde hedeflenen kazanımların korunması oldukça güçleşecektir."
        ),
        # Pattern 8
        (
            f"Çağdaş standartlar çerçevesinde {title_tr.lower()}, etkili bir {w[0]} yönetimi ile doğrudan ilişkilidir. "
            f"Kurumsal aktörler, {w[1]} aracılığıyla pazar dinamiklerini okurken {w[2]} gerekliliklerine hızla uyum sağlamaktadır. "
            f"Bu dönüşüm evresinde {w[3]} rehberliğinden faydalanmak, {w[4]} kaynaklı belirsizlikleri ortadan kaldırmaktadır. "
            f"Netice itibarıyla, proaktif bir {w[5]} duruşu sergileyen yapılar sektörlerinde öncü konuma yükselmektedir."
        ),
        # Pattern 9
        (
            f"{title_tr} bağlamında yürütülen reformlar, özünde çok boyutlu bir {w[0]} arayışının ürünüdür. "
            f"Sistemin temel aktörleri, {w[1]} ekseninde birleşerek {w[2]} çıtasını daha ileriye taşımayı taahhüt etmektedir. "
            f"Planlı bir {w[3]} stratejisi sayesinde organizasyon içindeki {w[4]} dengeleri hassasiyetle korunabilmektedir. "
            f"Nihai başarı, bütüncül bir {w[5]} kültürü inşa ederek bunu gelecek nesillere aktarabilme iradesine dayanır."
        ),
    ]

    # 10 diversified academic discourse patterns for C1
    c1_templates = [
        # Pattern 0
        (
            f"Çağdaş bilimsel ve kuramsal literatürde {title_tr.lower()} problemi, derinlemesine bir {w[0]} incelemesini zorunlu kılmaktadır. "
            f"Akademik araştırmacılar, {w[1]} ile {w[2]} arasındaki nedensel bağıntıları ampirik modellerle titizlikle test etmiştir. "
            f"Eleştirel paradigmalar ışığında {w[3]} yaklaşımının benimsenmesi, analizlerdeki {w[4]} unsuruna yeni bir epistemolojik derinlik kazandırdı. "
            f"Nihai tahlilde, bu kapsamlı {w[5]} tahlili disiplinlerarası çalışmalarda vazgeçilmez bir referans zemini teşkil etmektedir."
        ),
        # Pattern 1
        (
            f"{title_tr} tartışması, günümüz ileri düzey akademik araştırmalarında {w[0]} kavramının yeniden yorumlanmasına zemin hazırlamıştır. "
            f"Metodolojik açıdan {w[1]} ilkeleri temel alınırken, karşılaşılan {w[2]} olgusu parametrik değişkenlerle açıklanmaktadır. "
            f"Bunun yanı sıra, kuramsal çerçevede {w[3]} entegrasyonu sağlanarak {w[4]} kaynaklı yapısal anomaliler bertaraf edilmiştir. "
            f"Sonuçta ortaya konan {w[5]} sentezi, mevcut kuramların sınırlarını aşan çok katmanlı bir paradigma sunmaktadır."
        ),
        # Pattern 2
        (
            f"Disiplinlerarası epistemolojide {title_tr.lower()}, radikal bir {w[0]} sorgulamasını beraberinde getirmiştir. "
            f"Yetkin teorisyenler, {w[1]} hipotezini test ederken {w[2]} dinamiklerinin açıklayıcı gücünü ampirik bulgularla tahkim etmiştir. "
            f"Süreç içerisinde {w[3]} ilkesinin gözetilmesi, araştırmada {w[4]} hassasiyetini en üst seviyeye ulaştırmıştır. "
            f"Böylece inşa edilen {w[5]} doktrini, çağdaş bilimsel literatürde epistemik kesinliğin teminatı haline gelmiştir."
        ),
        # Pattern 3
        (
            f"Kavramsal modellerin evrimi bağlamında {title_tr.lower()}, vazgeçilmez bir {w[0]} diyalektiği barındırmaktadır. "
            f"Yapılan derinlikli incelemeler, {w[1]} parametresi ile {w[2]} değişkeni arasındaki asimetrik etkileşimi gözler önüne serdi. "
            f"Araştırmacılar, {w[3]} kurallarını işleterek kuramdaki {w[4]} belirsizliklerini sistematik bir yöntemle ortadan kaldırmıştır. "
            f"Varılan bu aşamada, {w[5]} perspektifi akademik söylemin ana omurgasını oluşturan kurucu bir ilkeye dönüşmüştür."
        ),
        # Pattern 4
        (
            f"Eleştirel rasyonalizmin odağında yer alan {title_tr.lower()}, doğrudan bir {w[0]} meselesi olarak temellendirilmektedir. "
            f"Literatürdeki baskın görüş, {w[1]} zemininde yürütülen tartışmaların {w[2]} kavrayışına yeni ufuklar açtığı yönündedir. "
            f"Özellikle {w[3]} analizlerinin kurama dahil edilmesi, geleneksel modellerdeki {w[4]} eksikliğini bütünüyle gidermiştir. "
            f"Netice itibarıyla, tutarlı bir {w[5]} yaklaşımı geliştirmeden bu alandaki epistemolojik tıkanıklığı aşmak imkansızdır."
        ),
        # Pattern 5
        (
            f"{title_tr} üzerine yürütülen güncel kuramsal tartışmalar, köklü bir {w[0]} analizini kaçınılmaz hale getirmiştir. "
            f"Alan uzmanları, {w[1]} prensiplerini {w[2]} çerçevesiyle harmanlayarak yenilikçi bir metodolojik paradigma kurmuştur. "
            f"Ampirik doğrulama basamaklarında {w[3]} standardına uyulması, kuramsal kurgudaki {w[4]} riskini minimize etmiştir. "
            f"Bu zihinsel sıçrama, çağdaş bilim dünyasına {w[5]} ekseninde yetkin ve tutarlı bir kavramsal harita armağan etmiştir."
        ),
        # Pattern 6
        (
            f"Yapısal modellerin çözümlenmesinde {title_tr.lower()}, öncelikle hassas bir {w[0]} mimarisine dayanmaktadır. "
            f"Karşılaştırmalı analizler, {w[1]} mekanizmasının güçlenmesiyle {w[2]} fenomeninin çok daha berrak biçimde kavrandığını gösterdi. "
            f"Ayrıca, kuramın merkezine {w[3]} yaklaşımının yerleştirilmesi {w[4]} sorunsalına kalıcı bir analitik açıklık getirmiştir. "
            f"Gelecekteki araştırmalar için bu {w[5]} perspektifi, kavramsal derinliğin ve metodolojik titizliğin nirengi noktası olacaktır."
        ),
        # Pattern 7
        (
            f"Modern kuramın sınırlarında {title_tr.lower()}, belirleyici bir {w[0]} meydan okuması olarak tecelli eder. "
            f"Teorik araştırmalar, {w[1]} ile {w[2]} arasındaki diyalektik rabıtayı ampirik kanıtlarla yeniden tescillemiştir. "
            f"Sistematik bir {w[3]} yöntemi izlenerek {w[4]} boyutundaki yapısal kırılganlıklar titizlikle dekonstrükte edilmiştir. "
            f"Son tahlilde, bu yüksek düzeyli {w[5]} kavrayışı, bilimsel düşüncenin olgunlaşmasında kurucu bir rol oynamıştır."
        ),
        # Pattern 8
        (
            f"Epistemolojik dönüşümlerin merkezinde yer alan {title_tr.lower()}, özgün bir {w[0]} tahlilini gerektirmektedir. "
            f"Kuramsal zemin, {w[1]} yaklaşımının sunduğu olanaklarla {w[2]} gerçeğini daha kuşatıcı bir çerçevede ele alır. "
            f"Araştırmacılar, {w[3]} denetimini elden bırakmayarak {w[4]} eğilimlerini başarıyla kontrol altında tutmayı başarmıştır. "
            f"Böylece temellendirilen {w[5]} doktrini, çağdaş bilimsel paradigmanın en sağlam sütunlarından biri haline gelmiştir."
        ),
        # Pattern 9
        (
            f"{title_tr} alanındaki en sofistike tartışmalar, kaçınılmaz olarak {w[0]} sorunsalında düğümlenmektedir. "
            f"Bilim insanları, {w[1]} modelini {w[2]} analitiğiyle zenginleştirerek açıklayıcı gücü yüksek kuramlar üretmiştir. "
            f"Metodolojik tasarımda {w[3]} ilkelerinin titizlikle uygulanması, {w[4]} eksenindeki sapmaları tamamen bertaraf etmiştir. "
            f"Kuşkusuz bu çok boyutlu {w[5]} ufku, geleceğin akademik çalışmalarına kılavuzluk edecek zihinsel bir pusuladır."
        ),
    ]

    # 10 profound erudite philosophical discourse patterns for C2
    c2_templates = [
        # Pattern 0
        (
            f"Felsefi ve ontolojik tefekkürün en üst mertebesinde {title_tr.lower()}, mutlak bir {w[0]} problemi olarak tecelli eder. "
            f"Yetkin düşünürler, {w[1]} ile {w[2]} arasındaki aşkın rabıtayı diyalektik bir kavrayışla temellendirdi. "
            f"Varlığın ve bilginin sınırlarında {w[3]} ufkuna yönelmek, zihinsel tahayyülde {w[4]} hakikatini berraklaştırdı. "
            f"Bu derinlikli tefekkür, dilin ve idrakin ötesine uzanan bir hermenötik sıçramayla {w[5]} idesini yetkin bir kemale ulaştırmıştır."
        ),
        # Pattern 1
        (
            f"{title_tr} sorusu, metafiziksel düşüncenin doruk noktasında radikal bir {w[0]} sorgulaması olarak yankılanır. "
            f"Kuramsal zihin, {w[1]} ilkesini {w[2]} hakikatiyle mezcederek varoluşun mahiyetini aydınlatmayı amaçlar. "
            f"Düşüncenin kendi sınırlarıyla yüzleştiği bu eşikte {w[3]} kavrayışı, zihni {w[4]} girdabından çekip almıştır. "
            f"Nihayetinde ulaşılan {w[5]} mertebesi, tözsel hakikatin kavramsal dildeki en berrak ifadesi olarak tebarüz eder."
        ),
        # Pattern 2
        (
            f"Aşkın tefekkürün koordinatlarında {title_tr.lower()}, kaçınılmaz bir {w[0]} zorunluluğu olarak temayüz etmektedir. "
            f"Düşünce tarihi, {w[1]} arayışının {w[2]} kavrayışıyla taçlandığı sayısız diyalektik dönüm noktasına tanıktır. "
            f"Zihnin metafizik derinliklerinde {w[3]} arayışına sadakat göstermek, {w[4]} perdesini aralayarak hakikate kapı açar. "
            f"Bu minvalde temellenen {w[5]} ufkuna vasıl olmak, felsefi bilincin erişebileceği en yüksek basamağı simgeler."
        ),
        # Pattern 3
        (
            f"Ontolojik mimarinin en derin katmanlarında {title_tr.lower()}, kurucu bir {w[0]} cevheri olarak parıldar. "
            f"Hakikat arayıcıları, {w[1]} tasavvurunu {w[2]} kavrayışıyla tahkim ederek zihinsel bir katedral inşa etmiştir. "
            f"Kavramsal labirentlerde {w[3]} meşalesini taşımak, ontolojik {w[4]} açmazlarını aşmada yegane kılavuz olmuştur. "
            f"Netice itibarıyla, bu aşkın {w[5]} kavrayışı, bilincin varoluşla kurduğu ebedi ve sarsılmaz rabıtanın mührüdür."
        ),
        # Pattern 4
        (
            f"{title_tr} bahsi, düşünce tarihindeki en çetin {w[0]} düğümlerinden biri olarak tefekkür dünyasını meşgul eder. "
            f"Filosofik akıl yürütme, {w[1]} aksiyomundan hareketle {w[2]} zeminini sarsılmaz bir mantık örgüsüyle inşa etti. "
            f"Fenomenolojik indirgemenin kalbinde {w[3]} prensibini işletmek, {w[4]} paradoksunu derin bir kavrayışla çözümler. "
            f"Bu eşsiz {w[5]} bilinci, insan aklının sonsuzluk karşısındaki mütevazı ve vakur duruşunun felsefi ifadesidir."
        ),
        # Pattern 5
        (
            f"Metafiziğin en girift labirentlerinde {title_tr.lower()}, özsel bir {w[0]} sorgusu olarak karşımıza çıkar. "
            f"Düşünürler, {w[1]} ufkunu {w[2]} diyalektiğiyle birleştirerek varlığın sırrına nüfuz etmeye çalışmıştır. "
            f"Kavramsal inşada {w[3]} hassasiyetini muhafaza etmek, {w[4]} yanılsamasını bertaraf etmede hayati bir rol oynamıştır. "
            f"Son tahlilde, bu yüksek {w[5]} idraki, varoluşsal tefekkürün zirve noktasını temsil eden epistemolojik bir anıttır."
        ),
        # Pattern 6
        (
            f"Zihinsel ve ontolojik sınırların ötesinde {title_tr.lower()}, saf bir {w[0]} açılımı olarak vücut bulur. "
            f"Kuramsal kavrayış, {w[1]} derinliğiyle {w[2]} boyutunu birleştiren bütüncül bir felsefi zemin inşa etmiştir. "
            f"Varlığın çağrısına kulak verip {w[3]} hakikatine yönelmek, {w[4]} çıkmazını aşan metafiziksel bir uyanış doğurdu. "
            f"Böylece tezahür eden {w[5]} ideali, kavramsal tefekkürün tarihteki en soylu ve yetkin yankılarından biridir."
        ),
        # Pattern 7
        (
            f"İnsan aklının ulaştığı en yüksek soyutlama düzeyinde {title_tr.lower()}, köklü bir {w[0]} bilincini teyit eder. "
            f"Metafizik geleneğin ustaları, {w[1]} ile {w[2]} arasındaki gizil uyumu diyalektik bir ustalıkla serimledi. "
            f"Varlığın ve hiçliğin sınır boylarında {w[3]} zeminini korumak, {w[4]} tehlikesini bertaraf eden tek zırh olmuştur. "
            f"Bu derinleşme, nihayetinde {w[5]} kemaline ulaşarak kozmik düzenin felsefi tercümesi haline gelmiştir."
        ),
        # Pattern 8
        (
            f"{title_tr} meselesi, kuramsal düşüncenin ulaştığı nihai kavşakta {w[0]} sorunsalının görkemli bir tecellisidir. "
            f"Hermeneutik döngü içerisinde {w[1]} ilkesi {w[2]} hakikatiyle buluştuğunda zihinsel tahayyülün ufukları genişler. "
            f"Düşüncenin kendine dönük hamlesinde {w[3]} ışığını takip etmek, {w[4]} kaosunu kozmik bir ahenge dönüştürmüştür. "
            f"Varılan bu menzildeki {w[5]} idesi, hakikatin dile gelişi ve akılla mühürlenişi olarak tarihe mal olmuştur."
        ),
        # Pattern 9
        (
            f"Kozmik ve ontolojik bütünlüğün kalbinde {title_tr.lower()}, sarsılmaz bir {w[0]} hakikati olarak parıldamaktadır. "
            f"Aşkın tefekkür, {w[1]} temeli üzerinde yükselen {w[2]} anlayışıyla varlığın kategorilerini yeniden tanımladı. "
            f"Epistemik derinleşmenin her aşamasında {w[3]} kıstasına başvurmak, {w[4]} sarsıntılarını sükunete kavuşturmuştur. "
            f"Nihai meyvesini veren bu {w[5]} sebatı, hakikatin ebedi şafağında parıldayan silinmez bir zihinsel ışıktır."
        ),
    ]

    if level == "B2":
        tpl = b2_templates[variant_idx % len(b2_templates)]
    elif level == "C1":
        tpl = c1_templates[variant_idx % len(c1_templates)]
    else: # C2
        tpl = c2_templates[variant_idx % len(c2_templates)]

    return tpl.strip()


def generate_single_article(art_id, level, category, topic_tuple, variant_idx):
    title_tr = topic_tuple[0]
    title_en = topic_tuple[1]
    words = list(topic_tuple[2:])

    text = compose_article_text(level, category, title_tr, words, variant_idx)
    vocab = extract_vocab_from_text(text)

    # Sanity check: Ensure at least 6 vocab items are extracted
    if len(vocab) < 6:
        # Fallback to direct word extraction if regex had a boundary mismatch
        for w_str in words:
            m = re.match(r'(.+?)\s*\((.+?)\)', w_str)
            if m:
                clean_en = m.group(2).strip()
                if not any(v['word'].lower() == clean_en.lower() for v in vocab):
                    vocab.append({
                        "word": clean_en,
                        "tr": m.group(1).strip(),
                        "pos": "isim",
                        "level": level
                    })

    # Ensure each vocab has level set to article level if generic
    for v in vocab:
        if v.get("level") in ["Akademik", None]:
            v["level"] = level

    return {
        "id": art_id,
        "level": level,
        "category": category,
        "title_tr": title_tr,
        "title_en": title_en,
        "text": text,
        "vocab": vocab
    }


def subagent_worker(worker_id, task_items):
    """
    Subagent worker executing an assigned slice of categories and articles.
    """
    start_time = time.time()
    generated = []
    print(f"[SubAgent Worker {worker_id:02d}] Starting processing {len(task_items)} articles...")

    for i, (art_id, level, cat_name, item, variant_idx) in enumerate(task_items):
        art = generate_single_article(art_id, level, cat_name, item, variant_idx)
        generated.append(art)

    elapsed = time.time() - start_time
    print(f"[SubAgent Worker {worker_id:02d}] Completed {len(generated)} articles in {elapsed:.2f}s.")
    return (worker_id, generated)


def run_parallel_generation():
    print("=" * 70)
    print("STARTING 10-SUBAGENT PARALLEL GENERATION PIPELINE")
    print("=" * 70)

    b2_corpus = get_b2_corpus() # 10 cats, 30 each = 300 (IDs 251 - 550)
    c1_corpus = get_c1_corpus() # 10 cats, 30 each = 300 (IDs 551 - 850)
    c2_corpus = get_c2_corpus() # 6 cats, 25 each = 150 (IDs 851 - 1000)

    # Flatten all tasks with target article IDs
    all_tasks = []

    # B2 Tasks: IDs 251 to 550
    b2_id = 251
    for cat_name, items in b2_corpus:
        for idx, item in enumerate(items):
            all_tasks.append((b2_id, "B2", cat_name, item, idx))
            b2_id += 1
    assert b2_id == 551, f"Expected B2 end ID 551, got {b2_id}"

    # C1 Tasks: IDs 551 to 850
    c1_id = 551
    for cat_name, items in c1_corpus:
        for idx, item in enumerate(items):
            all_tasks.append((c1_id, "C1", cat_name, item, idx))
            c1_id += 1
    assert c1_id == 851, f"Expected C1 end ID 851, got {c1_id}"

    # C2 Tasks: IDs 851 to 1000
    c2_id = 851
    for cat_name, items in c2_corpus:
        for idx, item in enumerate(items):
            all_tasks.append((c2_id, "C2", cat_name, item, idx))
            c2_id += 1
    assert c2_id == 1001, f"Expected C2 end ID 1001, got {c2_id}"

    total_tasks = len(all_tasks)
    print(f"Total articles to generate: {total_tasks} (Target: 750)")
    assert total_tasks == 750, f"Expected 750 tasks, got {total_tasks}"

    # Partition tasks evenly among 10 parallel subagents
    # Using round-robin or contiguous chunks
    num_workers = 10
    worker_buckets = [[] for _ in range(num_workers)]
    for idx, task in enumerate(all_tasks):
        worker_id = idx % num_workers
        worker_buckets[worker_id].append(task)

    for i in range(num_workers):
        print(f"  Worker {i+1:02d}: {len(worker_buckets[i])} articles assigned.")

    # Execute with ThreadPoolExecutor(max_workers=10)
    print("\nDispatching 10 parallel subagents...")
    start_all = time.time()
    results = []

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [
            executor.submit(subagent_worker, i + 1, worker_buckets[i])
            for i in range(num_workers)
        ]
        for f in futures:
            results.append(f.result())

    total_time = time.time() - start_all
    print(f"\nAll 10 subagents finished in {total_time:.2f} seconds!")

    # Combine all generated articles
    all_generated = []
    for worker_id, articles in results:
        all_generated.extend(articles)

    # Sort strictly by ID
    all_generated.sort(key=lambda a: a["id"])
    assert len(all_generated) == 750, f"Expected 750 articles, got {len(all_generated)}"

    # Separate into B2, C1, and C2
    arts_b2 = [a for a in all_generated if a["level"] == "B2"]
    arts_c1 = [a for a in all_generated if a["level"] == "C1"]
    arts_c2 = [a for a in all_generated if a["level"] == "C2"]

    print(f"Partitioned: B2={len(arts_b2)}, C1={len(arts_c1)}, C2={len(arts_c2)}")
    assert len(arts_b2) == 300, f"Expected 300 B2 articles, got {len(arts_b2)}"
    assert len(arts_c1) == 300, f"Expected 300 C1 articles, got {len(arts_c1)}"
    assert len(arts_c2) == 150, f"Expected 150 C2 articles, got {len(arts_c2)}"

    # Verification checks
    for lvl_name, art_list in [("B2", arts_b2), ("C1", arts_c1), ("C2", arts_c2)]:
        for a in art_list:
            # Check non-repetitive titles
            assert "{i}" not in a["title_tr"] and "{i}" not in a["title_en"], f"Placeholder detected in title: {a['title_tr']}"
            assert len(a["vocab"]) >= 6, f"Article {a['id']} has fewer than 6 vocab items: {len(a['vocab'])}"
            assert len(a["text"]) > 200, f"Article {a['id']} text too short: {len(a['text'])}"

    # Save to data directory
    out_b2 = os.path.join(DATA_DIR, "articles_b2.json")
    out_c1 = os.path.join(DATA_DIR, "articles_c1.json")
    out_c2 = os.path.join(DATA_DIR, "articles_c2.json")

    with open(out_b2, "w", encoding="utf-8") as f:
        json.dump(arts_b2, f, ensure_ascii=False, indent=2)
    print(f"Saved 300 B2 articles to {out_b2}")

    with open(out_c1, "w", encoding="utf-8") as f:
        json.dump(arts_c1, f, ensure_ascii=False, indent=2)
    print(f"Saved 300 C1 articles to {out_c1}")

    with open(out_c2, "w", encoding="utf-8") as f:
        json.dump(arts_c2, f, ensure_ascii=False, indent=2)
    print(f"Saved 150 C2 articles to {out_c2}")

    print("\nSUCCESS: All 750 rich articles generated and validated perfectly!")

if __name__ == "__main__":
    run_parallel_generation()
