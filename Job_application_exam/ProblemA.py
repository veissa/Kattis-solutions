"""
Problem A

You have been placed in charge of your company’s archive of digital data, and your first job is to convert a lot of old pictures into a newer format. But you have no software to read the old images, so you need to write it.

You do have a description of the old image format. The old images are 1-bit images (each pixel is either on or off) and are in a simple compressed format. The compression is a form of run-length encoding, which is popular because it runs efficiently on older hardware.

For each encoded image, produce a rendered version so that you can visually inspect it. You should also detect errors in the original encoded image, if there are any.
Input

Input consists of a sequence of up to
images. Each image starts with a line containing an integer indicating the number of scanlines in the image. The following lines each contain one scanline. Each scanline starts with either ‘.’ or ‘#’, indicating the value of the first pixel on the scanline. Following this are up to integers each in the range indicating the lengths of each subsequent run of pixels. Each scanline has at most total pixels (the sum of the integers on the line). Each run uses only one pixel value, which alternates between ‘.’ and ‘#’ with each run. Input ends with a line containing just the number

.
Output

For each image, decode and output image according to run-length encoding. In other words, for each scanline, expand each run of pixels of length
into

copies of that pixel value.

Some images may not have the same number of pixels output for all decoded scanlines. This is an error condition, which your program should identify by producing a line after the image with the text ‘Error decoding image’.

Separate adjacent images with a blank line.

Sample input : 
12
# 8 2 4 4 3
. 1 2 4 2 2 2 6 1 1
. 1 2 5 2 1 2 6 1 1
. 1 2 5 1 2 2 6 1 1
. 1 2 4 2 2 2 6 1 1
. 1 7 3 2 6 1 1
. 1 2 4 2 2 2 6 1 1
. 1 2 5 2 1 2 6 1 1
. 1 2 5 2 2 2 5 1 1
. 1 2 5 2 2 2 4 2 1
. 1 2 4 2 4 2 3 1 2
# 7 8 2 4
35
. 11 7 12
. 10 10 10
. 10 10 10
. 9 12 9
. 9 12 9
. 9 12 9
. 9 12 9
. 9 12 9
. 9 4 1 7 9
. 9 2 5 5 9
. 10 12 8
. 10 12 8
. 9 7 2 5 7
. 8 3 1 3 3 6 6
. 7 3 9 5 7
. 7 3 9 6 5
. 6 4 9 7 4
. 6 4 10 6 4
. 5 4 11 7 3
. 5 4 12 6 3
. 4 4 13 6 3
. 4 4 13 6 3
. 4 4 13 6 3
. 4 4 13 6 3
. 4 4 12 7 3
. 3 1 2 3 11 8 2
# 4 3 4 9 8 2
# 4 4 4 8 1 5 2 2
# 2 6 4 7 2 6 3
# 2 7 3 6 3 7 2
# 2 8 3 3 5 7 2
# 1 9 11 5 4
# 4 6 11 3 4 2
. 1 25 4
. 5 6 8 6 5
0

Sample Output :
########..####....###
.##....##..##......#.
.##.....##.##......#.
.##.....#..##......#.
.##....##..##......#.
.#######...##......#.
.##....##..##......#.
.##.....##.##......#.
.##.....##..##.....#.
.##.....##..##....##.
.##....##....##...#..
#######........##....

...........#######............
..........##########..........
..........##########..........
.........############.........
.........############.........
.........############.........
.........############.........
.........############.........
.........####.#######.........
.........##.....#####.........
..........############........
..........############........
.........#######..#####.......
........###.###...######......
.......###.........#####.......
.......###.........######.....
......####.........#######....
......####..........######....
.....####...........#######...
.....####............######...
....####.............######...
....####.............######...
....####.............######...
....####.............######...
....####............#######...
...#..###...........########..
####...####.........########..
####....####........#.....##..
##......####.......##......###
##.......###......###.......##
##........###...#####.......##
#.........###########.....####
####......###########...####..
.#########################....
.....######........######.....
Error decoding image

"""


def decomp(txt):
    new = txt.split()
    hashtag = "#"
    period = "."
    if new[0] != hashtag:
        hashtag, period = period, hashtag
    
    i = 1
    flag = ""
    length = len(new)
    
    while i < length - 1:
        flag += int(new[i]) * hashtag
        flag += int(new[i + 1]) * period
        i += 2
    
    if length % 2 == 0:
        flag += int(new[length - 1]) * hashtag
    
    return flag

def process_image(image_lines):
    decoded_lines = [decomp(line) for line in image_lines]
    
    lengths = [len(line) for line in decoded_lines]
    if len(set(lengths)) != 1:
        return decoded_lines, True  
    return decoded_lines, False  

image_numbers = []
frames_list = []

while True:
    try:
        image_count = int(input().strip())
    except EOFError:
        break
    if image_count == 0:
        break
    
    image_numbers.append(image_count)
    frames = []
    for _ in range(image_count):
        frames.append(str(input().strip()))
    frames_list.append(frames)

first_image = True
for idx, image_count in enumerate(image_numbers):
    if not first_image:
        print() 
    first_image = False
    
    frames = frames_list[idx]
    decoded_lines, has_error = process_image(frames)
    
    for line in decoded_lines:
        print(line)
    
    if has_error:
        print("Error decoding image")
