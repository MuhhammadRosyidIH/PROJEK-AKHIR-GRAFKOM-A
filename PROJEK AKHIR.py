import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from math import *
print("Sukses Import OpenGL!")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 1364, 700

# ===== SQUID GAME =====

def Lingkaran_Polygon(Posisi_x, Posisi_y, Radius, Jumlah_titik):          
    glBegin(GL_POLYGON)    
    for i in range(360):    
        sudut = i * (2*pi/Jumlah_titik)
        x = Posisi_x + Radius * cos(sudut)
        y = Posisi_y + Radius * sin(sudut)
        glVertex2f(x, y)
    glEnd()

def bg_menu():

    # -=-=-=-=- Latar -=-=-=-=-
    glBegin(GL_QUADS)
    # BG layer 1
    glColor3ub(23, 21, 19)
    glVertex2f(-682, -350)
    glVertex2f(-682, 350)
    glVertex2f(682, 350)
    glVertex2f(682, -350)
    # Tanah
    glColor3ub(46, 46, 41)
    glVertex2f(-682, -350)
    glVertex2f(-682, -300)
    glVertex2f(682, -300)
    glVertex2f(682,-350)
    # BG layer 2
    glColor3ub(36, 36, 33)
    glVertex2f(-482, -250)
    glVertex2f(-482, 250)
    glVertex2f(482, 250)
    glVertex2f(482, -250)
    # BG layer 3
    glColor3ub(74, 74, 54)
    glVertex2f(-282, -150)
    glVertex2f(-282, 150)
    glVertex2f(282, 150)
    glVertex2f(282, -150)
    # Frame atas
    glColor3ub(38, 38, 30)
    glVertex2f(-682, 350)
    glVertex2f(-642, 330)
    glVertex2f(642, 330)
    glVertex2f(682, 350)
    # Frame bawah
    glVertex2f(-682, -350)
    glVertex2f(-642, -330)
    glVertex2f(642, -330)
    glVertex2f(682, -350)
    # Frame kiri
    glVertex2f(-682, 350)
    glVertex2f(-662, 310)
    glVertex2f(-662, -310)
    glVertex2f(-682, -350)
    # Frame kanan
    glVertex2f(682, 350)
    glVertex2f(662, 310)
    glVertex2f(662, -310)
    glVertex2f(682, -350)
    glEnd()

    # Lampu Frame atas & lampu bawah
    def Lampu1(x):
        # Lampu frame atas
        glBegin(GL_QUADS)
        glColor3ub(255, 255, 255)
        glVertex2f(-601 + x, 340)
        glVertex2f(-597 + x, 335)
        glVertex2f(-593 + x, 340)
        glVertex2f(-597 + x, 345)

        # lampu frame bawah
        glVertex2f(-601 + x, -340)
        glVertex2f(-597 + x, -335)
        glVertex2f(-593 + x, -340)
        glVertex2f(-597 + x, -345)
        glEnd()

     # Lampu Frame kanan & lampu kiri
    def Lampu2(y):
        # Lampu frame kanan
        glBegin(GL_QUADS)
        glColor3ub(255, 255, 255)
        glVertex2f(676, 245 - y)
        glVertex2f(672, 240 - y)
        glVertex2f(668, 245 - y)
        glVertex2f(672, 250 - y)
        # lampu frame kiri
        glVertex2f(-676, 245 - y)
        glVertex2f(-672, 240 - y)
        glVertex2f(-668, 245 - y)
        glVertex2f(-672, 250 - y)
        glEnd()
    
    kor_x = (0,100,200,300,400,500,600,700,800,900,1000,1100,1200)
    kor_y = (0,100,200,300,400,500)
    for i in kor_x:
        Lampu1(i)
    for i in kor_y:
        Lampu2(i)

    # -=-=-=-=- Jembatan -=-=-=-=-

    # Kerangka Jembatan Kiri
    glBegin(GL_QUADS)
    glColor3ub(235, 242, 15)
    glVertex2f(-662, 0)
    glVertex2f(-662, -10)
    glVertex2f(-152, -10)
    glVertex2f(-142, 0)
    # Penopang miring
    glVertex2f(-542, -10)
    glVertex2f(-662, -80)
    glVertex2f(-662, -90)
    glVertex2f(-522, -10)
    # Besi Bawah
    glVertex2f(-572, -30)
    glVertex2f(-572, -35)
    glVertex2f(-222, -35)
    glVertex2f(-222, -30)
    # Besi Bawah Miring
    glVertex2f(-222, -35)
    glVertex2f(-222, -30)
    glVertex2f(-182, -10)
    glVertex2f(-172, -10)
    # Lampu Atas
    glColor3ub(255, 255, 255)
    glVertex2f(-394, 45)
    glVertex2f(-387, 45)
    glVertex2f(-387, 43)
    glVertex2f(-394, 43)
    glVertex2f(-614, 45)
    glVertex2f(-607, 45)
    glVertex2f(-607, 43)
    glVertex2f(-614, 43)
    # Lampu Bawah
    glVertex2f(-247, -10)
    glVertex2f(-247, -12.5)
    glVertex2f(-267, -12.5)
    glVertex2f(-267, -10)
    glVertex2f(-367, -10)
    glVertex2f(-367, -12.5)
    glVertex2f(-387, -12.5)
    glVertex2f(-387, -10)
    glVertex2f(-487, -10)
    glVertex2f(-487, -12.5)
    glVertex2f(-507, -12.5)
    glVertex2f(-507, -10)
    glEnd()
    # Pilar bawah
    glBegin(GL_LINES)
    glColor3ub(235, 242, 15)
    glVertex2f(-227, -10)
    glVertex2f(-227, -30)
    glVertex2f(-287, -10)
    glVertex2f(-287, -30)
    glVertex2f(-347, -10)
    glVertex2f(-347, -30)
    glVertex2f(-407, -10)
    glVertex2f(-407, -30)
    glVertex2f(-467, -10)
    glVertex2f(-467, -30)
    glVertex2f(-527, -10)
    glVertex2f(-527, -30)
    # Pegangan
    glVertex2f(-212, 0)
    glVertex2f(-212, 7.5)
    glVertex2f(-252, 0)
    glVertex2f(-252, 7.5)
    glVertex2f(-207, 7.5)
    glVertex2f(-257, 7.5)
    # --
    glVertex2f(-322, 0)
    glVertex2f(-322, 7.5)
    glVertex2f(-362, 0)
    glVertex2f(-362, 7.5)
    glVertex2f(-317, 7.5)
    glVertex2f(-367, 7.5)
    # --
    glVertex2f(-432, 0)
    glVertex2f(-432, 7.5)
    glVertex2f(-472, 0)
    glVertex2f(-472, 7.5)
    glVertex2f(-427, 7.5)
    glVertex2f(-477, 7.5)
    # --
    glVertex2f(-542, 0)
    glVertex2f(-542, 7.5)
    glVertex2f(-582, 0)
    glVertex2f(-582, 7.5)
    glVertex2f(-537, 7.5)
    glVertex2f(-587, 7.5)
    # Tiang Lampu
    glVertex2f(-399.5, 0)
    glVertex2f(-399.5, 50)
    glVertex2f(-402, 45)
    glVertex2f(-382, 45)
    # --
    glVertex2f(-619.5, 0)
    glVertex2f(-619.5, 50)
    glVertex2f(-622, 45)
    glVertex2f(-602, 45)
    glEnd()

    # Kerangka Jembatan Kanan
    glBegin(GL_QUADS)
    glColor3ub(235, 242, 15)
    glVertex2f(662, 0)
    glVertex2f(662, -10)
    glVertex2f(152, -10)
    glVertex2f(142, 0)
    # Penopang miring
    glVertex2f(542, -10)
    glVertex2f(662, -80)
    glVertex2f(662, -90)
    glVertex2f(522, -10)
    # Besi Bawah
    glVertex2f(572, -30)
    glVertex2f(572, -35)
    glVertex2f(222, -35)
    glVertex2f(222, -30)
    # Besi Bawah Miring
    glVertex2f(222, -35)
    glVertex2f(222, -30)
    glVertex2f(182, -10)
    glVertex2f(172, -10)
    # Lampu Atas
    glColor3ub(255, 255, 255)
    glVertex2f(394, 45)
    glVertex2f(387, 45)
    glVertex2f(387, 43)
    glVertex2f(394, 43)
    glVertex2f(614, 45)
    glVertex2f(607, 45)
    glVertex2f(607, 43)
    glVertex2f(614, 43)
    # Lampu Bawah
    glVertex2f(247, -10)
    glVertex2f(247, -12.5)
    glVertex2f(267, -12.5)
    glVertex2f(267, -10)
    glVertex2f(367, -10)
    glVertex2f(367, -12.5)
    glVertex2f(387, -12.5)
    glVertex2f(387, -10)
    glVertex2f(487, -10)
    glVertex2f(487, -12.5)
    glVertex2f(507, -12.5)
    glVertex2f(507, -10)
    glEnd()
    # Pilar bawah
    glBegin(GL_LINES)
    glColor3ub(235, 242, 15)
    glVertex2f(227, -10)
    glVertex2f(227, -30)
    glVertex2f(287, -10)
    glVertex2f(287, -30)
    glVertex2f(347, -10)
    glVertex2f(347, -30)
    glVertex2f(407, -10)
    glVertex2f(407, -30)
    glVertex2f(467, -10)
    glVertex2f(467, -30)
    glVertex2f(527, -10)
    glVertex2f(527, -30)
    # Pegangan
    glVertex2f(212, 0)
    glVertex2f(212, 7.5)
    glVertex2f(252, 0)
    glVertex2f(252, 7.5)
    glVertex2f(207, 7.5)
    glVertex2f(257, 7.5)
    # --
    glVertex2f(322, 0)
    glVertex2f(322, 7.5)
    glVertex2f(362, 0)
    glVertex2f(362, 7.5)
    glVertex2f(317, 7.5)
    glVertex2f(367, 7.5)
    # --
    glVertex2f(432, 0)
    glVertex2f(432, 7.5)
    glVertex2f(472, 0)
    glVertex2f(472, 7.5)
    glVertex2f(427, 7.5)
    glVertex2f(477, 7.5)
    # --
    glVertex2f(542, 0)
    glVertex2f(542, 7.5)
    glVertex2f(582, 0)
    glVertex2f(582, 7.5)
    glVertex2f(537, 7.5)
    glVertex2f(587, 7.5)
    # Tiang Lampu
    glVertex2f(399.5, 0)
    glVertex2f(399.5, 50)
    glVertex2f(402, 45)
    glVertex2f(382, 45)
    # --
    glVertex2f(619.5, 0)
    glVertex2f(619.5, 50)
    glVertex2f(622, 45)
    glVertex2f(602, 45)
    glEnd()

