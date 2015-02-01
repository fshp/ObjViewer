# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *

from obj import OBJ


def keypress(key, x, y):
    if key == b'w':
        glRotatef(5, 1, 0, 0)
    elif key == b's':
        glRotatef(-5, 1, 0, 0)
    elif key == b'a':
        glRotatef(5, 0, 1, 0)
    elif key == b'd':
        glRotatef(-5, 0, 1, 0)
    elif key == b'q':
        glRotatef(5, 0, 0, 1)
    if key == b'e':
        glRotatef(-5, 0, 0, 1)


def specialkeys(key, x, y):
    if key == GLUT_KEY_UP:  # Клавиша вверх
        glRotatef(5, 1, 0, 0)  # Вращаем на 5 градусов по оси X
    if key == GLUT_KEY_DOWN:  # Клавиша вниз
        glRotatef(-5, 1, 0, 0)  # Вращаем на -5 градусов по оси X
    if key == GLUT_KEY_LEFT:  # Клавиша влево
        glRotatef(5, 0, 1, 0)  # Вращаем на 5 градусов по оси Y
    if key == GLUT_KEY_RIGHT:  # Клавиша вправо
        glRotatef(-5, 0, 1, 0)  # Вращаем на -5 градусов по оси Y


def create_shader(shader_type, source):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    return shader


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_PROGRAM_POINT_SIZE)

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, pointdata)

    glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
    glColor(0, 0, 1)
    glDrawElements(GL_TRIANGLES, len(indexes), GL_UNSIGNED_INT, indexes)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glColor(1, 0, 0)
    glDrawElements(GL_TRIANGLES, len(indexes), GL_UNSIGNED_INT, indexes)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glColor(1, 1, 1)
    glDrawElements(GL_TRIANGLES, len(indexes), GL_UNSIGNED_INT, indexes)
    glutSwapBuffers()


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(900, 900)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"Py3D")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(specialkeys)
glutKeyboardFunc(keypress)
glClearColor(0.2, 0.2, 0.2, 1)
vertex = create_shader(GL_VERTEX_SHADER, """
varying vec4 vertex_color;
            void main(){
                gl_Vertex.xyz *=  1.0f;
                gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
                vertex_color = gl_Color;
                gl_PointSize = 3.0;
            }""")
fragment = create_shader(GL_FRAGMENT_SHADER, """
varying vec4 vertex_color;
            void main() {
                gl_FragColor = vertex_color;

}""")
program = glCreateProgram()
glAttachShader(program, vertex)
glAttachShader(program, fragment)
glLinkProgram(program)
glUseProgram(program)
model = OBJ('auto.obj')
pointdata = model.vertices
indexes = model.faces
glEnable(GL_DEPTH_TEST)
glutMainLoop()