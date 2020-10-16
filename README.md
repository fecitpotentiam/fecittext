# Text normalization tool (supports russian language)

##Using
    text = 'Пример текста для нормализации. Пример текста для нормализации'
    text_normalizer = TextNormalizer()
    result = text_normalizer.normalize_text(
        text=texts, 
        split_words=True, 
        split_sentences=True, 
        stop_words_ignore=True, 
        split_docs=False
    )
