import glfw
from OpenGL.GL import *
import numpy as np

p0 = np.array([200.,200.])
p3 = np.array([400.,400.])
p1 = np.array([300.,350.])
p2 = np.array([500.,550.])
gEditingPoint = ''

def render():
    global p0, p1,p2,p3
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,640, 0,640, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3ub(255, 255, 255)
    glBegin(GL_LINE_STRIP)
    for t in np.arange(0,1,.01):
        p = [t*t*t,t*t,t,1]@np.array([[-1,3,-3,1],
                                      [3,-6,3,0],
                                      [-3,3,0,0],
                                      [1,0,0,0],
                                      ])@np.array([p0,
                                                   p1,
                                                   p2,
                                                   p3,
                                                   ])
        glVertex2fv(p)
    glEnd()
    
    glColor3ub(0, 255, 0)
    glBegin(GL_LINE_STRIP)
    glVertex2fv(p0)
    glVertex2fv(p1)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2fv(p0)
    glVertex2fv(p3)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2fv(p1)
    glVertex2fv(p2)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2fv(p3)
    glVertex2fv(p2)
    glEnd()


    glPointSize(20.)
    glBegin(GL_POINTS)
    glVertex2fv(p0)
    glVertex2fv(p1)
    glVertex2fv(p2)
    glVertex2fv(p3)
    glEnd()

def button_callback(window, button, action, mod):
    global p0, p1, gEditingPoint,p2,p3
    if button==glfw.MOUSE_BUTTON_LEFT:
        x, y = glfw.get_cursor_pos(window)
        y = 640 - y
        if action==glfw.PRESS:
            if np.abs(x-p0[0])<10 and np.abs(y-p0[1])<10:
                gEditingPoint = 'p0'
            elif np.abs(x-p1[0])<10 and np.abs(y-p1[1])<10:
                gEditingPoint = 'p1'
            elif np.abs(x-p2[0])<10 and np.abs(y-p2[1])<10:
                gEditingPoint = 'pv0'
            elif np.abs(x-p3[0])<10 and np.abs(y-p3[1])<10:
                gEditingPoint = 'pv1'
        elif action==glfw.RELEASE:
            gEditingPoint = ''

def cursor_callback(window, xpos, ypos):
    global p0, p1, gEditingPoint,p2,p3
    ypos = 640 - ypos
    if gEditingPoint=='p0':
        p0[0]=xpos; p0[1]=ypos
    elif gEditingPoint=='p1':
        p1[0]=xpos; p1[1]=ypos
    elif gEditingPoint=='pv0':
        p2[0]=xpos; p2[1]=ypos
    elif gEditingPoint=='pv1':
        p3[0]=xpos; p3[1]=ypos

def main():
    if not glfw.init():
        return
    window = glfw.create_window(640,640,'Lecture23', None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_mouse_button_callback(window, button_callback)
    glfw.set_cursor_pos_callback(window, cursor_callback)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()

