"""
Master Builder for IELTS 1000 Contextual Articles (B1 - C2).
Generates:
1. IELTS_1000_Articles_B1_C2.md (Single comprehensive Markdown file)
2. IELTS_1000_Articles_B1_C2.typ (Typst book source)
3. IELTS_1000_Articles_B1_C2.pdf (Publication-grade single PDF file)
4. README.md (Comprehensive documentation and learning guide)
"""

import os
import sys
import json
import subprocess
import time
import re

# Base directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def load_all_articles():
    all_articles = []
    for lvl in ["b1", "b2", "c1", "c2"]:
        p = os.path.join(BASE_DIR, "data", f"articles_{lvl}.json")
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
            all_articles.extend(data)
            
    assert len(all_articles) == 1000, f"Expected 1000 articles, got {len(all_articles)}"
    for i, a in enumerate(all_articles):
        assert a["id"] == i + 1, f"Article index mismatch at {i}: id {a['id']}"
    return all_articles

def build_markdown(articles, out_path):
    print("Generating IELTS_1000_Articles_B1_C2.md ...")
    lines = []
    
    # Title & Metadata
    lines.append("# IELTS & Akademik İngilizce İçin Bağlam Odaklı 1000 Türkçe Makale")
    lines.append("## *1000 Contextual Reading Passages for IELTS & Academic English Mastery (B1 - C2)*\n")
    lines.append("> **Eser Türü:** Bağlamsal Dil Edinimi & Akademik IELTS Kelime Kitabı  ")
    lines.append("> **Hedef Seviye:** CEFR B1 - C2 (Orta Düzeyden Üst Düzey Ustalığa)  ")
    lines.append("> **Kapsam:** 1000 Özgün Türkçe Okuma Parçası & 5.700+ Bağlamsal İngilizce Hedef Kelime  ")
    lines.append("> **Metodoloji:** Hedef kelimelerin doğal Türkçe anlatı akışı içerisinde parantez içi gösterimi `Türkçe_anlam (english_word)`\n")
    lines.append("---\n")
    
    # Introduction & Methodology Guide
    lines.append("## Önsöz ve Çalışma Metodolojisi\n")
    lines.append("Bu eser, geleneksel soyut kelime listelerini ezberleme yönteminin ötesine geçerek, **bağlamsal öğrenme (contextual acquisition)** prensibini temel alır. ")
    lines.append("İnsan beyni, yeni bir kavramı izole edilmiş bir kelime kartından ziyade, anlamlı bir olay örgüsü, zihinsel imge ve duygu yüklü bir cümle içinde çok daha hızlı ve kalıcı biçimde kodlar.\n")
    lines.append("### Nasıl Çalışılmalı?\n")
    lines.append("1. **Akıcı Okuma Yapın:** Her makaleyi ilk okuyuşta duraksamadan, hikayenin veya akademik argümanın ana fikrini yakalayarak okuyun. Parantez içindeki İngilizce kelimeleri zihninizde Türkçe bağlamıyla eşleştirin.")
    lines.append("2. **Kelime Kutusunu İnceleyin:** Parçanın altında yer alan *Hedef Kelimeler (Target Vocabulary)* bölümünü gözden geçirin; kelimenin türünü (isim, fiil, sıfat, zarf) ve temel anlamını pekiştirin.")
    lines.append("3. **Kendi Cümlenizi Kurun (Aktif Hatırlama):** Okuduğunuz parçadaki en az iki hedef kelimeyi seçerek kendi İngilizce cümlenizde kullanın (Writing & Speaking transferi).")
    lines.append("4. **Kademeli İlerleme:** Kitap, B1 düzeyinden C2 düzeyine doğru zorluk ve akademik derinlik açısından kademeli olarak yükselmektedir. Günde 10-15 makale okuyarak 2-3 ay içerisinde IELTS Academic Reading & Writing sınavlarında karşılaşacağınız tüm akademik kelime dağarcığını kalıcı olarak edinebilirsiniz.\n")
    lines.append("---\n")

    # Table of Contents
    lines.append("## İçindekiler Tablosu (Table of Contents)\n")
    lines.append("- [Bölüm 1: B1 Seviyesi (Intermediate) – Makale 1 - 250](#bölüm-1-b1-seviyesi-intermediate--makale-1---250)")
    lines.append("- [Bölüm 2: B2 Seviyesi (Upper-Intermediate) – Makale 251 - 550](#bölüm-2-b2-seviyesi-upper-intermediate--makale-251---550)")
    lines.append("- [Bölüm 3: C1 Seviyesi (Advanced) – Makale 551 - 850](#bölüm-3-c1-seviyesi-advanced--makale-551---850)")
    lines.append("- [Bölüm 4: C2 Seviyesi (Proficiency / Mastery) – Makale 851 - 1000](#bölüm-4-c2-seviyesi-proficiency--mastery--makale-851---1000)\n")
    lines.append("---\n")

    current_section = None
    for a in articles:
        # Check if we should insert section header
        lvl = a["level"]
        if lvl != current_section:
            current_section = lvl
            if lvl == "B1":
                lines.append("\n# Bölüm 1: B1 Seviyesi (Intermediate) – Makale 1 - 250\n")
                lines.append("*Günlük ve profesyonel yaşama giriş, kampüs dinamikleri, seyahat, çevre ve temel teknoloji.*  \n---\n")
            elif lvl == "B2":
                lines.append("\n# Bölüm 2: B2 Seviyesi (Upper-Intermediate) – Makale 251 - 550\n")
                lines.append("*Kurumsal strateji, yenilenebilir enerji, bilişsel psikoloji, veri bilimi, hukuk ve pedagoji.*  \n---\n")
            elif lvl == "C1":
                lines.append("\n# Bölüm 3: C1 Seviyesi (Advanced) – Makale 551 - 850\n")
                lines.append("*İleri bilimsel metodoloji, jeopolitik dengeler, yapay zeka etiği, nörobiyoloji ve anayasa hukuku.*  \n---\n")
            elif lvl == "C2":
                lines.append("\n# Bölüm 4: C2 Seviyesi (Proficiency / Mastery) – Makale 851 - 1000\n")
                lines.append("*Ontoloji, epistemolojik kırılmalar, hermenötik, kuantum kozmolojisi, yüce estetik ve tekillik.*  \n---\n")

        # Format article
        vocab_lines = "\n".join([f"> - **{v['word']}**: {v['tr']} *({v['pos']})*" for v in a["vocab"]])
        article_md = f"""### Makale {a['id']}: {a['title_tr']} | {a['title_en']} [{a['level']} - {a['category']}]

{a['text']}

> **Hedef Kelimeler (Target Vocabulary):**
{vocab_lines}
"""
        lines.append(article_md)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Created {out_path} ({os.path.getsize(out_path) / 1024:.1f} KB)")

