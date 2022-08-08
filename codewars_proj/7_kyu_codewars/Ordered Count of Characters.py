def ordered_count(inp):
    return [(z, inp.count(z)) for z in sorted(set(inp), key=inp.index)]