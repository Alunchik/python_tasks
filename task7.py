def main(x):
    # return hex((x & 245760) >> 14), hex((x & 8192) >> 13), \
    #        hex((x & 6144) >> 11), hex((x & 1792) >> 8), \
    #        hex((x & 254) >> 1), hex(x & 1)
    return hex(x & 1), hex((x & 254) >> 1), \
           hex((x & 1792) >> 8), hex((x & 6144) >> 11), \
           hex((x & 8192) >> 13), hex((x & 245760) >> 14)
