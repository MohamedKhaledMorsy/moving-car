from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
angle=0
x=0
forward = True

def draw_sky():
    glColor3f(0,0.4,0.8)
    glBegin(GL_POLYGON)
    glVertex(10 ,10,0)
    glVertex(10 ,6,0)
    glVertex(-20,6,0)
    glVertex(-20,10,0)
    glEnd()

def draw_road():
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    glVertex(10 ,2,0)
    glVertex(10 ,-5,0)
    glVertex(-50,-5,0)
    glVertex(-50,2,0)
    glEnd()

def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60,1,1,30)
    gluLookAt(8,9,10,
              0,0,0,
              0,1,0)
    glClearColor(0,0.5,0.2,1)

def draw():
    global angle
    global  x
    global forward
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    draw_sky()
    draw_road()

    glColor3f(1,1,1)
    glLoadIdentity()
    glTranslate(0.125*x+2.5,7.5,0.5)
    glutSolidSphere(0.7,100,100)

    glColor3f(1,1,1)
    glLoadIdentity()
    glTranslate(0.125*x+3.2,7.5,0.5)
    glutSolidSphere(0.4,100,100)

    glColor3f(1,1,1)
    glLoadIdentity()
    glTranslate(0.125*x+1.8,7.3,0.5)
    glutSolidSphere(0.35,100,100)

    glColor3f(1,1,1)
    glLoadIdentity()
    glTranslate(0.125*x-2.5,7.5,0.5)
    glutSolidSphere(0.55,100,100)

    glColor3f(1,1,1)
    glLoadIdentity()
    glTranslate(0.125*x-3.2,7.4,0.5)
    glutSolidSphere(0.3,100,100)

    glColor3f(1,1,1)
    glLoadIdentity()
    glTranslate(0.125*x-1.8,7.65,0.5)
    glutSolidSphere(0.3,100,100)

    glColor3f(1,1,1)
    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(0-x,-1,-1.5)
    glVertex(0-x,-1,-2.5)
    glVertex(6-x,-1,-2.5)
    glVertex(6-x,-1,-1.5)
    glEnd()

    glColor3f(1,1,1)
    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(11-x,-1,-1.5)
    glVertex(11-x,-1,-2.5)
    glVertex(16-x,-1,-2.5)
    glVertex(16-x,-1,-1.5)
    glEnd()

    glColor3f(1,1,1)
    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(-11-x,-1,-1.5)
    glVertex(-11-x,-1,-2.5)
    glVertex(-5-x,-1,-2.5)
    glVertex(-5-x,-1,-1.5)
    glEnd()

    glColor3f(1,1,1)
    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(-16-x,-1,-1.5)
    glVertex(-16-x,-1,-2.5)
    glVertex(-22-x,-1,-2.5)
    glVertex(-22-x,-1,-1.5)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(-28-x,-1,-1.5)
    glVertex(-28-x,-1,-2.5)
    glVertex(-34-x,-1,-2.5)
    glVertex(-34-x,-1,-1.5)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(0-x,-1,1)
    glVertex(0-x,-1,0)
    glVertex(6-x,-1,0)
    glVertex(6-x,-1,1)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(11-x,-1,1)
    glVertex(11-x,-1,0)
    glVertex(16-x,-1,0)
    glVertex(16-x,-1,1)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(-11-x,-1,1)
    glVertex(-11-x,-1,0)
    glVertex(-5-x,-1,0)
    glVertex(-5-x,-1,1)
    glEnd()

    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(-16-x,-1,1)
    glVertex(-16-x,-1,0)
    glVertex(-22-x,-1,0)
    glVertex(-22-x,-1,1)
    glEnd()

    glColor3f(0.9,0.9,0)
    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(x+2.5,-1,-1)
    glVertex(x+2.5,-1,0.5)
    glVertex(x+6,-1,1.5)
    glVertex(x+6,-1,-2)
    glEnd()

    glColor3f(0.4,0.4,0.4)
    glLoadIdentity()
    glTranslate(x+0.25*5,-0.125*5,0.25*5)
    glRotate( angle ,0,0,1)
    glutSolidTorus(0.15,0.5,20,10)

    glColor3f(0.4,0.4,0.4)
    glLoadIdentity()
    glTranslate(x-0.25*5,-0.125*5,0.25*5)
    glRotate( angle ,0,0,1)
    glutSolidTorus(0.15,0.5,20,10)

    glColor3f(0,0,0.4)
    glLoadIdentity()
    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

    glColor3f(0,0,0.4)
    glLoadIdentity()
    glTranslate(x+0,4*0.25,0)
    glScale(0.5,0.25,0.5)
    glutSolidCube(5)

    glColor3f(0.5,0.5,0.5)
    glLoadIdentity()
    glBegin(GL_POLYGON)
    glVertex(x+1.28,0.75,1.3)
    glVertex(x+1.28,0.75,-1)
    glVertex(x+1.28,1.5,-1)
    glVertex(x+1.28,1.5,1.3)
    glEnd()

    glColor3f(0.9,0.9,0)
    glLoadIdentity()
    glTranslate(x+2.4,0,-0.8)
    glutSolidSphere(0.2,100,100)

    glColor3f(0.9,0.9,0)
    glLoadIdentity()
    glTranslate(x+2.4,0,0.5)
    glutSolidSphere(0.2,100,100)

    glutSwapBuffers()
    if forward :
        angle -= 0.5
        x += 0.005
        if x> 5:
            forward = False
    else:
        angle += 0.5
        x -= 0.005
        if x < -7:
            forward =True

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"moving car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
