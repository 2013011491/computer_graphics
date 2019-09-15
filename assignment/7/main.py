import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

gComposedM=np.identity(4)
camAng=0

def render(M, camAng):
        # enable depth test (we'll see details later)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)

        glLoadIdentity()

        # use orthogonal projection (we'll see details later)
        glOrtho(-1,1, -1,1, -1,1)

        # rotate "camera" position to see this 3D space better (we'll see details later)
        gluLookAt(.1*np.sin(camAng),.1,.1*np.cos(camAng), 0,0,0, 0,1,0)

        # draw coordinate: x in red, y in green, z in blue
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

        # draw triangle
        glBegin(GL_TRIANGLES)
        glColor3ub(255, 255, 255)
        glVertex3fv((M @ np.array([.0,.5,0.,1.]))[:-1])
        glVertex3fv((M @ np.array([.0,.0,0.,1.]))[:-1])
        glVertex3fv((M @ np.array([.5,.0,0.,1.]))[:-1])
        glEnd()
def key_callback(window, key, scancode, action, mods):
	global gComposedM
	global camAng
	if key==glfw.KEY_Q:
		if action==glfw.PRESS:
			new=np.array([[1.0,0.0,0.,-0.1],
                                      [0.0,1.0,.0,.0],
                                      [0.0,0.0,1.0,.0],
                                      [0.0,0.0,0.0,1.0]])
			gComposedM = new @ gComposedM
	if key==glfw.KEY_E:
		if action==glfw.PRESS:
			new=np.array([[1.0,0.0,0.0,0.1],
                                      [0.0,1.0,.0,0.0],
                                      [0.0,0.0,1.0,0.0],
                                      [0.0,0.0,0.0,1.0]])
			gComposedM = new @ gComposedM
	if key==glfw.KEY_A:
		if action==glfw.PRESS:
			th = np.radians(-10)
			new=np.array([[np.cos(th),0.0,np.sin(th),.0],
                                      [0.0,1.0,0.0,0.0],
                                      [-np.sin(th),0.0,np.cos(th),0.0],
                                      [0.0,0.0,0.0,1.0]])
			gComposedM = gComposedM @ new
	if key==glfw.KEY_D:
		if action==glfw.PRESS:
			th = np.radians(10)
			new=np.array([[np.cos(th),0.0,np.sin(th),.0],
                                      [0.0,1.0,0.0,0.0],
                                      [-np.sin(th),0.0,np.cos(th),0.0],
                                      [0.0,0.0,0.0,1.0]])
			gComposedM = gComposedM @ new
	if key==glfw.KEY_W:
		if action==glfw.PRESS:
			th = np.radians(-10)
			new=np.array([[1.0,0.0,0.0,.0],
                                      [0.0,np.cos(th),-np.sin(th),0.0],
                                      [0.0,np.sin(th),np.cos(th),0.0],
                                      [0.0,0.0,0.0,1.0]])
			gComposedM = gComposedM @ new
	if key==glfw.KEY_S:
		if action==glfw.PRESS:
			th = np.radians(10)
			new=np.array([[1.0,0.0,0.0,.0],
                                      [0.0,np.cos(th),-np.sin(th),0.0],
                                      [0.0,np.sin(th),np.cos(th),0.0],
                                      [0.0,0.0,0.0,1.0]])
			gComposedM = gComposedM @ new
	if key==glfw.KEY_1:
		if action==glfw.PRESS:
			camAng=np.radians(-10)+camAng
	if key==glfw.KEY_3:
		if action==glfw.PRESS:
			camAng=np.radians(10)+camAng
	elif key==glfw.KEY_SPACE and action==glfw.PRESS:
		print ('press space: (%d, %d)'%glfw.get_cursor_pos(window))
        
def main():
    global gComposedM
    global camAng
    if not glfw.init():
        return
    window =glfw.create_window(480,480,"2013011491",None,None)
    if not window:
        glfw.terminate()
        return
    glfw.set_key_callback(window, key_callback)
    glfw.make_context_current(window)

    glfw.swap_interval(1)

    count =0
    while not glfw.window_should_close(window):
        glfw.poll_events()

        render(gComposedM,camAng)


        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__":
    main() 
