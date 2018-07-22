import simple_draw as sd
sd.resolution = (1200,800)

sd.circle(sd.get_point(600,400), radius=100, width=20)
sd.circle(sd.get_point(630,440), radius=10, width=5)
sd.circle(sd.get_point(570,440), radius=10, width=5)

vector_1 = sd.get_vector(sd.get_point(570,340+20), angle=0, length=60, width=5)
vector_2 = sd.get_vector(sd.get_point(550,360+20), angle=0, length=100, width=5)
sd.line(vector_1.start_point, vector_2.start_point, width=5, color = sd.COLOR_RED)
sd.line(vector_1.end_point, vector_2.end_point, width=5, color = sd.COLOR_RED)
vector_1.draw(color = sd.COLOR_RED)
vector_2.draw(color = sd.COLOR_RED)

sd.pause()
