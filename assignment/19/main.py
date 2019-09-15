import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from OpenGL.arrays import vbo
import ctypes

gCamAng = 0.
gCamHeight = 1.
xn=0
zn=0
yn=0

def drawUnitCube_glVertex():
	glBegin(GL_TRIANGLES)
	glNormal3f(0,1,0) # v0, v1,... v5 normal
	glVertex3f( 0.5, 0.5,-0.5) #v0 position
	glVertex3f(-0.5, 0.5,-0.5) #v1 position
	glVertex3f(-0.5, 0.5, 0.5) #v2 position

	glVertex3f( 0.5, 0.5,-0.5)# v3 position
	glVertex3f(-0.5, 0.5, 0.5)# v4 position
	glVertex3f( 0.5, 0.5, 0.5)# v5 position

	glNormal3f(0,-1,0) # v6, v7,... v11 normal
	glVertex3f( 0.5,-0.5, 0.5) #v6 position
	glVertex3f(-0.5,-0.5, 0.5) #v7 position
	glVertex3f(-0.5,-0.5,-0.5) #v8 position

	glVertex3f( 0.5,-0.5, 0.5)# v9 position
	glVertex3f(-0.5,-0.5,-0.5)# v10 position
	glVertex3f( 0.5,-0.5,-0.5)# v11 position

	glNormal3f(0,0,1)
	glVertex3f( 0.5, 0.5, 0.5)
	glVertex3f(-0.5, 0.5, 0.5)
	glVertex3f(-0.5,-0.5, 0.5)

	glVertex3f( 0.5, 0.5, 0.5)
	glVertex3f(-0.5,-0.5, 0.5)
	glVertex3f( 0.5,-0.5, 0.5)

	glNormal3f(0,0,-1)
	glVertex3f( 0.5,-0.5,-0.5)
	glVertex3f(-0.5,-0.5,-0.5)
	glVertex3f(-0.5, 0.5,-0.5)

	glVertex3f( 0.5,-0.5,-0.5)
	glVertex3f(-0.5, 0.5,-0.5)
	glVertex3f( 0.5, 0.5,-0.5)

	glNormal3f(-1,0,0)
	glVertex3f(-0.5, 0.5, 0.5)
	glVertex3f(-0.5, 0.5,-0.5)
	glVertex3f(-0.5,-0.5,-0.5)

	glVertex3f(-0.5, 0.5, 0.5)
	glVertex3f(-0.5,-0.5,-0.5)
	glVertex3f(-0.5,-0.5, 0.5)

	glNormal3f(1,0,0)
	glVertex3f( 0.5, 0.5,-0.5)
	glVertex3f( 0.5, 0.5, 0.5)
	glVertex3f( 0.5,-0.5, 0.5)

	glVertex3f( 0.5, 0.5,-0.5)
	glVertex3f( 0.5,-0.5, 0.5)
	glVertex3f( 0.5,-0.5,-0.5)

	glEnd()

def createVertexArraySeparate():
	varr = np.array([
		[0,1,0],
		#
		[ 0.5, 0.5,-0.5],
		#
		[0,1,0],
		#
		[-0.5, 0.5,-0.5],
		#
		[0,1,0],
		#
		[-0.5, 0.5, 0.5],
		#
		[0,1,0],
		[ 0.5, 0.5,-0.5],
		[0,1,0],
		[-0.5, 0.5, 0.5],
		[0,1,0],
		[ 0.5, 0.5, 0.5], #
		#
		#
		#
		#
		# v3
		
		[0,-1,0],
		[ 0.5,-0.5, 0.5],
		[0,-1,0],
		[-0.5,-0.5, 0.5],
		[0,-1,0],
		[-0.5,-0.5,-0.5], #
		#
		#
		#
		#
		# v6
	
		[0,-1,0],
		[ 0.5,-0.5, 0.5],
		[0,-1,0],
		[-0.5,-0.5,-0.5],
		[0,-1,0],
		[ 0.5,-0.5,-0.5],
		[0,0,1],
		[ 0.5, 0.5, 0.5],
		[0,0,1],
		[-0.5, 0.5, 0.5],
		[0,0,1],
		[-0.5,-0.5, 0.5],
		[0,0,1],
		[ 0.5, 0.5, 0.5],
		[0,0,1],
		[-0.5,-0.5, 0.5],
		[0,0,1],
		[ 0.5,-0.5, 0.5],
		[0,0,-1],
		[ 0.5,-0.5,-0.5],
		[0,0,-1],
		[-0.5,-0.5,-0.5],
		[0,0,-1],
		[-0.5, 0.5,-0.5],
		[0,0,-1],
		[ 0.5,-0.5,-0.5],
		[0,0,-1],
		[-0.5, 0.5,-0.5],
		[0,0,-1],
		[ 0.5, 0.5,-0.5],
		[-1,0,0],
		[-0.5, 0.5, 0.5],
		[-1,0,0],
		[-0.5, 0.5,-0.5],
		[-1,0,0],
		[-0.5,-0.5,-0.5],
		[-1,0,0],
		[-0.5, 0.5, 0.5],
		[-1,0,0],
		[-0.5,-0.5,-0.5],
		[-1,0,0],
		[-0.5,-0.5, 0.5],
		[1,0,0],
		[ 0.5, 0.5,-0.5],
		[1,0,0],
		[ 0.5, 0.5, 0.5],
		[1,0,0],
		[ 0.5,-0.5, 0.5],
		[1,0,0],
		[ 0.5, 0.5,-0.5],
		[1,0,0],
		[ 0.5,-0.5, 0.5],
		[1,0,0],
		[ 0.5,-0.5,-0.5],
		], 'float32')
	return varr