def build_typst_and_pdf(articles, typ_path, pdf_path):
    print("Generating IELTS_1000_Articles_B1_C2.typ ...")
    
    typ_content = []
    
    # Document Setup & Styling
    typ_content.append('''
#set page(
  paper: "a4",
  margin: (top: 2.2cm, bottom: 2.2cm, left: 2cm, right: 1.8cm),
  header: context [
    #let page_num = counter(page).get().first()
    #if page_num > 2 [
      #grid(
        columns: (1fr, 1fr),
        align(left)[#text(size: 8pt, fill: rgb("#64748b"))[IELTS 1000 Bağlam Odaklı Okuma Makalesi]],
        align(right)[#text(size: 8pt, fill: rgb("#64748b"))[B1 - C2 Kelime Hazinesi]]
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
    ]
  ],
  footer: context [
    #let page_num = counter(page).get().first()
    #if page_num > 1 [
      #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
      #v(2pt)
      #grid(
        columns: (1fr, 1fr),
        align(left)[#text(size: 8pt, fill: rgb("#94a3b8"))[IELTS & Academic English Mastery]],
        align(right)[#text(size: 8pt, fill: rgb("#94a3b8"))[Sayfa #counter(page).display()]]
      )
    ]
  ]
)

#set text(font: ("Charter", "Helvetica Neue", "Arial"), lang: "tr", size: 9pt)
#set par(justify: true, leading: 0.65em)

// Cover Page
#align(center + horizon)[
  #block(
    fill: rgb("#0f172a"),
    inset: 35pt,
    radius: 12pt,
    width: 100%,
    [
      #text(fill: rgb("#38bdf8"), size: 14pt, weight: "bold", tracking: 2pt)[IELTS & AKADEMİK İNGİLİZCE]\\
      #v(10pt)
      #text(fill: white, size: 28pt, weight: "bold")[BAĞLAM ODAKLI\\ 1000 TÜRKÇE MAKALE]\\
      #v(8pt)
      #text(fill: rgb("#94a3b8"), size: 13pt, style: "italic")[1000 Contextual Reading Passages for IELTS Mastery (B1 - C2)]\\
      #v(20pt)
      #line(length: 60%, stroke: 2pt + rgb("#38bdf8"))
      #v(20pt)
      #grid(
        columns: (1fr, 1fr, 1fr, 1fr),
        align: center,
        block(fill: rgb("#1e293b"), inset: 8pt, radius: 4pt, text(fill: rgb("#38bdf8"), weight: "bold", size: 10pt)[B1 Intermediate]),
        block(fill: rgb("#1e293b"), inset: 8pt, radius: 4pt, text(fill: rgb("#38bdf8"), weight: "bold", size: 10pt)[B2 Upper-Int]),
        block(fill: rgb("#1e293b"), inset: 8pt, radius: 4pt, text(fill: rgb("#38bdf8"), weight: "bold", size: 10pt)[C1 Advanced]),
        block(fill: rgb("#1e293b"), inset: 8pt, radius: 4pt, text(fill: rgb("#38bdf8"), weight: "bold", size: 10pt)[C2 Mastery])
      )
      #v(25pt)
      #text(fill: rgb("#cbd5e1"), size: 10pt)[5.700+ Bağlamsal Hedef Kelime • Tek Eser • Kapsamlı Başvuru Kitabı]\\
      #v(15pt)
      #text(fill: rgb("#64748b"), size: 9pt)[Yazar & Geliştirici: Ali Turgut Bozkurt • 2026]
    ]
  )
]

#pagebreak()

// Introduction Page
#v(1cm)
#text(size: 20pt, weight: "bold", fill: rgb("#0f172a"))[Önsöz ve Metodoloji Rehberi]
#v(0.3cm)
#line(length: 100%, stroke: 1.5pt + rgb("#2563eb"))
#v(0.5cm)

Bu eser, geleneksel izole kelime listesi ezberleme yöntemine güçlü bir alternatif olarak *Bağlamsal Kelime Edinimi (Contextual Vocabulary Acquisition)* pedagojisi üzerine inşa edilmiştir.

#block(
  fill: rgb("#eff6ff"),
  inset: 12pt,
  radius: 6pt,
  stroke: 1pt + rgb("#bfdbfe"),
  [
    #text(weight: "bold", fill: rgb("#1e40af"))[Kitabın Temel İlkeleri:]
    - *Doğal Türkçe Akış:* Her makale kendi içinde bütünlüğü olan akıcı bir Türkçe anlatı sunar.
    - *Bağlam İçi Kelime Eşleşmesi:* Hedef İngilizce kelimeler, Türkçe karşılıklarının hemen ardından parantez içinde vurgulu olarak verilir: `ergonomik koltuğu (chair) çekip...`
    - *Kademeli Zorluk:* B1 seviyesinden C2 seviyesine uzanan 4 ana bölüm ve 36 alt tematik kategori ile dil yetkinliğinizi sıfırdan zirveye taşır.
    - *Kelime Kartları:* Her makalenin bitiminde yer alan özet panel, öğrenilen terimleri türleri (isim, fiil, sıfat) ile birlikte pekiştirir.
  ]
)

#v(0.8cm)
#text(size: 14pt, weight: "bold", fill: rgb("#1e293b"))[İçindekiler ve Bölüm Dağılımı]
#v(0.2cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 15pt,
  block(
    fill: rgb("#f8fafc"),
    inset: 10pt,
    radius: 4pt,
    stroke: 0.5pt + rgb("#e2e8f0"),
    [
      #text(weight: "bold", fill: rgb("#2563eb"))[Bölüm 1: B1 Seviyesi (Makale 1 - 250)]\\
      - Modern Ofis ve İş Hayatı (1 - 25)\\
      - Üniversite ve Kampüs Yaşamı (26 - 50)\\
      - Şehir Yaşamı, Ulaşım ve Altyapı (51 - 75)\\
      - Sağlık, Spor ve Beslenme (76 - 100)\\
      - Çevre, Doğa ve Geri Dönüşüm (101 - 125)\\
      - Temel Teknoloji ve İnternet (126 - 150)\\
      - Seyahat ve Dünya Kültürleri (151 - 175)\\
      - Sanat, Müzik ve Sinema (176 - 200)\\
      - Kişisel Finans ve Alışveriş (201 - 225)\\
      - Sosyal İlişkiler ve Topluluk (226 - 250)
    ]
  ),
  block(
    fill: rgb("#f8fafc"),
    inset: 10pt,
    radius: 4pt,
    stroke: 0.5pt + rgb("#e2e8f0"),
    [
      #text(weight: "bold", fill: rgb("#0f766e"))[Bölüm 2: B2 Seviyesi (Makale 251 - 550)]\\
      - Kurumsal Yönetişim ve Strateji (251 - 280)\\
      - Yenilenebilir Enerji ve İklim (281 - 310)\\
      - Bilişsel Psikoloji ve Davranış (311 - 340)\\
      - Yazılım Mühendisliği ve Büyük Veri (341 - 370)\\
      - Küresel Ticaret ve Pazarlar (371 - 400)\\
      - Modern Hukuk ve Adalet (401 - 430)\\
      - Çağdaş Mimari ve Kentsel Tasarım (431 - 460)\\
      - Biyomedikal ve Halk Sağlığı (461 - 490)\\
      - Medya Etiği ve Habercilik (491 - 520)\\
      - Pedagoji ve Eğitim Bilimleri (521 - 550)
    ]
  )
)

#v(0.3cm)
#grid(
  columns: (1fr, 1fr),
  gutter: 15pt,
  block(
    fill: rgb("#f8fafc"),
    inset: 10pt,
    radius: 4pt,
    stroke: 0.5pt + rgb("#e2e8f0"),
    [
      #text(weight: "bold", fill: rgb("#7c3aed"))[Bölüm 3: C1 Seviyesi (Makale 551 - 850)]\\
      - Bilimsel Metodoloji ve Hipotez (551 - 580)\\
      - Jeopolitik ve Uluslararası Güç (581 - 610)\\
      - Yapay Zeka Etiği ve Otonomi (611 - 640)\\
      - Gen Düzenleme ve Biyoetik (641 - 670)\\
      - Nörobiyoloji ve Zihin Felsefesi (671 - 700)\\
      - Ekonometri ve Parasal Teori (701 - 730)\\
      - Antroposen ve Ekolojik Kriz (731 - 760)\\
      - Karşılaştırmalı Anayasa Hukuku (761 - 790)\\
      - Sosyolojik Teori ve Hegemonya (791 - 820)\\
      - Bilim Felsefesi ve Paradigmalar (821 - 850)
    ]
  ),
  block(
    fill: rgb("#f8fafc"),
    inset: 10pt,
    radius: 4pt,
    stroke: 0.5pt + rgb("#e2e8f0"),
    [
      #text(weight: "bold", fill: rgb("#b91c1c"))[Bölüm 4: C2 Seviyesi (Makale 851 - 1000)]\\
      - Ontoloji ve Radikal Metafizik (851 - 875)\\
      - İleri Dilbilim ve Semiyotik (876 - 900)\\
      - Kuantum Kozmolojisi ve Uzay-Zaman (901 - 925)\\
      - Yüksek Devlet Aklı ve Realpolitik (926 - 950)\\
      - Edebi Kuram ve Yüce Estetik (951 - 975)\\
      - Transhümanizm ve Geleceğin Ontolojisi (976 - 1000)
    ]
  )
)

#pagebreak()
''')

    current_section = None
    colors = {
        "B1": "#2563eb",
        "B2": "#0f766e",
        "C1": "#7c3aed",
        "C2": "#b91c1c"
    }

    for a in articles:
        lvl = a["level"]
        accent = colors.get(lvl, "#2563eb")
        
        # Section Divider Page
        if lvl != current_section:
            current_section = lvl
            titles = {
                "B1": ("Bölüm 1: B1 Seviyesi (Intermediate)", "Makale 1 - 250 • Günlük Yaşam, İş Dünyası, Kampüs ve Temel İletişim"),
                "B2": ("Bölüm 2: B2 Seviyesi (Upper-Intermediate)", "Makale 251 - 550 • Profesyonel Yönetişim, Sürdürülebilirlik, Psikoloji ve Teknoloji"),
                "C1": ("Bölüm 3: C1 Seviyesi (Advanced)", "Makale 551 - 850 • Akademik Metodoloji, Jeopolitika, Nörobilim ve Hukuk"),
                "C2": ("Bölüm 4: C2 Seviyesi (Proficiency / Mastery)", "Makale 851 - 1000 • Ontoloji, Kuantum Kozmolojisi, Hermenötik ve Tekillik")
            }
            sec_title, sec_desc = titles[lvl]
            typ_content.append(f'''
#pagebreak()
#v(3cm)
#align(center)[
  #block(
    fill: rgb("{accent}").lighten(90%),
    inset: 25pt,
    radius: 8pt,
    stroke: 1.5pt + rgb("{accent}"),
    width: 90%,
    [
      #text(fill: rgb("{accent}"), size: 22pt, weight: "bold")[{sec_title}]\\
      #v(10pt)
      #text(fill: rgb("#334155"), size: 11pt, style: "italic")[{sec_desc}]
    ]
  )
]
#v(2cm)
''')

        # Format Article in Typst
        text = a['text']
        for c in ['\\', '#', '$', '@', '<', '>']:
            text = text.replace(c, '\\' + c)
            
        def repl(m):
            w = m.group(1)
            return f'#text(fill: rgb("{accent}"), weight: "bold")[({w})]'
        
        formatted_text = re.sub(r'\(([a-zA-Z\s\-\'/]+)\)', repl, text)
        vocab_items = " | ".join([f"• *{v['word']}*: {v['tr']} ({v['pos']})" for v in a['vocab']])
        
        art_block = f'''
#block(
  width: 100%,
  stroke: (left: 2.5pt + rgb("{accent}")),
  inset: (left: 8pt),
  [
    #text(weight: "bold", size: 11pt, fill: rgb("#0f172a"))[Makale {a['id']}: {a['title_tr']}] #h(6pt) #text(size: 8pt, fill: rgb("{accent}"), weight: "bold")[[{a['level']} • {a['category']}]]\\
    #text(size: 8pt, fill: rgb("#64748b"), style: "italic")[{a['title_en']}]
  ]
)
#v(3pt)
{formatted_text}

#v(3pt)
#block(
  fill: rgb("#f8fafc"),
  inset: (x: 8pt, y: 5pt),
  radius: 3pt,
  stroke: 0.5pt + rgb("#e2e8f0"),
  width: 100%,
  [
    #text(size: 7.5pt, weight: "bold", fill: rgb("#334155"))[Hedef Kelimeler (Target Vocabulary):] \\
    #text(size: 7.5pt, fill: rgb("#475569"))[{vocab_items}]
  ]
)
#v(0.25cm)
'''
        typ_content.append(art_block)

    with open(typ_path, "w", encoding="utf-8") as f:
        f.write("\n".join(typ_content))
    print(f"Created {typ_path} ({os.path.getsize(typ_path) / 1024:.1f} KB)")

    print(f"Compiling Typst to PDF: {pdf_path} ...")
    t0 = time.time()
    res = subprocess.run(["typst", "compile", typ_path, pdf_path], capture_output=True, text=True)
    t1 = time.time()
    if res.returncode != 0:
        print("Typst compile error:")
        print(res.stderr)
        sys.exit(1)
    print(f"Compiled PDF successfully in {t1 - t0:.2f}s! ({os.path.getsize(pdf_path) / (1024*1024):.2f} MB)")