def Tulisan_Squid_Game_Menu():
    # BG Tulisan
    glBegin(GL_QUADS)
    glColor3ub(15, 31, 19)
    # ats
    glVertex2f(-322, 262)
    glVertex2f(-287, 182)
    glVertex2f(242, 182)
    glVertex2f(207, 262)
    # bwh
    glVertex2f(-242, 192)
    glVertex2f(-207, 112)
    glVertex2f(322, 112)
    glVertex2f(287, 192)
    glEnd()

    glColor3ub(255,255,255)
    # HURUF ATAS
    glBegin(GL_QUADS)
    glVertex2f(-175, 255)
    glVertex2f(-150, 189)
    glVertex2f(-270, 189)
    glVertex2f(-295, 255)
    glVertex2f(-70, 255)
    glVertex2f(-45, 189)
    glVertex2f(-135, 189)
    glVertex2f(-160, 255)
    glVertex2f(35, 255)
    glVertex2f(60, 189)
    glVertex2f(-30, 189)
    glVertex2f(-55, 255)
    glVertex2f(80, 255)
    glVertex2f(105, 189)
    glVertex2f(90, 189)
    glVertex2f(65, 255)
    glVertex2f(195, 255)
    glVertex2f(220, 189)
    glVertex2f(130, 189)
    glVertex2f(105, 255)

    glColor3ub(15, 31, 19)
    # TUTUP TULISAN ATAS
    glVertex2f(-235, 255)
    glVertex2f(-216, 200)
    glVertex2f(-276, 200)
    glVertex2f(-295, 255)
    glEnd()

