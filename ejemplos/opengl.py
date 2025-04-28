from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glOrtho(-1, 1, -1, 1, -1, 1)     # Orthographic projection

def display():
    glClear(GL_COLOR_BUFFER_BIT)     # Clear the screen
    glBegin(GL_TRIANGLES)            # Start drawing a triangle
    glColor3f(1.0, 0.0, 0.0)         # Red
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)         # Green
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)         # Blue
    glVertex2f(0.0, 0.5)
    glEnd()
    glFlush()                        # Ensure all commands are executed

glutInit()                           # Initialize GLUT
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"PyOpenGL Triangle")  # Create window
glutInitWindowSize(400, 400)         # Set window size
glutInitWindowPosition(100, 100)     # Position the window
init()
glutDisplayFunc(display)             # Register display callback
glutMainLoop()                       # Enter the event-processing loop
