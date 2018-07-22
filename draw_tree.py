import simple_draw as sd
sd.resolution = (1200, 800)

def tree(vector):
    if vector.length < 5:
        sd.circle(vector.end_point, radius=10, color=sd.COLOR_GREEN, width=0)
        return
    vector.draw(color=sd.COLOR_DARK_ORANGE)
    length=vector.length/1.5
    width=round(vector.width/1.3)
    vector_1 = sd.get_vector(vector.end_point, angle=vector.angle-30, length=length, width=width)
    vector_2 = sd.get_vector(vector.end_point, angle=vector.angle+30, length=length, width=width)
    tree(vector_1)
    tree(vector_2)


vector_1 = sd.get_vector(sd.get_point(600, 0), angle=90, length=200, width=20)
tree(vector=vector_1)

sd.pause()
