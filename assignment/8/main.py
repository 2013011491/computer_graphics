import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

gCamAng = 0.
gComposedM = np.identity(4)

def render(camAng):
	global gComposedM
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	glLoadIdentity()
	glOrtho(-1,1, -1,1, -1,1)
	gluLookAt(.1*np.sin(camAng),.1,.1*np.cos(camAng),0,0,0, 0,1,0)
	glBegin(GL_LINES)
	glColor3ub(255, 0, 0)
	glVertex3fv(np.array([0.,0.,0.]))
	glVertex3fv(np.array([1.,0.,0.]))
	glColor3ub(0, 255, 0)
	glVertex3fv(np.array([0.,0.,0.]))
	glVertex3fv(np.array([0.,1.,0.]))
	glColor3ub(0, 0, 255)
	glVertex3fv(np.array([0.,0.,0]))
	glVertex3fv(np.array([0.,0.,1.]))
	glEnd()
	glColor3ub(255,255,255)
	glMultMatrixf(gComposedM.T)
	drawTriangle()

def drawTriangle() :
    glBegin(GL_TRIANGLES)
    glVertex3fv(np.array([.0,.5,0.]))
    glVertex3fv(np.array([.0,.0,0.]))
    glVertex3fv(np.array([.5,.0,0.]))
    glEnd()
    
def key_callback(window, key, scancode, action, mods):
	global gComposedM
	global gCamAng
	if action==glfw.PRESS or action==glfw.REPEAT:
            if key==glfw.KEY_Q:
                new=np.array([[1.0,0.0,0.,-0.1],
                              [0.0,1.0,.0,.0],
                              [0.0,0.0,1.0,.0],
                              [0.0,0.0,0.0,1.0]])
                gComposedM = new @ gComposedM
            elif key==glfw.KEY_E:
                new=np.array([[1.0,0.0,0.0,0.1],
                              [0.0,1.0,.0,0.0],
                              [0.0,0.0,1.0,0.0],
                              [0.0,0.0,0.0,1.0]])
                gComposedM = new @ gComposedM
            elif key==glfw.KEY_A:
                th = np.radians(-10)
                new=np.array([[np.cos(th),0.0,np.sin(th),.0],
                              [0.0,1.0,0.0,0.0],
                              [-np.sin(th),0.0,np.cos(th),0.0],
                              [0.0,0.0,0.0,1.0]])
                gComposedM = gComposedM @ new
            elif key==glfw.KEY_D:
                th = np.radians(10)
                new=np.array([[np.cos(th),0.0,np.sin(th),.0],
                              [0.0,1.0,0.0,0.0],
                              [-np.sin(th),0.0,np.cos(th),0.0],
                              [0.0,0.0,0.0,1.0]])
                gComposedM = gComposedM @ new
            elif key==glfw.KEY_W:
                th = np.radians(-10)
                new=np.array([[1.0,0.0,0.0,.0],
                              [0.0,np.cos(th),-np.sin(th),0.0],
                              [0.0,np.sin(th),np.cos(th),0.0],
                              [0.0,0.0,0.0,1.0]])
                gComposedM = gComposedM @ new
            elif key==glfw.KEY_S:
                th = np.radians(10)
                new=np.array([[1.0,0.0,0.0,.0],
                              [0.0,np.cos(th),-np.sin(th),0.0],
                              [0.0,np.sin(th),np.cos(th),0.0],
                              [0.0,0.0,0.0,1.0]])
                gComposedM = gComposedM @ new
            elif key==glfw.KEY_1:
            	gCamAng+=np.radians(-10)
            elif key==glfw.KEY_3:
                gCamAng+=np.radians(10)
            elif key==glfw.KEY_SPACE and action==glfw.PRESS:
                print ('press space: (%d, %d)'%glfw.get_cursor_pos(window))
        


def main():
    global gCamAng
    if not glfw.init():
        return
    window = glfw.create_window(480,480,'2013011491',None,None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(gCamAng)
        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()
