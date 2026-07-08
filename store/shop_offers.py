from urllib.parse import quote_plus

MECHTA_PRODUCTS = {
    "Samsung Galaxy A56 5G 128GB Awesome Lightgray (SM-A566) EZAAS": "https://www.mechta.kz/product/smartfon-samsung-galaxy-a56-5g-128gb-awesome-lightgray-sm-a566-ezaas/",
    "HONOR 600 Pro (12/512GB) Orange": "https://www.mechta.kz/product/smartfon-honor-600-pro-12512gb-orange/",
    "APPLE iPhone 17 Pro Max 256GB (Silver)": "https://www.mechta.kz/product/smartfon-apple-iphone-17-pro-max-256gb-silver/",
    "Apple iPhone 16 128GB (Pink)": "https://www.mechta.kz/product/smartfon-apple-iphone-16-128gb-pink/",
    "APPLE iPhone 17 Pro 256GB (Silver)": "https://www.mechta.kz/product/smartfon-apple-iphone-17-pro-256gb-silver/",
    "HONOR 600 (8/256GB) Orange": "https://www.mechta.kz/product/smartfon-honor-600-8256gb-orange/",
    "Apple iPhone 15 128GB (Pink)": "https://www.mechta.kz/product/smartfon-apple-iphone-15-128gb-pink/",
    "APPLE iPhone 17 Pro Max 2TB (Cosmic Orange)": "https://www.mechta.kz/product/smartfon-apple-iphone-17-pro-max-2tb-cosmic-orange/",
    "Apple iPhone 15 128GB (Black)": "https://www.mechta.kz/product/smartfon-apple-iphone-15-128gb-black/",
    "Xiaomi Redmi Note 13 Pro+ 5G 12/512GB Midnight Black": "https://www.mechta.kz/product/smartfon-xiaomi-redmi-note-13-proplus-5g-12512gb-midnight-black/",
    "Samsung Galaxy A26 5G 256GB White (SM-A266) BZWHS": "https://www.mechta.kz/product/smartfon-samsung-galaxy-a26-5g-256gb-white-sm-a266-bzwhs/",
    "OPPO A6 (8/256) Aurora Gold": "https://www.mechta.kz/product/smartfon-oppo-a6-8256-aurora-gold/",
}

MODEL_SEARCH_NAMES = {
    "Samsung Galaxy A56 5G 128GB Awesome Lightgray (SM-A566) EZAAS": "Samsung Galaxy A56",
    "HONOR 600 Pro (12/512GB) Orange": "Honor 600 Pro",
    "APPLE iPhone 17 Pro Max 256GB (Silver)": "iPhone 17 Pro Max",
    "Apple iPhone 16 128GB (Pink)": "iPhone 16",
    "APPLE iPhone 17 Pro 256GB (Silver)": "iPhone 17 Pro",
    "HONOR 600 (8/256GB) Orange": "Honor 600",
    "Apple iPhone 15 128GB (Pink)": "iPhone 15",
    "APPLE iPhone 17 Pro Max 2TB (Cosmic Orange)": "iPhone 17 Pro Max",
    "Apple iPhone 15 128GB (Black)": "iPhone 15",
    "Xiaomi Redmi Note 13 Pro+ 5G 12/512GB Midnight Black": "Redmi Note 13 Pro+",
    "Samsung Galaxy A26 5G 256GB White (SM-A266) BZWHS": "Samsung Galaxy A26",
    "OPPO A6 (8/256) Aurora Gold": "OPPO A6",
}

