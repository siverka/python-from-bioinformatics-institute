def gc_content(gen):
    gen_lower = gen.lower()
    return 100 * (gen_lower.count('c') + gen_lower.count('g'))/len(gen_lower)

print(gc_content('acggtgttat'))