def Game1_Penjaga():

    # Sepatu
    glBegin(GL_POLYGON)
    glColor3ub(0,0,0)
    glVertex2f(-672, -50)
    glVertex2f(-668, -50)
    glVertex2f(-660, -50)
    glVertex2f(-668, -45)
    glVertex2f(-672, -45)
    glEnd()

    # Celana
    glBegin(GL_QUADS)
    glColor3ub(255,0,0)
    glVertex2f(-668, -45)
    glVertex2f(-672, -45)
    glVertex2f(-675, -26)
    glVertex2f(-666, -26)

    # Baju
    glVertex2f(-666, -26)
    glVertex2f(-675, -26)
    glVertex2f(-673.5, 0)
    glVertex2f(-667, 0)

    # Sabuk
    glColor3ub(0,0,0)
    glVertex2f(-675.5, -26)
    glVertex2f(-665.5, -26)
    glVertex2f(-666.5, -24)
    glVertex2f(-675.5, -24)
    glEnd()

    # Kepala
    glColor3ub(255,0,0)
    Lingkaran_Polygon(-670.5, 6, 7, 60)
    glColor3ub(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(-667.5, 2)
    glVertex2f(-667.5, 10)
    glVertex2f(-666.5, -1)
    glVertex2f(-666.5, 13)
    glVertex2f(-665.5, 0)
    glVertex2f(-665.5, 12)
    glVertex2f(-664.5, 2)
    glVertex2f(-664.5, 10)
    glColor3ub(255,255,255)
    glVertex2f(-665.5, 3)
    glVertex2f(-665.5, 9)
    glVertex2f(-665.5, 9)
    glVertex2f(-664, 10)
    glVertex2f(-665.5, 3)
    glVertex2f(-664, 2)
    glEnd()

    # Lengan
    glBegin(GL_LINES)
    # SENAPAN
    glColor3ub(0,0,0)
    glVertex2f(-664, -13)
    glVertex2f(-664, -2)
    glVertex2f(-663, -13)
    glVertex2f(-663, 0)
    glEnd()
    # LENGAN
    glBegin(GL_QUADS)
    glColor3ub(255,0,0)
    glVertex2f(-675,0)
    glVertex2f(-665,-15)
    glVertex2f(-661,-10)
    glVertex2f(-668,0)
    glEnd()
    Lingkaran_Polygon(-663, -12, 3.5, 20)

def Game1_Boneka():

    # Sepatu
    glBegin(GL_POLYGON)
    glColor3ub(0,0,0)
    glVertex2f(-560, -50)
    glVertex2f(-545, -50)
    glVertex2f(-545, -48)
    glVertex2f(-555, -45)
    glVertex2f(-560, -45)
    glEnd()
    Lingkaran_Polygon(-545.5, -48.25, 2, 30)
    Lingkaran_Polygon(-560, -47.5, 3, 30)

    # Kaki
    glBegin(GL_QUADS)
    glColor3ub(194, 242, 220)
    glVertex2f(-555, -45)
    glVertex2f(-561.5, -45)
    glVertex2f(-561.5, -30)
    glVertex2f(-555, -30)
    glColor3ub(3, 255, 139)
    glVertex2f(-561.5, -30)
    glVertex2f(-555, -30)
    glVertex2f(-555, -25)
    glVertex2f(-561.5, -25)
    glEnd()

    # Baju
    glBegin(GL_QUADS)
    glColor3ub(201, 93, 10)
    glVertex2f(-546, -25)
    glVertex2f(-570.5, -25)
    glVertex2f(-562.5, 15)
    glVertex2f(-554, 15)
    glEnd()
    Lingkaran_Polygon(-558.25, 14, 5, 30)
    glColor3ub(225, 255, 0)
    Lingkaran_Polygon(-558.25, 14, 3.5, 30)
    glBegin(GL_QUADS)
    glVertex2f(-561.5, 12)
    glVertex2f(-555, 12)
    glVertex2f(-555, 0)
    glVertex2f(-561.5, 0)
    glEnd()

    # Lengan
    glColor3ub(3, 255, 139)
    glBegin(GL_QUADS)
    glVertex2f(-555.5, 0)
    glVertex2f(-561, 0)
    glVertex2f(-561, -10)
    glVertex2f(-555.5, -10 )
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-555.5, -10)
    glVertex2f(-551, -11.5)
    glVertex2f(-551, -13)
    glVertex2f(-561, -13)
    glVertex2f(- 561, -10)
    glEnd()