'''def render(ang):
	global gCamAng, gCamHeight
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	glMatrixMode(GL_PROJECTION) # use projection matrix stack for projection transformation for correct lighting
	glLoadIdentity()
	gluPerspective(45, 1, 1,10)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(5*np.sin(gCamAng),gCamHeight,5*np.cos(gCamAng), 0,0,0, 0,1,0)
	drawFrame()
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	# try to uncomment:
	# light position
	glPushMatrix()
	# glRotatef(ang,0,1,0) # try to uncomment: rotate light
	lightPos = (1.,1.,1.,1.)
	# try to change 4th element to 0. or 1.
	glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
	glPopMatrix()
	# light intensity for each color channel
	ambientLightColor = (.1,.1,.1,1.)
	diffuseLightColor = (1.,1.,1.,1.)
	specularLightColor = (1.,1.,1.,1.)
	glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLightColor)
	glLightfv(GL_LIGHT0, GL_DIFFUSE,diffuseLightColor)
	glLightfv(GL_LIGHT0, GL_SPECULAR,specularLightColor)
	# material reflectance for each color channel
	diffuseObjectColor = (0.8,0.0,0.8,1.)
	specularObjectColor = (1.,0.,0.,1.)
	glMaterialfv(GL_FRONT,
	GL_AMBIENT_AND_DIFFUSE, diffuseObjectColor)
	# glMaterialfv(GL_FRONT, GL_SPECULAR, specularObjectColor)
	glPushMatrix()
	# glRotatef(ang,0,1,0) uncomment: rotate object
	# try to
	glColor3ub(0, 0, 255) # glColor*() is ignored if lighting is enabled
	# drawUnitCube_glVertex()
	#drawUnitCube_glDrawArray()
	drawUnitCube_glDrawElements()
	glPopMatrix()
	glDisable(GL_LIGHTING)'''

def render(ang):
	global gCamAng, gCamHeight,xn,zn,yn
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45, 1, 1,10)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(5*np.sin(gCamAng),gCamHeight,5*np.cos(gCamAng), 0,0,0, 0,1,0)
# draw global frame
	drawFrame()
	
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_RESCALE_NORMAL) # rescale normal vectors after transformation and before lighting to have unit length

# set light properties
	lightPos = (1.,2.,3.,1.)
	glLightfv(GL_LIGHT0, GL_POSITION,lightPos)
	ambientLightColor = (.1,.1,.1,1.)
	diffuseLightColor = (1.,1.,1.,1.)
	specularLightColor = (1.,1.,1.,1.)
	glLightfv(GL_LIGHT0, GL_AMBIENT,ambientLightColor)
	glLightfv(GL_LIGHT0, GL_DIFFUSE,diffuseLightColor)
	glLightfv(GL_LIGHT0, GL_SPECULAR,specularLightColor)
# ZYX Euler angles
	xang = np.radians(xn)
	yang = np.radians(yn)
	zang = np.radians(zn)
	M = np.identity(4)
	Rx = np.array([[1,0,0],
                       [0, np.cos(xang), -np.sin(xang)],
                       [0, np.sin(xang), np.cos(xang)]])
	Ry = np.array([[np.cos(yang), -np.sin(yang), 0],
                       [np.sin(yang), np.cos(yang), 0],
                       [0,0,1]])
	Rz = np.array([[np.cos(zang), -np.sin(zang), 0],
                       [np.sin(zang), np.cos(zang), 0],
                       [0,0,1]])
	M[:3,:3] = Ry @ Rx @ Rz
	glMultMatrixf(M.T)
##The same ZYX Euler angles with OpenGL functions
	#glRotate(30, 0,0,1)
	#glRotate(30, 0,1,0)
	#glRotate(ang, 1,0,0)
	glScalef(.5,.5,.5)
# draw cubes
	glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (.5,.5,.5,1.))
	drawUnitCube_glDrawArray()
	glTranslatef(1.5,0,0)
	glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (1.,0.,0.,1.))
	drawUnitCube_glDrawArray()
	glTranslatef(-1.5,1.5,0)
	glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.,1.,0.,1.))
	drawUnitCube_glDrawArray()
	glTranslatef(0,-1.5,1.5)
	glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.,0.,1.,1.))
	drawUnitCube_glDrawArray()
	glDisable(GL_LIGHTING)

