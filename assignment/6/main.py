import glfw
from OpenGL.GL import *
import numpy as np

gComposedM=np.identity(3)

def render(T) :
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()

	#draw coordinate
	glBegin(GL_LINES)
	glColor3ub(255,0,0)
	glVertex2fv(np.array([0.,0.]))
	glVertex2fv(np.array([1.,0.]))
	glColor3ub(0,255,0)
	glVertex2fv(np.array([0.,0.]))
	glVertex2fv(np.array([0.,1.]))
	glEnd()

	#draw traingle
	glBegin(GL_TRIANGLES)
	glColor3ub(255,255,255)
	glVertex2fv((T@np.array([.0,0.5,1.0]))[:-1])
	glVertex2fv((T@np.array([.0,.0,1.]))[:-1])
	glVertex2fv((T@np.array([.5,.0,1.]))[:-1])
	glEnd()

def key_callback(window, key, scancode, action, mods):
	global gComposedM
	if key==glfw.KEY_Q:
		if action==glfw.PRESS:
			new=np.array([[1.0,0.0,-0.1],
                                      [0.0,1.0,.0],
                                      [0.0,0.0,1.0]])
			gComposedM = new @ gComposedM
	if key==glfw.KEY_E:
		if action==glfw.PRESS:
			new=np.array([[1.0,0.0,0.1],
                                      [0.0,1.0,.0],
                                      [0.0,0.0,1.0]])
			gComposedM = new @ gComposedM
	if key==glfw.KEY_A:
		if action==glfw.PRESS:
			th = np.radians(10)
			new=np.array([[np.cos(th),-np.sin(th),.0],
                                       [np.sin(th),np.cos(th),.0],
                                       [.0,.0,1.0]])
			gComposedM = gComposedM @ new
	if key==glfw.KEY_D:
		if action==glfw.PRESS:
			th = np.radians(10)
			new=np.array([[np.cos(th),np.sin(th),.0],
                                       [-np.sin(th),np.cos(th),.0],
                                       [.0,.0,1.0]])
			gComposedM = gComposedM @ new
	if key==glfw.KEY_1:
		if action==glfw.PRESS:
			gComposedM = np.identity(3)
	elif key==glfw.KEY_SPACE and action==glfw.PRESS:
		print ('press space: (%d, %d)'%glfw.get_cursor_pos(window))
		
def main():
    global gComposedM
    if not glfw.init():
        return
    window =glfw.create_window(480,480,"2013011491",None,None)
    if not window:
        glfw.terminate()
        return
    glfw.set_key_callback(window, key_callback)
    glfw.make_context_current(window)

    glfw.swap_interval(0)

    count =0
    while not glfw.window_should_close(window):
        glfw.poll_events()
                      
        render(gComposedM)

        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__":
    main() 
