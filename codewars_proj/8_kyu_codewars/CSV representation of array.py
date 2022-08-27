def to_csv_text(array):
    final = ""
    for y in array:
        if len(final)>1:
            final += "\n"
        final += ",".join(str(x) for x in y)
    return final