def Game1_Peserta():
    pass

def Game_1():

    #=-=-=-=- Latar -=-=-=-=
    #--- LANGIT ---
    glBegin(GL_QUADS)
    glColor3ub(201, 208, 255)
    glVertex2f(-682, -350)
    glVertex2f(-682, 350)
    glVertex2f(682, 350)
    glVertex2f(682, -350)
    glEnd()

    def gunung(x):
        glBegin(GL_TRIANGLES)
        glColor3ub(178, 191, 207)
        glVertex2f(-682+x, 30)
        glVertex2f(-511.5+x, 180)
        glVertex2f(-341+x, 30)
        glEnd()
        glBegin(GL_QUADS)
        glVertex2f(-682+x, -50)
        glVertex2f(-341+x, -50)
        glVertex2f(-341+x, 30)
        glVertex2f(-682+x, 30)
        glEnd()

    def rumput(y):
        glBegin(GL_TRIANGLES)
        glColor3ub(54, 102, 24)
        glVertex2f(-690+y, -50)
        glVertex2f(-677.5+y, -25)
        glVertex2f(-665+y, -50)
        glEnd()

    titik_gunung = (0,341,682,1023)
    titik_rumput = (0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,
                    300,315,330,345,360,375,390,405,420,435,450,465,480,495,510,525,540,555,570,585,
                    600,615,630,645,660,675,690,705,720,735,750,765,780,795,810,825,840,855,870,885,
                    900,915,930,945,960,975,990,1005,1020,1035,1050,1065,1080,1095,1110,1125,1140,1155,1170,1185,
                    1200,1215,1230,1245,1260,1275,1290,1305,1320,1335,1350,1365,1380,1395,1410,1425,1440,1455,1470,1485,)
    for i in titik_gunung:
        gunung(i)
    for i in titik_rumput:
        rumput(i)

    #--- LAND ---
    glBegin(GL_QUADS)
    glColor3ub(0, 255, 140)
    glVertex2f(-682, -350)
    glVertex2f(-682, -50)
    glVertex2f(682, -50)
    glVertex2f(682, -350)

    #--- RUMAH ---
    glColor3ub(173, 255, 196)
    glVertex2f(682, -50)
    glVertex2f(602, -50)
    glVertex2f(602, 30)
    glVertex2f(682, 30)
    # Atap
    glColor3ub(212, 72, 72)
    glVertex2f(682, 30)
    glVertex2f(582, 30)
    glVertex2f(612, 80)
    glVertex2f(682, 80)
    # Pintu
    glColor3ub(54, 38, 21)
    glVertex2f(602, -50)
    glVertex2f(567, -50)
    glVertex2f(567, 10)
    glVertex2f(602, 10)
    glEnd()
    # Jendela
    Lingkaran_Polygon(640,-4,20,60)
    glBegin(GL_QUADS)
    glVertex2f(620, -4)
    glVertex2f(660, -4)
    glVertex2f(660, -34)
    glVertex2f(620, -34)
    glEnd()
    # Kaca Jendela
    glColor3ub(213, 222, 220)
    Lingkaran_Polygon(640,-4,16,60)
    glBegin(GL_QUADS)
    glVertex2f(624, -4)
    glVertex2f(656, -4)
    glVertex2f(656, -30)
    glVertex2f(624, -30)
    # Bingkai
    glColor3ub(54, 38, 21)
    glVertex2f(638, 12)
    glVertex2f(642, 12)
    glVertex2f(642, -30)
    glVertex2f(638, -30)
    glVertex2f(624, -11)
    glVertex2f(656, -11)
    glVertex2f(656, -15)
    glVertex2f(624, -15)
    glEnd()

    #--- POHON ---
    glBegin(GL_QUADS)
    glColor3ub(10, 59, 22)
    glVertex2f(-638, -50)
    glVertex2f(-629, -30)
    glVertex2f(-585, -30)
    glVertex2f(-576, -50)
    glVertex2f(-629, -30)
    glVertex2f(-626, -10)
    glVertex2f(-588, -10)
    glVertex2f(-585, -30)
    glVertex2f(-626, -10)
    glVertex2f(-616, 40)
    glVertex2f(-598, 40)
    glVertex2f(-588, -10)
    # Dahan 1
    glVertex2f(-609, 40)
    glVertex2f(-596, 36)
    glVertex2f(-584, 53)
    glVertex2f(-586, 62)
    glVertex2f(-587, 53)
    glVertex2f(-586, 62)
    glVertex2f(-547, 72)
    glVertex2f(-556, 63)
    # Ranting Dahan 1
    glVertex2f(-595, 52)
    glVertex2f(-585, 54)
    glVertex2f(-596, 80)
    glVertex2f(-602, 80)
    # Dahan 2
    glVertex2f(-609, 40)
    glVertex2f(-617, 32)
    glVertex2f(-634, 53)
    glVertex2f(-632, 62)
    glVertex2f(-632, 62)
    glVertex2f(-634, 53)
    glVertex2f(-655, 66)
    glVertex2f(-662, 75)
    # Ranting Dahan 2
    glVertex2f(-622, 42)
    glVertex2f(-634, 53)
    glVertex2f(-645, 98)
    glVertex2f(-640, 90)
    glEnd()
    # Pucuk Ranting Dahan 1
    glBegin(GL_TRIANGLES)
    glVertex2f(-547, 72)
    glVertex2f(-556, 64)
    glVertex2f(-522, 68)
    glVertex2f(-550, 67)
    glVertex2f(-560, 64)
    glVertex2f(-535, 90)
    glVertex2f(-562, 67)
    glVertex2f(-567, 63)
    glVertex2f(-535, 45)
    glVertex2f(-572, 60)
    glVertex2f(-580, 60)
    glVertex2f(-556, 108)
    glVertex2f(-596, 80)
    glVertex2f(-602, 80)
    glVertex2f(-595, 113)
    glVertex2f(-595, 80)
    glVertex2f(-603, 80)
    glVertex2f(-620, 110)
    glEnd()

    # Garis Bantu
    glBegin(GL_LINES)
    glColor3ub(255,255,255)
    glVertex2f(-682, -50)
    glVertex2f(682, -50)
    glVertex2f(-682, 40)
    glVertex2f(682, 40)
    glEnd()

