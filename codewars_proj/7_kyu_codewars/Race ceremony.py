def race_podium(blocks):
    if blocks%3==0:
        return (blocks/3,blocks/3+1,blocks/3-1)
    elif blocks%3==1:
        return ((blocks+2)/3,(blocks+2)/3+1,(blocks+2)/3-3) if (blocks+2)/3-3 != 0 else ((blocks+2)/3-1,(blocks+2)/3+1,(blocks+2)/3-2)
    elif blocks%3==2:
        return ((blocks+1)/3,(blocks+1)/3+1,(blocks+1)/3-2)
    