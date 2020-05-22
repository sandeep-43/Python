def shopping(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg, end=" ")
        print("\n","-" * 40)
        keys = sorted(keywords.keys())
        print("KEYS ->",keywords)
    for kw in keys:
        print(kw, ":", keywords[kw])

shopping("umberlla", "It's very runny, sir.", "It's really very", "VERY runny, sir.", shopkeeper="Tom Kennedy", client="John Right", sketch="Variety Shop Sketch")
