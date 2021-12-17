from functools import reduce


simple_sum = "C200B40A82"
simple_product = "04005AC33890"
simple_min = "880086C3E88112"
simple_max = "CE00C43D881120"
puzzle_input = "A20D5080210CE4BB9BAFB001BD14A4574C014C004AE46A9B2E27297EECF0C013F00564776D7E3A825CAB8CD47B6C537DB99CD746674C1000D29BBC5AC80442966FB004C401F8771B61D8803D0B22E4682010EE7E59ACE5BC086003E3270AE4024E15C8010073B2FAD98E004333F9957BCB602E7024C01197AD452C01295CE2DC9934928B005DD258A6637F534CB3D89A944230043801A596B234B7E58509E88798029600BCF5B3BA114F5B3BA10C9E77BAF20FA4016FCDD13340118B929DD4FD54E60327C00BEB7002080AA850031400D002369400B10034400F30021400F20157D804AD400FE00034E000A6D001EB2004E5C00B9AE3AC3C300470029091ACADBFA048D656DFD126792187008635CD736B3231A51BA5EBDF42D4D299804F26B33C872E213C840022EC9C21FFB34EDE7C559C8964B43F8AD77570200FC66697AFEB6C757AC0179AB641E6AD9022006065CEA714A4D24C0179F8E795D3078026200FC118EB1B40010A8D11EA27100990200C45A83F12C401A8611D60A0803B1723542889537EFB24D6E0844004248B1980292D608D00423F49F9908049798B4452C0131006230C14868200FC668B50650043196A7F95569CF6B663341535DCFE919C464400A96DCE1C6B96D5EEFE60096006A400087C1E8610A4401887D1863AC99F9802DC00D34B5BCD72D6F36CB6E7D95EBC600013A88010A8271B6281803B12E124633006A2AC3A8AC600BCD07C9851008712DEAE83A802929DC51EE5EF5AE61BCD0648028596129C3B98129E5A9A329ADD62CCE0164DDF2F9343135CCE2137094A620E53FACF37299F0007392A0B2A7F0BA5F61B3349F3DFAEDE8C01797BD3F8BC48740140004322246A8A2200CC678651AA46F09AEB80191940029A9A9546E79764F7C9D608EA0174B63F815922999A84CE7F95C954D7FD9E0890047D2DC13B0042488259F4C0159922B0046565833828A00ACCD63D189D4983E800AFC955F211C700"

tx: list = list(puzzle_input)
bits: str = None
bit_index: int = 0


def read_bits(bit_count: int) -> str:
    global tx, bits, bit_index
    
    while bits is None or bit_count > len(bits):
        new_word = bin(int(tx.pop(0), base = 16)).removeprefix("0b").zfill(4)
        if bits is None:
            bits = new_word
        else:
            bits += new_word

    bit_index += bit_count
    return_this = bits[:bit_count]
    bits = bits[bit_count:]
    return return_this


def read_number(bit_count: int) -> int:
    return int(read_bits(bit_count), base = 2)


def read_literal() -> int:
    number_so_far = ""
    while True:
        quint = read_bits(5)
        number_so_far += quint[1:]
        if quint[0] == "0":
            return int(number_so_far, base = 2)


def read_packet() -> int:
    global version_sum

    packet_version = read_number(3)
    packet_type = read_number(3)

    if packet_type == 4:
        return read_literal()
    
    length_type = read_number(1)
    subpackets = []
    
    if length_type == 0:
        bit_length = read_number(15)
        before = bit_index
        while bit_index < before + bit_length:
            subpackets.append(read_packet())
    elif length_type == 1:
        subpacket_count = read_number(11)
        for _ in range(subpacket_count):
            subpackets.append(read_packet())

    if packet_type == 0:
        return sum(subpackets)
    elif packet_type == 1:
        return reduce(lambda a, b: a * b, subpackets, 1)
    elif packet_type == 2:
        return min(subpackets)
    elif packet_type == 3:
        return max(subpackets)
    elif packet_type == 5:
        assert(len(subpackets) == 2)
        return 1 if subpackets[0] > subpackets[1] else 0
    elif packet_type == 6:
        assert(len(subpackets) == 2)
        return 1 if subpackets[0] < subpackets[1] else 0
    elif packet_type == 7:
        assert(len(subpackets) == 2)
        return 1 if subpackets[0] == subpackets[1] else 0

    assert(False)


print(read_packet())
