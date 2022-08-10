def int32_to_ip(int32):
    int32=str(bin(int32))[2:].zfill(32)
    return f"{int(int32[-32:-24],2)}.{int(int32[-24:-16],2)}.{int(int32[-16:-8],2)}.{int(int32[-8:],2)}"