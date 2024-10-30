import maya.cmds as cmds # type: ignore

size = float(3)
percentage = float(0.85)

cmds.polySphere (radius=size, subdivisionsX= 20, subdivisionsY=20, axis= (0,1,0), createUVs= 2, constructionHistory = True)
cmds.move (0,size, 0, relative= True, objectSpace=True, worldSpaceDistance=False)
cmds.polySphere (radius=(size-1), subdivisionsX= 20, subdivisionsY=20, axis= (0,1,0), createUVs= 2, constructionHistory = True)
cmds.move(0, percentage * ((size * 2) + (size - 1)), 0, r=True, os=True, wd=True)
cmds.polySphere(r=size - 2, sx=20, sy=20, ax=(0, 1, 0), cuv=2, ch=1)
cmds.move(0, percentage * ((size * 2) + ((size - 1) * 2) + (size - 2)), 0, r=True, os=True, wd=True)
