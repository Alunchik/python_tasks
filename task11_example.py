import struct


def main(binary_data):
    signature = b'\x4c\x59\x4b'

    if binary_data[:len(signature)] != signature:
        raise ValueError("Invalid signature")

    struct_a = ">" + "7sIHH"
    struct_c = ">" + "Id qfh4Q I"
    struct_d = ">" + "IbQbHHBh"
    struct_f = ">" + "HII"

    a = struct.unpack_from(struct_a, binary_data, len(signature))

    d = struct.unpack_from(struct_c, binary_data, a[-1])

    e = struct.unpack_from(struct_f, binary_data, d[-1])

    arrayF = ">" + "b" * e[0]
    f = struct.unpack_from(arrayF, binary_data, e[1])

    g = struct.unpack_from(struct_d, binary_data, d[0])

    arrayD = ">" + "b" * g[4]
    h = struct.unpack_from(arrayD, binary_data, g[5])

    struct_data = {'A1': a[0].decode(),
                   'A2': [],
                   'A3': {'C1': {'D1': g[0],
                                 'D2': g[1],
                                 'D3': g[2],
                                 'D4': g[3],
                                 'D5': list(h),
                                 'D6': g[6],
                                 'D7': g[7]},
                          'C2': d[1],
                          'C3': {'E1': d[2],
                                 'E2': d[3],
                                 'E3': d[4],
                                 'E4': [d[5],
                                        d[6],
                                        d[7],
                                        d[8]]},
                          'C4': {'F1': list(f), 'F2': e[-1]}}}

    arrayAB = ">" + "I" * a[1]
    b = struct.unpack_from(arrayAB, binary_data, a[2])
    for i in range(a[1]):
        struct_b = ">" + "qI"
        c = struct.unpack_from(struct_b, binary_data, b[i])
        bi = {'B1': c[0], 'B2': c[1]}
        struct_data["A2"].append(bi)

    return struct_data