TECHNODOM_OFFERS = {
    "Samsung Galaxy A56 5G 128GB Awesome Lightgray (SM-A566) EZAAS": {
        "url": "https://www.technodom.kz/p/smartfon-samsung-galaxy-a56-128-awesome-lightgray-sm-a566ezaaskz-289302?recommended_by=instant_search&source=suggest&suggest_item_index=0&recommended_code=Samsung+Galaxy+A56+Lightgray",
        "price": "219 890 ₸",
        "note": "точная карточка товара",
    },
    "HONOR 600 Pro (12/512GB) Orange": {
        "url": "https://www.technodom.kz/p/smartfon-gsm-honor-600-pro-12-512gb-oranzheviy-298795?recommended_by=instant_search&source=suggest&suggest_item_index=0&recommended_code=Honor+600+Pro",
        "price": "549 990 ₸",
        "note": "точная карточка товара",
    },
    "APPLE iPhone 17 Pro Max 256GB (Silver)": {
        "url": "https://www.technodom.kz/p/smartfon-gsm-apple-iphone-17-pro-max-12-256gb-6-9-48-silver-293876?recommended_by=instant_search&source=suggest&suggest_item_index=0&recommended_code=iPhone+17+Pro+Max",
        "price": "898 990 ₸",
        "note": "точная карточка товара",
    },
    "Apple iPhone 16 128GB (Pink)": {
        "url": "https://www.technodom.kz/p/smartfon-apple-iphone-16-128gb-pink-284605?recommended_by=instant_search&source=suggest&suggest_item_index=2&recommended_code=iPhone+16",
        "price": "515 990 ₸",
        "note": "точная карточка товара",
    },
    "APPLE iPhone 17 Pro 256GB (Silver)": {
        "url": "https://www.technodom.kz/p/smartfon-apple-iphone-17-pro-12256gb6348-silver-293867?recommended_by=instant_search&source=suggest&suggest_item_index=0&recommended_code=iPhone+17+Pro",
        "price": "836 990 ₸",
        "note": "точная карточка товара",
    },
    "HONOR 600 (8/256GB) Orange": {
        "url": "https://www.technodom.kz/p/smartfon-honor-600-8256gb-oranzhevyj-298801?recommended_by=instant_search&source=suggest&suggest_item_index=1&recommended_code=Honor+600",
        "price": "329 990 ₸",
        "note": "точная карточка товара",
    },
    "Apple iPhone 15 128GB (Pink)": {
        "url": "https://www.technodom.kz/p/smartfon-apple-iphone-15-128gb-blue-mtp43-274375?recommended_by=instant_search&source=suggest&suggest_item_index=0&recommended_code=iPhone+15+128+Pink",
        "price": "443 990 ₸",
        "note": "та же модель и память, другой цвет",
    },
    "APPLE iPhone 17 Pro Max 2TB (Cosmic Orange)": {
        "url": "https://www.technodom.kz/p/smartfon-gsm-apple-iphone-17-pro-max-12-2tb-6-9-48-cosmic-orange-293886?recommended_by=instant_search&source=suggest&suggest_item_index=4&recommended_code=iPhone+17+Pro+Max",
        "price": "1 522 990 ₸",
        "note": "точная карточка товара",
    },
    "Apple iPhone 15 128GB (Black)": {
        "url": "https://www.technodom.kz/p/smartfon-apple-iphone-15-128gb-black-mtp03-274372?recommended_by=instant_search&source=suggest&suggest_item_index=2&recommended_code=iPhone+15",
        "price": "443 990 ₸",
        "note": "точная карточка товара",
    },
    "Samsung Galaxy A26 5G 256GB White (SM-A266) BZWHS": {
        "url": "https://www.technodom.kz/p/smartfon-gsm-samsung-galaxy-a26-8-256-6-7-50-white-sm-a266bzwhskz-289291?recommended_by=instant_search&source=suggest&suggest_item_index=2&recommended_code=Samsung+Galaxy+A26",
        "price": "149 890 ₸",
        "note": "точная карточка товара",
    },
    "OPPO A6 (8/256) Aurora Gold": {
        "url": "https://www.technodom.kz/p/smartfon-gsm-oppo-a6-8256gb67550-shampan-297138?recommended_by=instant_search&source=suggest&suggest_item_index=1&recommended_code=OPPO+A6",
        "price": "164 990 ₸",
        "note": "та же модель, близкий цвет",
    },
}

