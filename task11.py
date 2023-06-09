import struct


def main(binary_data):
    signature = b'\x49\x55\x56\x50'

    if binary_data[:len(signature)] != signature:
        raise ValueError("Invalid signature")

    struct_a = ">" + "Id"
    struct_b = ">" + "HII"
    struct_c = ">" + "4IdbHHq"
    struct_d = ">" + "HHBfBii"
    struct_e = ">" + "IbIH"

    a = struct.unpack_from(struct_a, binary_data, len(signature))

    b = struct.unpack_from(struct_b, binary_data, a[0])

    c = struct.unpack_from(struct_c, binary_data, b[0])

    arrayB = struct.unpack_from(">" + "I" * b[1], binary_data, b[2])

    d_list = []
    for i in range(4):  # массим структур D в структуре C
        d_list.append(struct.unpack_from(struct_d, binary_data, c[i]))

    e = struct.unpack_from(struct_e, binary_data, c[-3])

    arrayE = struct.unpack_from(">" + "H" * e[2], binary_data, e[3])

    d_format = []
    for j in range(4):
        arrayD = struct.unpack_from(">" + 'b' * d_list[j][0],
                                    binary_data, d_list[j][1])
        d_dict = {'D1': list(arrayD),
                  'D2': d_list[j][2],
                  'D3': d_list[j][3],
                  'D4': d_list[j][4],
                  'D5': d_list[j][5],
                  'D6': d_list[j][6],
                  }
        d_format.append(d_dict)

    struct_data = {'A1': {
        'B1': {
            'C1': d_format,
            'C2': c[4],
            'C3': c[5],
            'C4': {
                'E1': e[0],
                'E2': e[1],
                'E3': list(arrayE),
            },
            'C5': c[7],
            'C6': c[8],
        },
        'B2': list(arrayB),
    },
        'A2': a[1]
    }

    return struct_data
