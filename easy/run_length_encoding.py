def getNextEncoding(string, index):
    char = string[index]
    count = 1
    for i in range(index + 1, len(string)):
        if string[i] == char:
            count += 1
        else:
            break
    if count < 10:
        format_start = ''
        format_end = '{}{}'.format(count, char)
    else:
        format_start = '9{}'.format(char) * (count // 9)
        format_end = '{}{}'.format(count % 9, char)
    return format_start + format_end, index + count

def runLengthEncoding(string):
    index = 0
    formats = []
    while True:
        if index == len(string):
            break
        format, index = getNextEncoding(string, index)
        formats.append(format)
    return ''.join(formats)
        
    