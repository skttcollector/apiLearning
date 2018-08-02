import maya.cmds as cmds
import maya.api.OpenMaya as om

sel = cmds.ls(sl=True)

xVec = om.MVector()
yVec = om.MVector(0, 1, 0)
zVec = om.MVector()

apos = cmds.xform(sel[0], ws=True, q=True, rp=True)
bpos = cmds.xform(sel[1], ws=True, q=True, rp=True)
a = om.MVector(apos[0], apos[1], apos[2])
b = om.MVector(bpos[0], bpos[1], bpos[2])
aimVec = b-a
xVec = aimVec.normal()
zVec = xVec^yVec

mList = [xVec[0], xVec[1], xVec[2], 0, yVec[0], yVec[1], yVec[2], 0, zVec[0], zVec[1], zVec[2], 0, apos[0], apos[1], apos[2], 1]
mat = om.MMatrix(mList)
xmat = om.MTransformationMatrix(mat)
rot = xmat.rotation(asQuaternion=False)

cmds.xform(sel[0], ws=True, ro=rot* 57.2958)

#TODO - deal with vaious orientations, rotationUp adn other up options