import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
print("Sukses Import OpenGL!")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

def background():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()

    glBegin(GL_QUADS)
    # //red color
    glColor3ub(0,0,0)
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0,-1.0)
    # //blue color
    glColor3ub(0,0, 128)
    glVertex2f(1.0,-1.0)
    glVertex2f(1.0, -1.0)
    glEnd()

def tulisan():
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    #Huruf Y
    #//1
    glVertex2f(-560, 260) #titik s
    glVertex2f(-520, 260) #titik t
    glVertex2f(-460, 200) # titik r
    glVertex2f(-500, 200) #titik q

    #//2
    glVertex2f(-440, 260) #titik u
    glVertex2f(-400, 260) #titik v
    glVertex2f(-460, 200) # titik r
    glVertex2f(-500, 200) #titik q

    #//3
    glVertex2f(-460, 200) # titik r
    glVertex2f(-500, 200) #titik q
    glVertex2f(-500, 102) #titik o
    glVertex2f(-460, 102) #titik p

    # Huruf U
    #//1
    glVertex2f(-280, 240) # titik b1
    glVertex2f(-240, 240) #titik c1
    glVertex2f(-240, 160) #titik d1
    glVertex2f(-280, 160) #titik m1
    glEnd()

    #//2
    glBegin(GL_POLYGON)
    glVertex2f(-280, 160) #titik m1
    glVertex2f(-276, 139) # titik s4
    glVertex2f(-249, 108) #titik t4
    glVertex2f(-200, 103) #titik u4
    glVertex2f(-174, 121) #titik v4
    glVertex2f(-160, 160) #titik k1
    glEnd()
    

    #//2 sisi dalam
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(-240, 160) #titik d1
    glVertex2f(-230,143) # titik r4
    glVertex2f(-207, 145) #titik w4
    glVertex2f(-200, 160) #titik l1
    glEnd()

    #//3
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(-200, 160) #titik l1
    glVertex2f(-160, 160) #titik k1
    glVertex2f(-160, 280) #titik j1
    glVertex2f(-200, 280) #titik i1

    #huruf L
    #//1
    glVertex2f(-120, 260) #titik a
    glVertex2f(-80, 260) #titik e
    glVertex2f(-80, 100) #titik z4
    glVertex2f(-120, 100) #titik b

    #//2
    glVertex2f(-120, 140) #titik a5
    glVertex2f(20, 140) #titik d
    glVertex2f(20, 100) #titik c
    glVertex2f(-120, 100) #titik b



    #Huruf S
    #//1
    glVertex2f(170, 130) #titik i
    glVertex2f(170, 100) #titik j
    glVertex2f(320, 100) #titik k
    glVertex2f(320, 130) #titik l

    #//2
    glVertex2f(320, 160) #titik m
    glVertex2f(320, 190) #titik n1
    glVertex2f(270, 190) #titik o1
    glVertex2f(270, 160) #titik n

    #//3
    glVertex2f(270, 250) #titik p1
    glVertex2f(270, 220) #titik s1
    glVertex2f(350, 220) #titik r1
    glVertex2f(350, 250) #titik q1
    glEnd()

    #//4 Lengkungan dalam
    glBegin(GL_POLYGON)
    glVertex2f(320, 100) #titik k
    glVertex2f(340, 105) #titik b5
    glVertex2f(358, 121) #titik c5
    glVertex2f(365, 143) #titik d5
    glVertex2f(362, 159) #titik e5
    glVertex2f(343, 183) #titik f5
    glVertex2f(320, 190) #titik n1
    glEnd()

    #//5 Lengkungan luar
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(320, 130) #titik l
    glVertex2f(330, 134) #titik i5
    glVertex2f(335, 144) #titik g5
    glVertex2f(331, 155) #titik h5
    glVertex2f(320, 160) #titik m
    glEnd()

    #//6 lengkungan #2 luar
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex2f(270, 160) #titik n
    glVertex2f(250, 165) #titik j5
    glVertex2f(232, 180) #titik k5
    glVertex2f(225, 200) #titik l5
    glVertex2f(228, 222) #titik m5
    glVertex2f(240, 239) #titik n5
    glVertex2f(253, 247) #titik o5
    glVertex2f(270, 250) #titik p1
    glEnd()

    #//6 lengkungan #2 dalam
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(270, 190) #titik o1
    glVertex2f(260, 194) #titik r5
    glVertex2f(255, 206) #titik p5
    glVertex2f(260, 216) #titik q5
    glVertex2f(270, 220) #titik s1
    glEnd()

    #Huruf E
    #//1
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(380, 250) #titik t1
    glVertex2f(380, 100) #titik u1
    glVertex2f(410, 100) #titik v1
    glVertex2f(410, 250) #titik w1

    #//2
    glVertex2f(380, 250) #titik t1
    glVertex2f(380, 220) #titik c2
    glVertex2f(500, 220) #titik d2
    glVertex2f(500, 250) #titik e2

    #//3
    glVertex2f(380, 130) #titik z1
    glVertex2f(380, 100) #titik u1
    glVertex2f(500, 100) #titik b2
    glVertex2f(500, 130) #titik a2

    #//4
    glVertex2f(440, 190) #titik f2
    glVertex2f(440, 160) #titik g2
    glVertex2f(560, 160) #titik h2
    glVertex2f(560, 190) #titik i2
    glEnd()


