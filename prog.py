#!/usr/bin/python

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from kg import *
from obj import *


def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    # glEnable(GL_LIGHTING)
    #glEnable(GL_LIGHT0)
    #glEnable(GL_COLOR_MATERIAL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGrid(length, a):
    i = 0
    global s
    # if a<=0: s=a=0.1

    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(-length, 0)
    glVertex2f(length, 0)
    glVertex2f(0, -length)
    glVertex2f(0, length)
    glEnd()

    glColor3f(0.2, 0.2, 0.2)
    while i <= length:
        glBegin(GL_LINES)
        glVertex2f(-length, i)
        glVertex2f(length, i)
        glVertex2f(-length, -i)
        glVertex2f(length, -i)
        glVertex2f(i, -length)
        glVertex2f(i, length)
        glVertex2f(-i, -length)
        glVertex2f(-i, length)
        glEnd()
        i += a


def ReSizeGLScene(Width, Height):
    if Height == 0: Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    global x, y, z
    glTranslatef(x, y, z)
    global q
    modem = [GL_FILL, GL_LINE, GL_POINT]
    colorm = ((0.5, 0.5, 0.5), (1, 0, 0), (0, 0, 1))

    for mode, color in zip(modem, colorm):
        glPolygonMode(GL_FRONT_AND_BACK, mode)
        glBegin(GL_QUADS)
        r, g, b = color
        glColor(r, g, b)
        for i in q():
            i.pop()
            glVertex3fv(i)
        glEnd()

    global l
    global s
    DrawGrid(l, s)

    glutSwapBuffers()


def KeyPressed(*args):
    global q
    global s
    global l, x, y, z
    if args[0] == "\033":
        sys.exit()
    elif args[0] == b"w":
        q.set_z(-1)
    elif args[0] == b"s":
        q.set_z(1)
    elif args[0] == b"a":
        q.set_x(-1)
    elif args[0] == b"d":
        q.set_x(1)
    elif args[0] == b"q":
        q.set_y(-1)
    elif args[0] == b"e":
        q.set_y(1)
    elif args[0] == b"u":
        q.set_anglez(2)
    elif args[0] == b"j":
        q.set_anglez(-2)
    elif args[0] == b"h":
        q.set_anglex(2)
    elif args[0] == b"k":
        q.set_anglex(-2)
    elif args[0] == b"y":
        q.set_angley(2)
    elif args[0] == b"i":
        q.set_angley(-2)


def SpecialKeyPressed(*args):
    tr = 1
    if args[0] == GLUT_KEY_UP:
        q.set_y(tr)
    elif args[0] == GLUT_KEY_DOWN:
        q.set_y(-tr)
    elif args[0] == GLUT_KEY_RIGHT:
        q.set_x(tr)
    elif args[0] == GLUT_KEY_LEFT:
        q.set_x(-tr)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(400, 300)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("2d")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(KeyPressed)
    glutSpecialFunc(SpecialKeyPressed)
    #glutFullScreen()
    InitGL(400, 300)
    glutMainLoop()


x = 0
y = 0
z = -20
a = 3.0
l = 10
s = 1
# q = Polygons3f([Point3f(-a,-a,-a)(), Point3f(a,-a,-a)(), Point3f(-a,a,a)()])#, Point(a,a)()])
q = Polygons3f([Point3f(-a, -a, -a)(),
                Point3f(-a, a, -a)(),
                Point3f(-a, a, a)(),
                Point3f(-a, -a, a)(),
                Point3f(a, -a, -a)(),
                Point3f(a, -a, a)(),
                Point3f(a, a, a)(),
                Point3f(a, a, -a)(),
                Point3f(-a, -a, -a)(),
                Point3f(-a, -a, a)(),
                Point3f(a, -a, a)(),
                Point3f(a, -a, -a)(),
                Point3f(-a, a, -a)(),
                Point3f(-a, a, a)(),
                Point3f(a, a, a)(),
                Point3f(a, a, -a)(),
                Point3f(-a, -a, -a)(),
                Point3f(a, -a, -a)(),
                Point3f(a, a, -a)(),
                Point3f(-a, a, -a)(),
                Point3f(-a, -a, a)(),
                Point3f(a, -a, a)(),
                Point3f(a, a, a)(),
                Point3f(-a, a, a)()
])

model = OBJ("model.obj")

main()
