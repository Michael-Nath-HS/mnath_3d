inpt = open("new_script", "a")
def create_body(file, cx, cy, cz, r):
    file.write("circle\n")
    file.write(f"{cx} {cy} {cz} {r}\n")
    file.write("ident\nscale\n1 2 1\napply\n")
    file.write("sphere\n")
    file.write(f"{cx - (r / 2)} {cy + (4 * r)} {0} {r/2}\n")
    file.write("sphere\n")
    file.write(f"{cx + (r / 2)} {cy + (4 * r)} {0} {r/2}\n")

def create_wing(file, cx, cy, cz, r0, r1):
    file.write("torus\n")
    file.write(f"{0} {0} {cz} {r0} {r1}\n")
    file.write(f"ident\nrotate\nz 90\napply\n")
    file.write("torus\n")
    file.write(f"{0} {0} {cz} {r0} {r1}\n")
    file.write(f"ident\nrotate\nz 90\napply\n")
    file.write("torus\n")
    file.write(f"{0} {0} {cz} {r0} {r1}\n")
    file.write(f"ident\nrotate\nz 90\napply\n")
    file.write(f"ident\nrotate\nx 18\nrotate\ny 18\nrotate\nz 45\nmove\n250 250 0\nscale\n1 0.5 1\napply\n")
    
def create_antennae(file, x0, y0, x1, y1, rx0, ry0, rx1, ry1):
    file.write("hermite\n")
    file.write(f"{x0} {y0} {x1} {y1} {rx0} {ry0} {rx1} {ry1}\n")
    file.write("sphere\n")
    file.write(f"{x1} {y1} 0 5\n")    


inpt.write("box\n")
inpt.write("0 200 0 300 300 300\n")
inpt.write("ident\nrotate\nz -315\nrotate\nx -18\nrotate\ny -10\nmove\n-50 0 0\napply\n")
create_wing(inpt, 0, 0, 0, 10, 150)
create_body(inpt, 250, 125, 0, 50)
create_antennae(inpt, 260, 350, 324, 430, 28, 161, 126, -51)
create_antennae(inpt, 231, 350, 206, 430, 12, 140, -201, -65)

inpt.write("display\nsave\nbutterfly.png\n")