SULPAK_OFFERS = {
    "Samsung Galaxy A56 5G 128GB Awesome Lightgray (SM-A566) EZAAS": {
        "url": "https://www.sulpak.kz/g/smartfoniy-samsung-galaxy-a56-5g-128gb-lightgray-sm-a566ezaaskz",
        "price": "189 890 ₸",
        "note": "точная карточка товара",
    },
    "HONOR 600 Pro (12/512GB) Orange": {
        "url": "https://www.sulpak.kz/g/smartfoniy-honor-600-pro-12512gb-orange",
        "price": "549 990 ₸",
        "note": "точная карточка товара",
    },
    "APPLE iPhone 17 Pro Max 256GB (Silver)": {
        "url": "https://www.sulpak.kz/g/smartfoniy-apple-iphone-17-pro-max-256gb-silver-mfym4hxa",
        "price": "898 990 ₸",
        "note": "точная карточка товара",
    },
    "Apple iPhone 16 128GB (Pink)": {
        "url": "https://www.sulpak.kz/g/smartfoniy-apple-iphone-16-128gb-pink-myea3hxa",
        "price": "515 990 ₸",
        "note": "точная карточка товара",
    },
    "APPLE iPhone 17 Pro 256GB (Silver)": {
        "url": "https://www.sulpak.kz/g/smartfoniy-apple-iphone-17-pro-256gb-silver-mg8g4hxa",
        "price": "836 990 ₸",
        "note": "точная карточка товара",
    },
    "HONOR 600 (8/256GB) Orange": {
        "url": "https://www.sulpak.kz/g/smartfoniy-honor-600-8256gb-orange",
        "price": "329 990 ₸",
        "note": "точная карточка товара",
    },
    "Apple iPhone 15 128GB (Pink)": {
        "url": "https://www.sulpak.kz/g/smartfoniy_apple_15_128gb_black",
        "price": "443 990 ₸",
        "note": "та же модель и память, другой цвет",
    },
    "APPLE iPhone 17 Pro Max 2TB (Cosmic Orange)": {
        "url": "https://www.sulpak.kz/g/smartfoniy-apple-iphone-17-pro-max-2tb-cosmic-orange-mg004hxa",
        "price": "1 522 990 ₸",
        "note": "точная карточка товара",
    },
    "Apple iPhone 15 128GB (Black)": {
        "url": "https://www.sulpak.kz/g/smartfoniy_apple_15_128gb_black",
        "price": "443 990 ₸",
        "note": "точная карточка товара",
    },
    "Xiaomi Redmi Note 13 Pro+ 5G 12/512GB Midnight Black": {
        "url": "https://www.sulpak.kz/g/smartfoniy_xiaomi_redmi__note_13_pro__5g_12512_moonlight_white",
        "price": "189 990 ₸",
        "note": "та же модель и память, другой цвет",
    },
    "Samsung Galaxy A26 5G 256GB White (SM-A266) BZWHS": {
        "url": "https://www.sulpak.kz/g/smartfoniy-samsung-galaxy-a26-5g-256gb-white-sm-a266bzwhskz",
        "price": "149 890 ₸",
        "note": "точная карточка товара",
    },
    "OPPO A6 (8/256) Aurora Gold": {
        "url": "https://www.sulpak.kz/g/smartfoniy-oppo-a6-8256gb-aurora-gold",
        "price": "164 890 ₸",
        "note": "точная карточка товара",
    },
}

def _search_text(phone):
    return MODEL_SEARCH_NAMES.get(phone.name, phone.name)

def get_shop_offers(phone):
    model_name = _search_text(phone)
    query = quote_plus(model_name)
    price = f"{int(phone.price):,} ₸".replace(",", " ")
    technodom = TECHNODOM_OFFERS.get(phone.name)
    sulpak = SULPAK_OFFERS.get(phone.name)

    mechta_url = phone.shop_mechta_url or MECHTA_PRODUCTS.get(phone.name, f"https://www.mechta.kz/search/?q={query}")
    technodom_url = phone.shop_technodom_url or (technodom["url"] if technodom else "https://www.technodom.kz/catalog/smartfony-i-gadzhety/smartfony-i-telefony/smartfony")
    sulpak_url = phone.shop_sulpak_url or (sulpak["url"] if sulpak else "https://www.sulpak.kz/f/smartfoniy/")

    return [
        {
            "store": "Mechta",
            "price": price,
            "url": mechta_url,
            "note": "точная карточка товара" if phone.shop_mechta_url else ("" if MECHTA_PRODUCTS.get(phone.name) else f"откройте каталог и ищите: {model_name}"),
        },
        {
            "store": "Technodom",
            "price": technodom["price"] if technodom else "карточка не найдена",
            "url": technodom_url,
            "note": technodom["note"] if technodom else ("" if not phone.shop_technodom_url else ""),
        },
        {
            "store": "Sulpak",
            "price": sulpak["price"] if sulpak else "карточка не найдена",
            "url": sulpak_url,
            "note": sulpak["note"] if sulpak else ("" if not phone.shop_sulpak_url else ""),
        },
    ]
