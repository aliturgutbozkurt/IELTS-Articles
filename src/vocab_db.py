"""
Vocabulary Database and Helper Functions for IELTS 1000 Contextual Articles.
Maps English target words to their Turkish definitions, parts of speech, and CEFR level.
"""

VOCAB_DB = {
    # B1 Words
    "chair": {"tr": "koltuk, sandalye", "pos": "isim", "level": "B1"},
    "desk": {"tr": "çalışma masası", "pos": "isim", "level": "B1"},
    "keyboard": {"tr": "klavye", "pos": "isim", "level": "B1"},
    "mouse": {"tr": "fare (bilgisayar)", "pos": "isim", "level": "B1"},
    "shelf": {"tr": "raf", "pos": "isim", "level": "B1"},
    "paper": {"tr": "kağıt", "pos": "isim", "level": "B1"},
    "notebook": {"tr": "not defteri", "pos": "isim", "level": "B1"},
    "pen": {"tr": "tükenmez kalem", "pos": "isim", "level": "B1"},
    "password": {"tr": "şifre, parola", "pos": "isim", "level": "B1"},
    "screen": {"tr": "ekran", "pos": "isim", "level": "B1"},
    "arrive": {"tr": "varmak, ulaşmak", "pos": "fiil", "level": "B1"},
    "guard": {"tr": "güvenlik görevlisi", "pos": "isim", "level": "B1"},
    "entrance": {"tr": "giriş", "pos": "isim", "level": "B1"},
    "badge": {"tr": "kimlik kartı, yaka kartı", "pos": "isim", "level": "B1"},
    "reception": {"tr": "danışma, karşılama", "pos": "isim", "level": "B1"},
    "guide": {"tr": "rehber, kılavuz", "pos": "isim", "level": "B1"},
    "elevator": {"tr": "asansör", "pos": "isim", "level": "B1"},
    "scan": {"tr": "taramak, okutmak", "pos": "fiil", "level": "B1"},
    "lobby": {"tr": "lobi, giriş salonu", "pos": "isim", "level": "B1"},
    "gather": {"tr": "toplanmak, bir araya gelmek", "pos": "fiil", "level": "B1"},
    "meeting": {"tr": "toplantı", "pos": "isim", "level": "B1"},
    "goal": {"tr": "hedef, amaç", "pos": "isim", "level": "B1"},
    "colleague": {"tr": "iş arkadaşı", "pos": "isim", "level": "B1"},
    "agenda": {"tr": "gündem", "pos": "isim", "level": "B1"},
    "courage": {"tr": "cesaret", "pos": "isim", "level": "B1"},
    "cooperation": {"tr": "işbirliği", "pos": "isim", "level": "B1"},
    "assignment": {"tr": "görev, ödev", "pos": "isim", "level": "B1"},
    "email": {"tr": "e-posta", "pos": "isim", "level": "B1"},
    "draft": {"tr": "taslak", "pos": "isim", "level": "B1"},
    "subject": {"tr": "konu başlığı", "pos": "isim", "level": "B1"},
    "attachment": {"tr": "dosya eki", "pos": "isim", "level": "B1"},
    "send": {"tr": "göndermek", "pos": "fiil", "level": "B1"},
    "recipient": {"tr": "alıcı", "pos": "isim", "level": "B1"},
    "polite": {"tr": "kibar, nazik", "pos": "sıfat", "level": "B1"},
    "reply": {"tr": "yanıt vermek", "pos": "fiil", "level": "B1"},
    "break": {"tr": "mola, ara", "pos": "isim", "level": "B1"},
    "coffee machine": {"tr": "kahve makinesi", "pos": "isim", "level": "B1"},
    "kitchen": {"tr": "mutfak", "pos": "isim", "level": "B1"},
    "chat": {"tr": "sohbet etmek", "pos": "fiil", "level": "B1"},
    "friendly": {"tr": "samimi, dostça", "pos": "sıfat", "level": "B1"},
    "relax": {"tr": "rahatlamak", "pos": "fiil", "level": "B1"},
    "advice": {"tr": "tavsiye, öğüt", "pos": "isim", "level": "B1"},
    "casual": {"tr": "rahat, resmi olmayan", "pos": "sıfat", "level": "B1"},
    "printer": {"tr": "yazıcı", "pos": "isim", "level": "B1"},
    "paper jam": {"tr": "kağıt sıkışması", "pos": "isim", "level": "B1"},
    "technician": {"tr": "teknisyen", "pos": "isim", "level": "B1"},
    "toner": {"tr": "toner, mürekkep kartuşu", "pos": "isim", "level": "B1"},
    "copy": {"tr": "fotokopi çekmek, kopyalamak", "pos": "fiil", "level": "B1"},
    "replace": {"tr": "değiştirmek, yenisini koymak", "pos": "fiil", "level": "B1"},
    "solve": {"tr": "çözmek", "pos": "fiil", "level": "B1"},
    "folder": {"tr": "klasör, dosya", "pos": "isim", "level": "B1"},
    "archive": {"tr": "arşiv", "pos": "isim", "level": "B1"},
    "document": {"tr": "belge, doküman", "pos": "isim", "level": "B1"},
    "cabinet": {"tr": "dolap", "pos": "isim", "level": "B1"},
    "organize": {"tr": "düzenlemek", "pos": "fiil", "level": "B1"},
    "alphabet": {"tr": "alfabe", "pos": "isim", "level": "B1"},
    "record": {"tr": "kayıt, tutanak", "pos": "isim", "level": "B1"},
    "drawer": {"tr": "çekmece", "pos": "isim", "level": "B1"},
    "calendar": {"tr": "takvim", "pos": "isim", "level": "B1"},
    "appointment": {"tr": "randevu", "pos": "isim", "level": "B1"},
    "reminder": {"tr": "hatırlatıcı", "pos": "isim", "level": "B1"},
    "deadline": {"tr": "son teslim tarihi", "pos": "isim", "level": "B1"},
    "postpone": {"tr": "ertelemek", "pos": "fiil", "level": "B1"},
    "prioritize": {"tr": "önceliklendirmek", "pos": "fiil", "level": "B1"},
    "confirm": {"tr": "onaylamak", "pos": "fiil", "level": "B1"},
    "busy": {"tr": "meşgul, yoğun", "pos": "sıfat", "level": "B1"},
    "phone": {"tr": "telefon", "pos": "isim", "level": "B1"},
    "client": {"tr": "müşteri, danışan", "pos": "isim", "level": "B1"},
    "inquiry": {"tr": "soru, danışma", "pos": "isim", "level": "B1"},
    "message": {"tr": "mesaj", "pos": "isim", "level": "B1"},
    "transfer": {"tr": "aktarmak, bağlamak", "pos": "fiil", "level": "B1"},
    "answer": {"tr": "yanıtlamak", "pos": "fiil", "level": "B1"},
    "resolve": {"tr": "çözüme kavuşturmak", "pos": "fiil", "level": "B1"},
    "stationery": {"tr": "kırtasiye malzemeleri", "pos": "isim", "level": "B1"},
    "supplies": {"tr": "malzemeler, gereçler", "pos": "isim", "level": "B1"},
    "order": {"tr": "sipariş vermek", "pos": "fiil", "level": "B1"},
    "scissors": {"tr": "makas", "pos": "isim", "level": "B1"},
    "staples": {"tr": "zımba telleri", "pos": "isim", "level": "B1"},
    "delivery": {"tr": "teslimat", "pos": "isim", "level": "B1"},
    "invoice": {"tr": "fatura", "pos": "isim", "level": "B1"},
}

def infer_pos(word, tr):
    tr_clean = tr.strip().lower()
    if tr_clean.endswith("mek") or tr_clean.endswith("mak"):
        return "fiil"
    w_clean = word.strip().lower()
    if w_clean.endswith("ly"):
        return "zarf"
    if any(w_clean.endswith(sfx) for sfx in ["al", "ic", "ous", "ive", "able", "ible", "ant", "ent", "ful", "less"]):
        return "sıfat"
    if any(w_clean.endswith(sfx) for sfx in ["tion", "sion", "ment", "ity", "ism", "ance", "ence", "or", "er", "ness", "gy", "phy", "my"]):
        return "isim"
    return "isim"

def lookup_vocab(word, tr_fallback=""):
    """Returns a dictionary with word, tr meaning, pos, and cefr level."""
    clean_word = word.strip().lower()
    if clean_word in VOCAB_DB:
        info = VOCAB_DB[clean_word]
        return {
            "word": word.strip(),
            "tr": info["tr"],
            "pos": info["pos"],
            "level": info.get("level", "B1")
        }
    
    pos = infer_pos(word, tr_fallback)
    return {
        "word": word.strip(),
        "tr": tr_fallback.strip() or "kavram",
        "pos": pos,
        "level": "Akademik"
    }