def build_readme(articles, out_path):
    print("Generating README.md ...")
    total_vocab = sum(len(a['vocab']) for a in articles)
    b1_count = sum(1 for a in articles if a['level'] == 'B1')
    b2_count = sum(1 for a in articles if a['level'] == 'B2')
    c1_count = sum(1 for a in articles if a['level'] == 'C1')
    c2_count = sum(1 for a in articles if a['level'] == 'C2')

    readme = f"""# IELTS & Akademik İngilizce İçin Bağlam Odaklı 1000 Türkçe Makale (B1 - C2)
*1000 Contextual Reading Passages for IELTS & Academic English Mastery*

Bu proje, IELTS Academic Reading ve Writing sınavlarına hazırlanan, akademik metinleri anlama kabiliyetini geliştirmek isteyen ve İngilizce kelime dağarcığını **bağlam içerisinde (contextual learning)** kalıcı olarak edinmeyi hedefleyen adaylar için geliştirilmiş dev bir başvuru eseridir.

---

## 📊 Eser İstatistikleri

| Metrik | Değer |
| :--- | :--- |
| **Toplam Makale Sayısı** | **1.000 Özgün Makale** |
| **Toplam Hedef Kelime** | **{total_vocab:,}+ Bağlamsal Kelime Kullanımı** |
| **Seviye Dağılımı** | B1 ({b1_count}), B2 ({b2_count}), C1 ({c1_count}), C2 ({c2_count}) |
| **Tematik Kategori Sayısı** | **36 Ana Kategori** |
| **Tek Markdown Dosyası** | [`IELTS_1000_Articles_B1_C2.md`](./IELTS_1000_Articles_B1_C2.md) |
| **Tek PDF Kitap Dosyası** | [`IELTS_1000_Articles_B1_C2.pdf`](./IELTS_1000_Articles_B1_C2.pdf) |
| **Derleme Motoru** | Typst 0.15+ (Yüksek Performanslı Dizgi Motoru) |

---

## 🎯 Metodoloji ve Pedagojik Yaklaşım

Geleneksel ezber yöntemlerinde kelimeler soyut bir liste halinde sunulur ve beyin bu kelimeleri gerçek bir bağlamla ilişkilendiremediği için kısa sürede unutur.

Bu kitapta uygulanan **Bağlamsal Dil Edinimi Modeli**'nde:
1. Anadilde (Türkçe) akıcı, sürükleyici ve tutarlı bir anlatı sunulur.
2. Hedef İngilizce kavramlar, cümlenin doğal sözdizimi içerisinde ve tam anlamına denk düşecek şekilde parantez içerisinde belirtilir:
   > *...Alex ergonomik koltuğu **(chair)** çekip oturduğunda masanın **(desk)** üzerindeki kablosuz klavyeyi **(keyboard)** ve fareyi **(mouse)** fark etti...*
3. Her makalenin altında, kelimelerin sözlük biçimi ve dilbilgisel kategorisi (isim, fiil, sıfat) pratik bir özet kartı halinde verilir.

---

## 📚 Bölüm ve Kategori Dağılımı

### 🔵 Bölüm 1: B1 Düzeyi (Orta Düzey - Makale 1 - 250)
- Modern Ofis ve İş Hayatına Giriş (Makale 1 - 25)
- Üniversite ve Kampüs Yaşamı (Makale 26 - 50)
- Şehir Yaşamı, Ulaşım ve Altyapı (Makale 51 - 75)
- Sağlık, Beden Zindeliği ve Beslenme (Makale 76 - 100)
- Çevre, Doğa ve Geri Dönüşüm (Makale 101 - 125)
- Temel Teknoloji, Dijital Cihazlar ve İnternet (Makale 126 - 150)
- Seyahat, Dünya Kültürleri ve Turizm (Makale 151 - 175)
- Sanat, Müzik, Sinema ve Eğlence (Makale 176 - 200)
- Kişisel Finans, Alışveriş ve Bütçe (Makale 201 - 225)
- Sosyal İlişkiler, Aile ve Topluluk (Makale 226 - 250)

### 🟢 Bölüm 2: B2 Düzeyi (İleri-Orta Düzey - Makale 251 - 550)
- Kurumsal Yönetişim ve Stratejik Planlama (Makale 251 - 280)
- Yenilenebilir Enerji ve Sürdürülebilirlik (Makale 281 - 310)
- Bilişsel Psikoloji ve Davranış Bilimleri (Makale 311 - 340)
- Yazılım Mühendisliği ve Büyük Veri (Makale 341 - 370)
- Küresel Ticaret ve Dış Pazarlar (Makale 371 - 400)
- Modern Hukuk ve Adalet Sistemleri (Makale 401 - 430)
- Çağdaş Mimari ve Kentsel Tasarım (Makale 431 - 460)
- Biyomedikal Bilimler ve Halk Sağlığı (Makale 461 - 490)
- Medya Etiği ve Dijital İletişim (Makale 491 - 520)
- Pedagojik İnovasyon ve Eğitim Bilimleri (Makale 521 - 550)

### 🟣 Bölüm 3: C1 Düzeyi (İleri Düzey - Makale 551 - 850)
- İleri Düzey Bilimsel Metodoloji ve Hipotez Testi (Makale 551 - 580)
- Jeopolitik Dinamikler ve Uluslararası Diplomasi (Makale 581 - 610)
- Yapay Zeka Etiği ve Otonom Sistemler (Makale 611 - 640)
- Gen Düzenleme ve Biyoetik Sınırlar (Makale 641 - 670)
- Nörobiyoloji ve Zihin Felsefesi (Makale 671 - 700)
- Ekonometri ve Makroekonomik Teori (Makale 701 - 730)
- Antroposen ve Ekolojik Sistemler (Makale 731 - 760)
- Karşılaştırmalı Anayasa Hukuku ve İnsan Hakları (Makale 761 - 790)
- Sosyolojik Teori ve Postmodern Eleştiri (Makale 791 - 820)
- Bilim Felsefesi ve Epistemolojik Dönüşüm (Makale 821 - 850)

### 🔴 Bölüm 4: C2 Düzeyi (Ustalık Düzeyi - Makale 851 - 1000)
- Ontoloji ve Radikal Metafizik (Makale 851 - 875)
- İleri Dilbilim ve Hermenötik Göstergebilim (Makale 876 - 900)
- Teorik Astrofizik ve Kuantum Kozmolojisi (Makale 901 - 925)
- Yüksek Devlet Aklı ve Realpolitik (Makale 926 - 950)
- Edebi Kuram ve İleri Estetik (Makale 951 - 975)
- Transhümanizm ve Geleceğin Epistemolojisi (Makale 976 - 1000)

---

## 🛠️ Derleme ve Çalıştırma

Projeyi yerel ortamınızda baştan oluşturmak için:

```bash
# 1. Depoyu klonlayın
git clone https://github.com/aliturgutbozkurt/IELTS-Articles.git
cd IELTS-Articles

# 2. Python ile veri setlerini ve dosyaları derleyin
python3 scripts/build_master.py
```

Derleme sonucunda projenin kök dizininde `IELTS_1000_Articles_B1_C2.md` ve `IELTS_1000_Articles_B1_C2.pdf` dosyaları otomatik olarak üretilir.

---

## 📄 Lisans ve Haklar
Bu çalışma, dil öğrenimini herkes için erişilebilir kılmak amacıyla açık kaynak ve kamuya açık olarak sunulmuştur. Tüm hakları saklıdır © 2026 Ali Turgut Bozkurt.
"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(readme.strip() + "\n")
    print(f"Created {out_path}")

def main():
    print("=" * 60)
    print("MASTER BUILD PROCESS FOR IELTS 1000 ARTICLES")
    print("=" * 60)
    t_start = time.time()
    
    articles = load_all_articles()
    print(f"Loaded {len(articles)} validated articles.")
    
    md_path = os.path.join(BASE_DIR, "IELTS_1000_Articles_B1_C2.md")
    typ_path = os.path.join(BASE_DIR, "IELTS_1000_Articles_B1_C2.typ")
    pdf_path = os.path.join(BASE_DIR, "IELTS_1000_Articles_B1_C2.pdf")
    readme_path = os.path.join(BASE_DIR, "README.md")
    
    build_markdown(articles, md_path)
    build_typst_and_pdf(articles, typ_path, pdf_path)
    build_readme(articles, readme_path)
    
    t_end = time.time()
    print("=" * 60)
    print(f"ALL DELIVERABLES COMPLETED SUCCESSFULLY in {t_end - t_start:.2f}s!")
    print(f"1. Markdown: {md_path}")
    print(f"2. PDF:      {pdf_path}")
    print(f"3. README:   {readme_path}")
    print("=" * 60)

if __name__ == "__main__":
    main()
