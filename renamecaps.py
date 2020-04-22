file = "renamecaps.bat"
fhand = open(file, "w")

common = "convert -background none -fill white -font Handwriting-Regular.ttf -pointsize 300 label:"

for i in range(ord('A'),ord('Z')+1):
    fhand.write(common)
    fhand.write('"')
    fhand.write(chr(i))
    fhand.write('" ')
    fhand.write(chr(i))
    fhand.write(".png")
    fhand.write("\n")
fhand.close()
