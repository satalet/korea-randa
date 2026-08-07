import json

# بنك الكلمات المعتمد (مقسم مجموعات 15 كلمة)
dictionary_data = [
    # --- الدفعة 1 (Batch 1) ---
    {"hangul": "안녕하세요", "roman": "Annyeong-haseyo", "arabic": "مرحباً / السلام عليكم"},
    {"hangul": "감사합니다", "roman": "Gamsa-hamnida", "arabic": "شكراً لك"},
    {"hangul": "네", "roman": "Ne", "arabic": "نعم"},
    {"hangul": "아니요", "roman": "Aniyo", "arabic": "لا"},
    {"hangul": "사랑해요", "roman": "Sarang-haeyo", "arabic": "أحبك"},
    {"hangul": "죄송합니다", "roman": "Joesong-hamnida", "arabic": "آسف"},
    {"hangul": "괜찮아요", "roman": "Gwaenchana-yo", "arabic": "لا بأس / أنا بخير"},
    {"hangul": "주세요", "roman": "Juseyo", "arabic": "أعطني من فضلك"},
    {"hangul": "얼마예요?", "roman": "Eolmayeyo?", "arabic": "كم السعر؟"},
    {"hangul": "어디예요?", "roman": "Eodiyeyo?", "arabic": "أين المكان؟"},
    {"hangul": "맛있어요", "roman": "Masisseoyo", "arabic": "لذيذ"},
    {"hangul": "도와주세요", "roman": "Dowajuseyo", "arabic": "ساعدني من فضلك"},
    {"hangul": "안녕히 가세요", "roman": "Annyeonghi gaseyo", "arabic": "مع السلامة"},
    {"hangul": "네, 맞아요", "roman": "Ne, majayo", "arabic": "نعم، هذا صحيح"},
    {"hangul": "잠시만요", "roman": "Jamsimanyo", "arabic": "لحظة من فضلك"},

    # --- الدفعة 2 (Batch 2) ---
    {"hangul": "물", "roman": "Mul", "arabic": "ماء"},
    {"hangul": "밥", "roman": "Bap", "arabic": "أرز / طعام"},
    {"hangul": "학교", "roman": "Hakgyo", "arabic": "مدرسة"},
    {"hangul": "집", "roman": "Jip", "arabic": "بيت / منزل"},
    {"hangul": "친구", "roman": "Chingu", "arabic": "صديق"},
    {"hangul": "사람", "roman": "Saram", "arabic": "شخص / إنسان"},
    {"hangul": "오늘", "roman": "Oneul", "arabic": "اليوم"},
    {"hangul": "내일", "roman": "Naeil", "arabic": "غداً"},
    {"hangul": "어제", "roman": "Eoje", "arabic": "أمس"},
    {"hangul": "시간", "roman": "Sigan", "arabic": "وقت / ساعة"},
    {"hangul": "돈", "roman": "Don", "arabic": "نقود / مصاري"},
    {"hangul": "일", "roman": "Il", "arabic": "عمل / شغل"},
    {"hangul": "한국", "roman": "Hanguk", "arabic": "كوريا"},
    {"hangul": "언어", "roman": "Eoneo", "arabic": "لغة"},
    {"hangul": "선생님", "roman": "Seonsaengnim", "arabic": "معلم / أستاذ"},

    # --- الدفعة 3 (Batch 3) ---
    {"hangul": "가다", "roman": "Gada", "arabic": "يذهب"},
    {"hangul": "오다", "roman": "Oda", "arabic": "يأتي"},
    {"hangul": "먹다", "roman": "Meokda", "arabic": "يأكل"},
    {"hangul": "마시다", "roman": "Masida", "arabic": "يشرب"},
    {"hangul": "자다", "roman": "Jada", "arabic": "ينام"},
    {"hangul": "보다", "roman": "Boda", "arabic": "يرى / يشاهد"},
    {"hangul": "듣다", "roman": "Deutda", "arabic": "يسمع"},
    {"hangul": "말하다", "roman": "Malhada", "arabic": "يتكلم"},
    {"hangul": "읽다", "roman": "Ikda", "arabic": "يقرأ"},
    {"hangul": "쓰다", "roman": "Sseuda", "arabic": "يكتب"},
    {"hangul": "좋다", "roman": "Joh-da", "arabic": "جيد / جميل"},
    {"hangul": "나쁘다", "roman": "Nappeuda", "arabic": "سيء"},
    {"hangul": "크다", "roman": "Keuda", "arabic": "كبير"},
    {"hangul": "작다", "roman": "Jakda", "arabic": "صغير"},
    {"hangul": "행복", "roman": "Haengbok", "arabic": "سعادة"}
]

# معالجة وتقسيم الكلمات لدفعات من 15 كلمة تلقائياً
formatted_words = []
batch_size = 15

for index, word in enumerate(dictionary_data):
    batch_num = (index // batch_size) + 1
    formatted_words.append({
        "id": index + 1,
        "batch": batch_num,
        "hangul": word["hangul"],
        "roman": word["roman"],
        "arabic": word["arabic"]
    })

# كتابة ملف words.json المحدث
with open("words.json", "w", encoding="utf-8") as f:
    json.dump(formatted_words, f, ensure_ascii=False, indent=2)

print(f"✅ تم توليد ملف words.json بنجاح! إجمالي الكلمات: {len(formatted_words)} مقسمة على {formatted_words[-1]['batch']} دفعات.")