def Game_2():
        # -=-=-=-=- Latar -=-=-=-=-
    glBegin(GL_QUADS)
    # BG layer 1
    glColor3ub(23, 21, 19)
    glVertex2f(-682, -350)
    glVertex2f(-682, 350)
    glVertex2f(682, 350)
    glVertex2f(682, -350)
    # Tanah
    glColor3ub(46, 46, 41)
    glVertex2f(-682, -350)
    glVertex2f(-682, -300)
    glVertex2f(682, -300)
    glVertex2f(682,-350)
    # BG layer 2
    glColor3ub(36, 36, 33)
    glVertex2f(-482, -250)
    glVertex2f(-482, 250)
    glVertex2f(482, 250)
    glVertex2f(482, -250)
    # BG layer 3
    glColor3ub(74, 74, 54)
    glVertex2f(-282, -150)
    glVertex2f(-282, 150)
    glVertex2f(282, 150)
    glVertex2f(282, -150)
    # Frame atas
    glColor3ub(38, 38, 30)
    glVertex2f(-682, 350)
    glVertex2f(-642, 330)
    glVertex2f(642, 330)
    glVertex2f(682, 350)
    # Frame bawah
    glVertex2f(-682, -350)
    glVertex2f(-642, -330)
    glVertex2f(642, -330)
    glVertex2f(682, -350)
    # Frame kiri
    glVertex2f(-682, 350)
    glVertex2f(-662, 310)
    glVertex2f(-662, -310)
    glVertex2f(-682, -350)
    # Frame kanan
    glVertex2f(682, 350)
    glVertex2f(662, 310)
    glVertex2f(662, -310)
    glVertex2f(682, -350)
    glEnd()

    # Lampu Frame atas & lampu bawah
    def Lampu1(x):
        # Lampu frame atas
        glBegin(GL_QUADS)
        glColor3ub(255, 255, 255)
        glVertex2f(-601 + x, 340)
        glVertex2f(-597 + x, 335)
        glVertex2f(-593 + x, 340)
        glVertex2f(-597 + x, 345)

        # lampu frame bawah
        glVertex2f(-601 + x, -340)
        glVertex2f(-597 + x, -335)
        glVertex2f(-593 + x, -340)
        glVertex2f(-597 + x, -345)
        glEnd()

     # Lampu Frame kanan & lampu kiri
    def Lampu2(y):
        # Lampu frame kanan
        glBegin(GL_QUADS)
        glColor3ub(255, 255, 255)
        glVertex2f(676, 245 - y)
        glVertex2f(672, 240 - y)
        glVertex2f(668, 245 - y)
        glVertex2f(672, 250 - y)
        # lampu frame kiri
        glVertex2f(-676, 245 - y)
        glVertex2f(-672, 240 - y)
        glVertex2f(-668, 245 - y)
        glVertex2f(-672, 250 - y)
        glEnd()
    
    kor_x = (0,100,200,300,400,500,600,700,800,900,1000,1100,1200)
    kor_y = (0,100,200,300,400,500)
    for i in kor_x:
        Lampu1(i)
    for i in kor_y:
        Lampu2(i)

    # -=-=-=-=- Jembatan -=-=-=-=-

    # Kerangka Jembatan Kiri
    glBegin(GL_QUADS)
    glColor3ub(235, 242, 15)
    glVertex2f(-662, 0)
    glVertex2f(-662, -10)
    glVertex2f(-152, -10)
    glVertex2f(-142, 0)
    # Penopang miring
    glVertex2f(-542, -10)
    glVertex2f(-662, -80)
    glVertex2f(-662, -90)
    glVertex2f(-522, -10)
    # Besi Bawah
    glVertex2f(-572, -30)
    glVertex2f(-572, -35)
    glVertex2f(-222, -35)
    glVertex2f(-222, -30)
    # Besi Bawah Miring
    glVertex2f(-222, -35)
    glVertex2f(-222, -30)
    glVertex2f(-182, -10)
    glVertex2f(-172, -10)
    # Lampu Atas
    glColor3ub(255, 255, 255)
    glVertex2f(-394, 45)
    glVertex2f(-387, 45)
    glVertex2f(-387, 43)
    glVertex2f(-394, 43)
    glVertex2f(-614, 45)
    glVertex2f(-607, 45)
    glVertex2f(-607, 43)
    glVertex2f(-614, 43)
    # Lampu Bawah
    glVertex2f(-247, -10)
    glVertex2f(-247, -12.5)
    glVertex2f(-267, -12.5)
    glVertex2f(-267, -10)
    glVertex2f(-367, -10)
    glVertex2f(-367, -12.5)
    glVertex2f(-387, -12.5)
    glVertex2f(-387, -10)
    glVertex2f(-487, -10)
    glVertex2f(-487, -12.5)
    glVertex2f(-507, -12.5)
    glVertex2f(-507, -10)
    glEnd()
    # Pilar bawah
    glBegin(GL_LINES)
    glColor3ub(235, 242, 15)
    glVertex2f(-227, -10)
    glVertex2f(-227, -30)
    glVertex2f(-287, -10)
    glVertex2f(-287, -30)
    glVertex2f(-347, -10)
    glVertex2f(-347, -30)
    glVertex2f(-407, -10)
    glVertex2f(-407, -30)
    glVertex2f(-467, -10)
    glVertex2f(-467, -30)
    glVertex2f(-527, -10)
    glVertex2f(-527, -30)
    # Pegangan
    glVertex2f(-212, 0)
    glVertex2f(-212, 7.5)
    glVertex2f(-252, 0)
    glVertex2f(-252, 7.5)
    glVertex2f(-207, 7.5)
    glVertex2f(-257, 7.5)
    # --
    glVertex2f(-322, 0)
    glVertex2f(-322, 7.5)
    glVertex2f(-362, 0)
    glVertex2f(-362, 7.5)
    glVertex2f(-317, 7.5)
    glVertex2f(-367, 7.5)
    # --
    glVertex2f(-432, 0)
    glVertex2f(-432, 7.5)
    glVertex2f(-472, 0)
    glVertex2f(-472, 7.5)
    glVertex2f(-427, 7.5)
    glVertex2f(-477, 7.5)
    # --
    glVertex2f(-542, 0)
    glVertex2f(-542, 7.5)
    glVertex2f(-582, 0)
    glVertex2f(-582, 7.5)
    glVertex2f(-537, 7.5)
    glVertex2f(-587, 7.5)
    # Tiang Lampu
    glVertex2f(-399.5, 0)
    glVertex2f(-399.5, 50)
    glVertex2f(-402, 45)
    glVertex2f(-382, 45)
    # --
    glVertex2f(-619.5, 0)
    glVertex2f(-619.5, 50)
    glVertex2f(-622, 45)
    glVertex2f(-602, 45)
    glEnd()

    # Kerangka Jembatan Kanan
    glBegin(GL_QUADS)
    glColor3ub(235, 242, 15)
    glVertex2f(662, 0)
    glVertex2f(662, -10)
    glVertex2f(152, -10)
    glVertex2f(142, 0)
    # Penopang miring
    glVertex2f(542, -10)
    glVertex2f(662, -80)
    glVertex2f(662, -90)
    glVertex2f(522, -10)
    # Besi Bawah
    glVertex2f(572, -30)
    glVertex2f(572, -35)
    glVertex2f(222, -35)
    glVertex2f(222, -30)
    # Besi Bawah Miring
    glVertex2f(222, -35)
    glVertex2f(222, -30)
    glVertex2f(182, -10)
    glVertex2f(172, -10)
    # Lampu Atas
    glColor3ub(255, 255, 255)
    glVertex2f(394, 45)
    glVertex2f(387, 45)
    glVertex2f(387, 43)
    glVertex2f(394, 43)
    glVertex2f(614, 45)
    glVertex2f(607, 45)
    glVertex2f(607, 43)
    glVertex2f(614, 43)
    # Lampu Bawah
    glVertex2f(247, -10)
    glVertex2f(247, -12.5)
    glVertex2f(267, -12.5)
    glVertex2f(267, -10)
    glVertex2f(367, -10)
    glVertex2f(367, -12.5)
    glVertex2f(387, -12.5)
    glVertex2f(387, -10)
    glVertex2f(487, -10)
    glVertex2f(487, -12.5)
    glVertex2f(507, -12.5)
    glVertex2f(507, -10)
    glEnd()
    # Pilar bawah
    glBegin(GL_LINES)
    glColor3ub(235, 242, 15)
    glVertex2f(227, -10)
    glVertex2f(227, -30)
    glVertex2f(287, -10)
    glVertex2f(287, -30)
    glVertex2f(347, -10)
    glVertex2f(347, -30)
    glVertex2f(407, -10)
    glVertex2f(407, -30)
    glVertex2f(467, -10)
    glVertex2f(467, -30)
    glVertex2f(527, -10)
    glVertex2f(527, -30)
    # Pegangan
    glVertex2f(212, 0)
    glVertex2f(212, 7.5)
    glVertex2f(252, 0)
    glVertex2f(252, 7.5)
    glVertex2f(207, 7.5)
    glVertex2f(257, 7.5)
    # --
    glVertex2f(322, 0)
    glVertex2f(322, 7.5)
    glVertex2f(362, 0)
    glVertex2f(362, 7.5)
    glVertex2f(317, 7.5)
    glVertex2f(367, 7.5)
    # --
    glVertex2f(432, 0)
    glVertex2f(432, 7.5)
    glVertex2f(472, 0)
    glVertex2f(472, 7.5)
    glVertex2f(427, 7.5)
    glVertex2f(477, 7.5)
    # --
    glVertex2f(542, 0)
    glVertex2f(542, 7.5)
    glVertex2f(582, 0)
    glVertex2f(582, 7.5)
    glVertex2f(537, 7.5)
    glVertex2f(587, 7.5)
    # Tiang Lampu
    glVertex2f(399.5, 0)
    glVertex2f(399.5, 50)
    glVertex2f(402, 45)
    glVertex2f(382, 45)
    # --
    glVertex2f(619.5, 0)
    glVertex2f(619.5, 50)
    glVertex2f(622, 45)
    glVertex2f(602, 45)
    glEnd()

def Game_3():
    
    #=-=-=-=- Latar -=-=-=-=
    #--- LANGIT ---
    glBegin(GL_QUADS)
    glColor3ub(156, 114, 9)
    glVertex2f(-682, -350)
    glVertex2f(-682, 350)
    glVertex2f(682, 350)
    glVertex2f(682, -350)
    glEnd()

def APK():
    #bg_menu()
    #Tulisan_Squid_Game_Menu()
    Game_1()
    Game1_Penjaga()
    Game1_Boneka()

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
    iterate()
    APK()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1364, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("PROJEK AKHIR GRAFKOM A")
glutDisplayFunc(ShowScreen)
glutIdleFunc(ShowScreen)
glutMainLoop()