def drawUnitCube_glDrawArray():
	global gVertexArraySeparate
	varr = gVertexArraySeparate
	glEnableClientState(GL_VERTEX_ARRAY)
	glEnableClientState(GL_NORMAL_ARRAY)
	glNormalPointer(GL_FLOAT, 6*varr.itemsize, varr)
	glVertexPointer(3, GL_FLOAT, 6*varr.itemsize, ctypes.c_void_p(varr.ctypes.data + 3*varr.itemsize))
	glDrawArrays(GL_TRIANGLES, 0, int(varr.size/6))

def drawFrame():
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


def key_callback(window, key, scancode, action, mods):
	global gCamAng, gCamHeight,xn,zn,yn
	if action==glfw.PRESS or action==glfw.REPEAT:
		if key==glfw.KEY_1:
			gCamAng += np.radians(-10)
		elif key==glfw.KEY_3:
			gCamAng += np.radians(10)
		elif key==glfw.KEY_2:
			gCamHeight += .1
		elif key==glfw.KEY_W:
			gCamHeight += -.1
		elif key==glfw.KEY_A:
			zn += 10
		elif key==glfw.KEY_Z:
			zn -= 10
		elif key==glfw.KEY_S:
			xn += 10
		elif key==glfw.KEY_X:
			xn -= 10
		elif key==glfw.KEY_D:
			yn += 10
		elif key==glfw.KEY_C:
			yn -= 10
		elif key==glfw.KEY_V:
			xn=0
			zn=0
			yn=0

gVertexArraySeparate = None
def main():
	global gVertexArraySeparate
	if not glfw.init():
		return
	window = glfw.create_window(640,640,'Lecture17', None,None)
	if not window:
		glfw.terminate()
		return
	glfw.make_context_current(window)
	glfw.set_key_callback(window, key_callback)
	glfw.swap_interval(1)
	gVertexArraySeparate = createVertexArraySeparate()
	count = 0
	while not glfw.window_should_close(window):
		glfw.poll_events()
		ang = count % 360
		render(ang)
		count += 1
		glfw.swap_buffers(window)
	
	glfw.terminate()



def createVertexAndIndexArrayIndexed():
        varr = np.array([
                normalized([1,1,-1]),
                [ 0.5, 0.5,-0.5],
                normalized([-1,1,-1]),
                [-0.5, 0.5,-0.5],
                normalized([-1,1,1]),
                [-0.5, 0.5, 0.5],
                normalized([1,1,1]),
                [ 0.5, 0.5, 0.5],
                normalized([1,-1,1]),
                [ 0.5,-0.5, 0.5],
                normalized([-1,-1,1]),
                [-0.5,-0.5, 0.5],
                normalized([-1,-1,-1]),
                [-0.5,-0.5,-0.5],
                normalized([1,-1,-1]),
                [ 0.5,-0.5,-0.5],
                ], 'float32')
        iarr = np.array([
                [0,1,2],
                [0,2,3],
                [4,5,6],
                [4,6,7],
                [3,2,5],
                [3,5,4],
                [7,6,1],
                [7,1,0],
                [2,1,6],
                [2,6,5],
                [0,3,4],
                [0,4,7],
                ])
        return varr, iarr
def l2norm(v):
        return np.sqrt(np.dot(v, v))
def normalized(v):
        l = l2norm(v)
        return 1/l * np.array(v)
def drawUnitCube_glDrawElements():
        global gVertexArrayIndexed, gIndexArray
        varr = gVertexArrayIndexed
        iarr = gIndexArray
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_NORMAL_ARRAY)
        glNormalPointer(GL_FLOAT, 6*varr.itemsize,varr)
        glVertexPointer(3, GL_FLOAT,6*varr.itemsize,ctypes.c_void_p(varr.ctypes.data +3*varr.itemsize))
        glDrawElements(GL_TRIANGLES, iarr.size,GL_UNSIGNED_INT, iarr)

gVertexArrayIndexed = None
gIndexArray = None

'''def main():
        global gVertexArraySeparate
        global gVertexArrayIndexed, gIndexArray

        if not glfw.init():
                        return
        window = glfw.create_window(640,640,'Lecture8', None,None)

        if not window:
                glfw.terminate()
                return
        glfw.make_context_current(window)
        glfw.set_key_callback(window, key_callback)
        glfw.swap_interval(1)
        gVertexArraySeparate = createVertexArraySeparate()
        gVertexArrayIndexed, gIndexArray = createVertexAndIndexArrayIndexed()
        count = 0
        while not glfw.window_should_close(window):
                glfw.poll_events()
                ang = count % 360
                render(ang)
                count += 1
                glfw.swap_buffers(window)
        glfw.terminate()'''
if __name__ == "__main__":
	main()
