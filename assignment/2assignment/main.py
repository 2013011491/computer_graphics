import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

gCamAng = 0.
gCamHeight = 1.
count=1
angle = 180
check =0

def drawCube():
    glBegin(GL_QUADS)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)

    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0,-1.0)

    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)

    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glEnd()

# draw a sphere of radius 1, centered at the origin.
# numLats: number of latitude segments (horizontal)
# numLongs: number of longitude segments (horizontal)
def drawSphere(numLats=12, numLongs=12):
    for i in range(0, numLats + 1):
        lat0 = np.pi * (-0.5 + float(float(i - 1) / float(numLats)))
        z0 = np.sin(lat0)
        zr0 = np.cos(lat0)

        lat1 = np.pi * (-0.5 + float(float(i) / float(numLats)))
        z1 = np.sin(lat1)
        zr1 = np.cos(lat1)
        
        # Use Quad strips to draw the sphere
        glBegin(GL_QUAD_STRIP)

        for j in range(0, numLongs + 1):
            lng = 2 * np.pi * float(float(j - 1) / float(numLongs))
            x = np.cos(lng)
            y = np.sin(lng)
            glVertex3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr1, y * zr1, z1)

        glEnd()

def drawCylinder(numLats=12, numLongs=12) :
    for i in range(0, numLats + 1):
        lat0 = np.pi * (-0.5 + float(float(i - 1) / float(numLats)))
        z0 = np.sin(lat0)

        lat1 = np.pi * (-0.5 + float(float(i) / float(numLats)))
        z1 = np.sin(lat1)
        
        # Use Quad strips to draw the cylinder
        glBegin(GL_QUAD_STRIP)

        for j in range(0, numLongs + 1):
            lng = 2 * np.pi * float(float(j - 1) / float(numLongs))
            x = np.cos(lng)
            y = np.sin(lng)
            glVertex3f(x , z0, y)
            glVertex3f(x , z1, y)

        glEnd()


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

def render():
    global count
    global angle
    global check
    if check == 0 :
        if angle == 150 :
            check = -1
            angle+=1
        else : angle-=1
    else :
        if angle == 210 :
            check = 0
            angle-=1
        else : angle+=1
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
    glViewport(100,100,400,400)
    glLoadIdentity()
    glPushMatrix()
    
    gluPerspective(45,1,1,10)
    gluLookAt(5*np.sin(gCamAng),gCamHeight,5*np.cos(gCamAng), 0,0,0, 0,1,0)

    drawFrame()
    glTranslate(count/1000,0,0)
    glPushMatrix()
    
    glColor3ub(255, 255, 255)
    #drawing head
    glTranslate(0,1.5,0)
    glScale(0.2,0.2,0.2)
    drawSphere()
    glPopMatrix()

    #drawing body
    glPushMatrix()
    glTranslate(0,0.8,0)
    glScale(0.2,0.5,0.4)
    drawCube()
    glPopMatrix()
        
    #drawing leg
    #leg common loca
    glPushMatrix()
    glTranslate(0,.2,0)
    glPushMatrix()
    #right_leg
    glTranslate(0,0,0.2)
    glPushMatrix()
    glScale(0.15,0.15,0.15)
    drawSphere()
    glPopMatrix()
    glRotatef(-angle,0,0,1)
    glTranslate(0,0.4,0)
    glScale(0.15,0.5,0.15)
    drawCylinder()
    glPopMatrix()
    #left_leg
    glTranslate(0,0,-0.2)
    glPushMatrix()
    glScale(0.15,0.15,0.15)
    drawSphere()
    glPopMatrix()
    glRotatef(angle,0,0,1)
    glTranslate(0,0.4,0)
    glScale(0.15,0.5,0.15)
    drawCylinder()
    glPopMatrix()
    
    #drawing arm
    glPushMatrix()
    glTranslate(0,1.1,0)
    glPushMatrix()
    
    glTranslate(0,0,0.55)
    glPushMatrix()
    glScale(0.15,0.15,0.15)
    drawSphere()
    glPopMatrix()
    glRotatef(angle,0,0,1)
    glTranslate(0,0.3,0)
    glScale(0.15,0.3,0.15)
    drawCylinder()
    glPopMatrix()
    
    glTranslate(0,0,-0.55)
    glPushMatrix()
    glScale(0.15,0.15,0.15)
    drawSphere()
    glPopMatrix()
    glRotatef(-angle,0,0,1)
    glTranslate(0,0.3,0)
    glScale(0.15,0.3,0.15)
    drawCylinder()
    glPopMatrix()

    glPopMatrix()
        
def key_callback(window, key, scancode, action,mods):
	global gCamAng, gCamHeight
	if action==glfw.PRESS or action==glfw.REPEAT:
		if key==glfw.KEY_1:
			gCamAng += np.radians(-10)
		elif key==glfw.KEY_3:
			gCamAng += np.radians(10)
		elif key==glfw.KEY_2:
			gCamHeight += .1
		elif key==glfw.KEY_W:
			gCamHeight += -.1

def main():
    global count
    if not glfw.init():
        return
    window = glfw.create_window(640,640,'2013011491',None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    while not glfw.window_should_close(window):
        glfw.poll_events()
        count +=1
        if count==1000:
            count =1
        render()
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__":
	main() 
