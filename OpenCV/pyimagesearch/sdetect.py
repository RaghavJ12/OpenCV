import cv2
import numpy.linalg as la
import numpy as np
import math



def quad(cnt2):
    img = cv2.imread("square.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ret, thresh = cv2.threshold(gray, 0,255,0)
    img1,contours,heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt1 = contours[0]
 
 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)

    if 0.3< ret<0.7:
        return("Parallelogram")
        
    elif 0< ret < 0.2:

            return("Rhombus")
     
    else:
       return("Quadrilateral")


    
    
def SortCorners(points):

    C=np.mean(points,axis=0)[0]
    angle=[]
    for i in range(len(points)):
        a=(points[i])[0]
        angle.append(math.atan2(a[1]-C[1],a[0]-C[0]))
    ID=np.argsort(angle)
    sorted_p=points[ID]
    return sorted_p

def FindAngle(a,b,c):

    ab=b-a
    ac=c-a
    dot=np.dot(ab, ac)
    norm_ab=la.norm(ab)
    norm_ac=la.norm(ac)
    angle=math.acos(dot/(norm_ac*norm_ab))*180/np.pi
    return angle


def IsSquare(vcti):
    angles=[]
    vct=SortCorners(vcti)
    s_vct=len(vct)
    for i in range (s_vct):
        angles.append(FindAngle((vct[i%s_vct])[0], (vct[(i-1)%s_vct])[0], (vct[(i+1)%s_vct])[0]))
    if 86<=angles[0]<=94 and 86<=angles[1]<=94 and 86<=angles[2]<=94:
        return True

class shapedetect:
	def __init__(self):
		pass

	def detect(self, c):
            shape = "unidentified"
#            peri = cv2.arcLength(c, True)
            epsilon = 0.035*cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c,epsilon,True)
            l=["triangle","square","pentagon","hexagon","septagon",]
            if 3<=len(approx)<=7:
                shape=l[len(approx)-3]
                if len(approx)==4:
                    if IsSquare(approx):
                        (x, y, w, h) = cv2.boundingRect(approx)
                        ar = w / float(h)
                        shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
                    else:
                        shape=quad(c)
            
            else:
                shape="circle"
            return shape
    