def player_killed_action():
    glColor3f(0,1,0)
    glBegin(GL_LINES)
    glVertex2f(-200, -150) #titik k2
    glVertex2f(-200, -300) #titik n2

    glVertex2f(-200, -200) #titik o2
    glVertex2f(-240, -240) #titik q2

    glVertex2f(-200, -200) #titik o2
    glVertex2f(-160, -240) #titik p2

    glVertex2f(-200, -300) #titik n2
    glVertex2f(-240, -340) #titik r2

    glVertex2f(-200, -300) #titik n2
    glVertex2f(-160, -340) #titik s2
    glEnd()

def npc_kill_action():
    glColor3f(1,0,0)
    glBegin(GL_LINES)
    glVertex2f(40, -150) #titik m2
    glVertex2f(40, -300) #titik w2

    glVertex2f(40, -200) #titik b3
    glVertex2f(-20, -160) #titik c3

    glVertex2f(40, -200) #titik b3
    glVertex2f(120, -180) #titik d3

    glVertex2f(40, -300) #titik w2
    glVertex2f(80, -340) #titik a3

    glVertex2f(40, -300) #titik w2
    glVertex2f(5, -340) #titik z2
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(-30, -170) #titik f3
    glVertex2f(-20, -170) #titik g3
    glVertex2f(-20, -150) #titik h3
    glVertex2f(-30, -150) #titik s5

    glVertex2f(-20, -150) #titik h3
    glVertex2f(-20, -160) #titik c3
    glVertex2f(-50, -160) #titik j3
    glVertex2f(-50, -150) #titik i3
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(40, -62) #titik t2
    glVertex2f(20, -102) #titik u2
    glVertex2f(60, -102) #titik v2
    glEnd()



def lingkaran_polygon(Posisi_x, Posisi_y, Radius, Jumlah_titik):
    glBegin(GL_POLYGON)    
    for i in range(360):    
        sudut = i * (2*pi/Jumlah_titik)
        x = Posisi_x + Radius * cos(sudut)
        y = Posisi_y + Radius * sin(sudut)
        glVertex2f(x, y)
    glEnd()

def Circle():
    glColor3f(1,1,1)
    lingkaran_polygon(-360, 170, 70, 100) #Huruf o #1 sisi luar
    lingkaran_polygon(100, 170, 70, 100) #Huruf o #2 sisi luar

    glColor3ub(204, 14, 117) #warma pink squid game
    lingkaran_polygon(-360, 170, 40, 100) #Huruf o #1 sisi dalam
    lingkaran_polygon(100, 170, 40, 100) #Huruf o #2 sisi dalam

    glColor3f(0,1,0)
    lingkaran_polygon(-200, -100, 50, 100) #kepala player

    glColor3f(1,0,0)
    lingkaran_polygon(-200, -80, 5, 100) #kepala player

    glColor3f(1,0,0)
    lingkaran_polygon(40, -100, 50, 100) #kepala npc

def logo():
    glColor3ub(204, 14, 117) #warma pink squid game
    glBegin(GL_QUADS)
    glVertex2f(-500, -50) #titik d9
    glVertex2f(-200, -50) #titik e9
    glVertex2f(-200, 250)#titik f9
    glVertex2f(-500, 250) #titik c9

    glColor3f(0,0,0)
    glVertex2f(-470, 220) #titik g9
    glVertex2f(-230, 220) #titik h9
    glVertex2f(-230, -20)#titik i9
    glVertex2f(-470, -20) #titik j9
    glEnd()

    glColor3ub(204, 14, 117) #warma pink squid game
    glBegin(GL_TRIANGLES)
    glVertex2f(-100, -50) #titik k9
    glVertex2f(200, -50) #titik m9
    glVertex2f(50, 250)#titik l9

    glColor3f(0,0,0)
    glVertex2f(-50, -20) #titik n9
    glVertex2f(150, -20) #titik p9
    glVertex2f(50, 190)#titik 09
    glEnd()
    glColor3ub(204, 14, 117) #warma pink squid game
    lingkaran_polygon(400, 100,160,100)

    glColor3f(0,0,0)
    lingkaran_polygon(400, 100,120,100)

def iterate():
    glViewport(0, 0, 1364, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-682.,682.,-350.,350.)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def ShowScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #letak background
    background()

    iterate()
    #letak objek
    logo()
    tulisan()
    Circle()
    player_killed_action()
    npc_kill_action()

    glutSwapBuffers()
def Main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1364, 700)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("Layer Menang")
    # timer(0) #fungsi timer dipanggil disini
    glutDisplayFunc(ShowScreen)
    # glutMouseFunc(iniHandleMouse)
    glutIdleFunc(ShowScreen)
    glutMainLoop()

Main()
