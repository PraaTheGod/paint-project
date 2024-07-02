import tkinter
from math import*
from pygame import *
from random import *
from pygame import font 
from tkinter import filedialog
tkinter.Tk().withdraw()
font.init()
init()
mixer.init()

display.set_caption("PONY PAINT !!")
icon=image.load("pygame photos/ponytitle.png")
display.set_icon(icon)

width,height=1400,800
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
myClock=time.Clock()
running=True

#backround
ponytheme=image.load("pygame photos/PONY THEME.png")
ponytitle=image.load("pygame photos/ponytitle12.png")
screen.blit(ponytheme,(0,0))
screen.blit(ponytitle,(10,18))

#rectTools
pencilRect=Rect(20,250,60,60)
eraserRect=Rect(90,250,60,60)
brushRect=Rect(160,250,60,60)
fillRect=Rect(230,250,60,60)
sprayRect=Rect(20,320,60,60)
lineRect=Rect(90,320,60,60)
frectRect=Rect(160,320,60,60)
rectRect=Rect(230,320,60,60)
fcircRect=Rect(20,390,60,60)
circRect=Rect(90,390,60,60)
eyedropRect=Rect(160,390,60,60)
fireworkRect=Rect(230,390,60,60)
nothingRect=Rect(0,0,0,0)
histrect=Rect(0,0,0,0)
whiteRect=Rect(22,252,56,56)

#restart,save,undo,redo rects
loadRect=Rect(399,613,55,55)
restartRect=Rect(399,671,55,55)
saveRect=Rect(427,729,55,55)
undoRect=Rect(457,613,55,55)
redoRect=Rect(457,671,55,55)

#Stamping
stampdescription=image.load("p/stampdescription.png")
musicdescription=image.load("p/music description.png")
arrowLeft=transform.scale(image.load("p/leftArrowicon.png"),(56,56))
arrowRight=transform.scale(image.load("p/arrowRighticon.png"),(56,56))
stampRect=Rect(520,613,300,150)
draw.rect(screen,WHITE,stampRect)
draw.rect(screen,"hot pink",stampRect,3)
leftStampRect=Rect(526,657,56,56)
rightStampRect=Rect(755,657,56,56)
screen.blit(arrowLeft,(526,657))
screen.blit(arrowRight,(755,657))

ponyRect=Rect(586,615,165,146)
poniesList=["p/yellowPony.png","p/purplePony.png","p/redPony.png","p/greenPony.png","p/pinkPony.png"]
ponyList=[]
for i in range(5):
    pony=transform.scale(image.load(poniesList[i]),(160,130))
    ponyList.append(pony)
screen.blit(ponyList[0],(586,621))
pos1=0
#Music
musicicon=image.load("p/musicicon.png")
screen.blit(musicicon,(1090,730))
MusicList=["p/ComeTogether.ogg","p/EquestriaGirls.ogg","p/FitRightIn.ogg","p/PerfectDay.ogg","p/StrangeWorld.ogg"]
repeat=image.load("p/repeat.png")
repeatgreen=image.load("p/repeatgreen.png")
shuffle=image.load("p/shuffle.png")
shufflegreen=image.load("p/shufflegreen.png")
pause=image.load("p/pause.png")
play=image.load("p/play.png")
musiclayout=(image.load("p/musiclayout.png"))
screen.blit(musiclayout,(910,640))
musiclayoutRect=Rect(910,640,422,59)
shuffleRect=Rect(1013,657,35,35)
backRect=Rect(1050,657,35,35)
pauseRect=Rect(1096,650,45,45)
nextRect=Rect(1150,657,35,35)
repeatRect=Rect(1190,657,35,35)
musicRects=[shuffleRect,backRect,pauseRect,nextRect,repeatRect]
draw.rect(screen,"hot pink",musiclayoutRect,2)
screen.blit(pause,(1095,653))

#canvas&border
everyRect=Rect(0,0,1400,800)
canvasRect=Rect(400,9,971,600)
outcanvasRect=Rect(399,8,973,602)
draw.rect(screen,WHITE,canvasRect)

#restart,save,undo,redo rects
draw.rect(screen,YELLOW,loadRect,2)
draw.rect(screen,YELLOW,restartRect,2)
draw.rect(screen,YELLOW,saveRect,2)
draw.rect(screen,YELLOW,undoRect,2)
draw.rect(screen,YELLOW,redoRect,2)

#current colour rectangle
currentRect=Rect(295,610,100,60)

#font
comicFont=font.SysFont("Eras Demi ITC",20)
titleFont=font.SysFont("Showcard Gothic",40)
font=font.SysFont("Agency FB",35)

#printing 'current\n colour'
curcol=comicFont.render("Current",True,BLACK)
curcols=comicFont.render("Colour",True,BLACK)
title=titleFont.render("PONY PAINT!",True,BLACK)
screen.blit(curcol,(305,666))
screen.blit(curcols,(310,684))
screen.blit(title,(36,200))

#image of colour wheel
colourwheel=image.load("colour wheel.jpg")
screen.blit(colourwheel,(15,613)) #creating colour wheel
colourRect=Rect(15,613,272,174)

#Border of colour wheel
bordercolRect=Rect(12,610,278,180)
draw.rect(screen,YELLOW,bordercolRect,3)

#starting tool,colour,size,mouse pointer
col=BLACK
omx,omy=0,0
size=10
tool="nothing"
soundcount=0
shuffleecount=0
repeattcount=0
songpos=0

#mylists
myTools= [ "pencil" , "eraser" , "brush" , "fill" , "spray" , "line" , "frect" , "rect" , "felip" ,"elipps", "eyedrop" , "firework" , "stamp", "nothing" ]
myRects= [pencilRect,eraserRect,brushRect,fillRect,sprayRect,lineRect,frectRect,rectRect,fcircRect,circRect,eyedropRect,fireworkRect,histrect,nothingRect]

#mypics
pos=0
picNames=["p/pencilicon.png","p/erasericon.png","p/paintbrush.png","p/bucket.png","p/spray can.png","p/line.png","p/fillrect.png","p/rectangle.png","p/fillellipse.png","p/ellipse.png","p/eyedropper.png"]
picList= []

#drawing icons
for i in range(len(picNames)):
    pic=image.load(picNames[i])    
    picList.append(pic)
for i in range(4):
    draw.rect(screen,"hot pink",(22+i*70,252,56,56))
    draw.rect(screen,"hot pink",(22+i*70,322,56,56))
    draw.rect(screen,"hot pink",(22+i*70,392,56,56))
    screen.blit(picList[i],(27+i*68,254))
for i in range(2):
    draw.rect(screen,"hot pink",(401,615+i*58,51,51))
    draw.rect(screen,"hot pink",(459,615+i*58,51,51))
    draw.rect(screen,"hot pink",(429,731,51,51))
#adjusting sizes of some icons
fillrect=transform.scale(image.load("p/fillrect.png"),(56,56))
rectangle=transform.scale(image.load("p/rectangle.png"),(50,50))
fillellipse=transform.scale(image.load("p/fillellipse.png"),(52,52))
ellipse=transform.scale(image.load("p/ellipse.png"),(52,52))
firework=transform.scale(image.load("p/fireworkicon.png"),(50,50))
picList.append(fillrect)
picList.append(rectangle)
picList.append(fillellipse)
picList.append(ellipse)
screen.blit(fillrect,(162,322))
screen.blit(rectangle,(235,325))
screen.blit(fillellipse,(24,395))
screen.blit(ellipse,(94,395))
screen.blit(firework,(235,395))
screen.blit(picList[10],(166,395))
screen.blit(picList[4],(18,319))
screen.blit(picList[5],(90,321))    
#extra
undoPic=transform.scale(image.load("p/undo.png"),(50,50))
redoPic=transform.scale(image.load("p/redo.png"),(50,50))
loadPic=transform.scale(image.load("p/loadicon.png"),(52,52))
savePic=transform.scale(image.load("p/save.png"),(52,52))
restartPic=transform.scale(image.load("p/restarticon.png"),(50,50))
screen.blit(loadPic,(399,614))
screen.blit(restartPic,(401,673))
screen.blit(savePic,(429,731))
screen.blit(undoPic,(459,614))
screen.blit(redoPic,(459,672))

#drawing descriptions
urlsr=[loadRect,restartRect,saveRect,undoRect,redoRect,nothingRect]
desNames=["p/pencil description.png","p/eraser description.png","p/paintbrush description.png","p/bucket description.png","p/spraypaint description.png","p/line description.png","p/filled rectangle description.png","p/rectangle description.png","p/filled ellipse description.png","p/ellipse description.png","p/eyedropper description.png","p/random tool description.png"]
des1Names=["p/load description.png","p/restart description.png","p/save description.png","p/undo description.png","p/redo description.png"]
#undo
undolist=[screen.subsurface(canvasRect).copy()]#Makes sure that a picture of the canvas will be in the list
undopos=0

while running:
    click=False
    for evt in event.get():
        if evt.type==QUIT:
            running=False
            
        if evt.type==MOUSEBUTTONUP:
            if canvasRect.collidepoint(mx,my):
                if undopos<len(undolist)-1: #Checks if list is empty
                    del undolist[undopos+1:]
                undolist+=[screen.subsurface(canvasRect).copy()]
                undopos+=1 #Adds to the undopos to keep track

        if evt.type==MOUSEBUTTONDOWN:
            click=True
            sx,sy=evt.pos #The click position
            back=screen.subsurface(canvasRect).copy() #A copy of the canvas is being made everytime the mouse is clicked

            if evt.button==4: #Scrolling for bigger size
                size+=1
                if size>200:
                    size=200
            if evt.button==5: #Scrolling for smaller size
                size-=1
                if size<1:
                    size=1
                
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    keys=key.get_pressed()

#drawing border
    draw.rect(screen,BLACK,outcanvasRect,1)

#Music
    mixer.music.get_busy=False

    if click and pauseRect.collidepoint(mx,my):
        mixer.music.get_busy==True
        soundcount+=1
        if soundcount%2==1:
            screen.blit(play,(1096,652))
            mixer.music.load(MusicList[songpos])            
            mixer.music.play()
            if mixer.music.get_busy==False:
                songpos=(songpos+1)%len(MusicList)
                mixer.music.load(MusicList[songpos])
                mixer.music.play()
        elif soundcount%2==0:
            screen.blit(pause,(1095,653))
            mixer.music.stop()

                
    if click and repeatRect.collidepoint(mx,my):
        repeattcount+=1
        print(repeattcount)
        if repeattcount%2==1:
            screen.blit(repeatgreen,(1183,656))
        elif repeattcount%2==0:
            screen.blit(repeat,(1184,649))

            
    if click and nextRect.collidepoint(mx,my):
        if repeattcount%2==1:
            songPos=(songpos+1)%len(MusicList)
            mixer.music.load(MusicList[songPos])
            mixer.music.play()
        else:
            songpos=(songpos+1)%len(MusicList)
            mixer.music.load(MusicList[songpos])
            mixer.music.play()
        
    if click and backRect.collidepoint(mx,my):
        songpos=(songpos-1+len(MusicList))%len(MusicList)        
        mixer.music.load(MusicList[songpos])
        mixer.music.play()
    if musiclayoutRect.collidepoint(mx,my):
        screen.blit(musicdescription,(20,470))
        
                    




#Stamps    
    if click and leftStampRect.collidepoint(mx,my):
        draw.rect(screen,RED,leftStampRect,2)
        pos1=(pos1-1)%len(ponyList)
        draw.rect(screen,WHITE,ponyRect)
        screen.blit(ponyList[pos1],(586,621))        
    else:
        draw.rect(screen,WHITE,leftStampRect,2)
        
    if click and rightStampRect.collidepoint(mx,my):
        draw.rect(screen,RED,rightStampRect,2)
        pos1=(pos1+1)%len(ponyList)
        draw.rect(screen,WHITE,ponyRect)
        screen.blit(ponyList[pos1],(586,621))
    else:
        draw.rect(screen,WHITE,rightStampRect,2)
    for i in range(5):
        if ponyRect.collidepoint(mx,my) and mb[0]:
            tool="stamp"
            currentstamp=(ponyList[pos1])
    if mb[0] and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect) #This is to not make any stamps outside the canvas.
        if currentstamp==ponyList[0]:
            screen.blit(back,canvasRect) #This is to make it an actual "stamp". #Without blitting it, it will make a trail of the picture selected
            screen.blit(ponyList[0],(mx-(ponyList[0]).get_width()/2,my-(ponyList[0]).get_height()/2)) #This is to get the mouse cursor in the middle of the picture when using the stamp
        if currentstamp==ponyList[1]:
            screen.blit(back,canvasRect)
            screen.blit(ponyList[1],(mx-(ponyList[1]).get_width()/2,my-(ponyList[1]).get_height()/2))
        if currentstamp==ponyList[2]:
            screen.blit(back,canvasRect)
            screen.blit(ponyList[2],(mx-(ponyList[2]).get_width()/2,my-(ponyList[2]).get_height()/2))
        if currentstamp==ponyList[3]:
            screen.blit(back,canvasRect)
            screen.blit(ponyList[3],(mx-(ponyList[3]).get_width()/2,my-(ponyList[3]).get_height()/2))
        if currentstamp==ponyList[4]:
            screen.blit(back,canvasRect)
            screen.blit(ponyList[4],(mx-(ponyList[4]).get_width()/2,my-(ponyList[4]).get_height()/2))
        screen.set_clip(None)
    if mb[0] and ponyRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,ponyRect,1)
    elif ponyRect.collidepoint(mx,my):
        draw.rect(screen,RED,ponyRect,1)
    else:
        draw.rect(screen,"hot pink",ponyRect,1)
    
        
                
        
#blitting descriptions    
    if tool=="pencil":
        pencildescription=image.load("p/pencil description.png")
        screen.blit(pencildescription,(20,470))
        draw.rect(screen,BLACK,(20,470,346,121),3)
    for i in range(len(desNames)): 
        if myRects[i].collidepoint(mx,my) and mb[0]:
            descrip=image.load(desNames[i])
            screen.blit(descrip,(20,470))
            draw.rect(screen,BLACK,(20,470,346,121),3)
    for i in range(len(des1Names)):
        if urlsr[i].collidepoint(mx,my):
            descript=image.load(des1Names[i])
            screen.blit(descript,(20,470))
            draw.rect(screen,BLACK,(20,470,346,121),3)
            draw.rect(screen,RED,urlsr[i],2)
        else:
            draw.rect(screen,YELLOW,urlsr[i],2)
    if stampRect.collidepoint(mx,my):
        screen.blit(stampdescription,(20,470))
    
            
#selecting the tool    
    for i in range(len(myRects)):
        draw.rect(screen,GREEN,myRects[myTools.index(tool)],2)#when tool is selected it will draw a green rect on the selected tool
        if myRects[i].collidepoint(mx,my) and mb[0]:
            tool=myTools[i]
            currentstamp=()
        elif myRects[i].collidepoint(mx,my):
            draw.rect(screen,RED,myRects[i],2)
        else:
            draw.rect(screen,YELLOW,myRects[i],2)


#using the tool
    screen.set_clip(canvasRect)#only the canvas gets updated
    
    if mb[0] and canvasRect.collidepoint(mx,my):
        if tool=="pencil":
            draw.line(screen,col,(mx,my),(omx,omy))            
        if tool=="eraser":
            x=mx-omx
            y=my-omy
            d=hypot(x,y) #finding distance between x and y

            if d==0:
                d=1

            for i in range(int(d)):
                dx=int(omx+i/d*x) #This ratio will get every pixel on the line with endpoints being omx,omy and mx,my
                dy=int(omy+i/d*y)
                draw.circle(screen,(255,255,255),(dx,dy),size)
        if tool=="brush":
            x=mx-omx #This finds delta x and delta y
            y=my-omy
            d=hypot(x,y)
            if d==0:
                d=1
            for i in range(int(d)):
                dx=int(omx+i/d*x) #This ratio will get every pixel on the line with endpoints being omx,omy and mx,my
                dy=int(omy+i/d*y)
                draw.circle(screen,col,(dx,dy),size)
        
        if tool=="eyedrop":
            col=screen.get_at((mx,my))
        if tool=="fill":
            screen.fill(col)
        if tool=="spray":
            for i in range(15): #Putting it in a for loop makes it spray faster
                spray_x=randint(-1*size,size) #range of the spray from the current size
                spray_y=randint(-1*size,size)
                if spray_x**2+spray_y**2<=size**2: #Equation of a circle to find the points to draw on the circle. Also since it is "<=size", it can lie on the circle border itself too
                        draw.circle(screen,col,(mx+spray_x,my+spray_y),1)
        if tool=="line":
            screen.blit(back,canvasRect)
            draw.line(screen,col,(sx,sy),(mx,my),size)
        if tool=="frect":
            screen.blit(back,canvasRect)
            rect=Rect(sx,sy,mx-sx,my-sy)
            rect.normalize()
            draw.rect(screen,col,rect)
        if tool=="rect":
            screen.blit(back,canvasRect)
            rect=Rect(sx,sy,mx-sx,my-sy)
            rect.normalize()
            draw.rect(screen,col,rect,size)
        if tool=="felip":
            screen.blit(back,canvasRect)
            if keys[K_LSHIFT] or keys[K_RSHIFT]:
                dist = ((mx-sx)**2+(my-sy)**2)**0.5
                draw.circle(screen,col,(sx,sy),dist)
            else:
                if mx<sx and my<sy:
                    topL=(mx,my)
                elif mx>sx and my<sy:
                    topL=(sx,my)                    
                elif mx<sx and my>sy:
                    topL=(mx,sy)
                else:
                    topL=(sx,sy)
                draw.ellipse(screen,col,(topL[0],topL[1],abs(mx-sx),abs(my-sy)))
        if tool=="elipps":
            screen.blit(back,canvasRect)
            if keys[K_LSHIFT] or keys[K_RSHIFT]:
                dist = ((mx-sx)**2+(my-sy)**2)**0.5
                draw.circle(screen,col,(sx,sy),dist,size)
            else:
                if mx<sx and my<sy:
                    topL=(mx,my)
                elif mx>sx and my<sy:
                    topL=(sx,my)                    
                elif mx<sx and my>sy:
                    topL=(mx,sy)
                else:
                    topL=(sx,sy)
                draw.ellipse(screen,col,(topL[0],topL[1],abs(mx-sx),abs(my-sy)),size) 
        if tool=="firework":
            for x in range(0,80): #Putting it in a for loop makes it run faster

                xrange=randint(mx-1*size,mx+size) #Range of the rect that the tool draws lines from
                yrange=randint(my-1*size,my+size)

                randcol=(randint(0,255),randint(0,255),randint(0,255)) #This will be a random colour each time.

                draw.line(screen,randcol,(mx,my),(xrange,yrange),1) #Draws random coloured lines from the mouse's position to how big the range will be.
        if tool=="stamp":
            ()
    screen.set_clip(None)

#getting colour when u click on colour pallette
    if mb[0] and colourRect.collidepoint(mx,my):
        draw.rect(screen,WHITE,bordercolRect,3)
        col=screen.get_at((mx,my))        
        screen.set_clip(colourRect)
        screen.blit(colourwheel,(15,613))
        draw.rect(screen,BLACK,(mx-5,my-5,10,10),1)#Black box that is set wherever the user selected colour from last
        screen.set_clip(None)
    else:
        draw.rect(screen,YELLOW,bordercolRect,3)
    draw.rect(screen,col,currentRect)
    draw.rect(screen,YELLOW,currentRect,2)

    #Tools that are not used on the canvas
    if  click and undoRect.collidepoint(mx,my):
          if len(undolist)-1>0: #Checks if the list is empty or not
            undopos-=1 #Subtracts from the counter to get the right position
            screen.blit(undolist[undopos],(400,9)) #Blits the capture
          if undopos<=1:
            screen.blit(undolist[undopos],(400,9))
            undopos=1 #Sets a restriction so that the index doesn't go out of range

    if click and redoRect.collidepoint(mx,my):
        if len(undolist)-1>0:#Checks if the list is empty or not
            if undopos>=len(undolist)-1: #Makes sure the index isn't out of range
                    screen.blit(undolist[undopos],(400,9))
            else:
                undopos+=1
                screen.blit(undolist[undopos],(400,9))
    if mb[0] and redoRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,redoRect,2)

    if mb[0] and saveRect.collidepoint(mx,my): #saving the canvas
        draw.rect(screen,GREEN,saveRect,2)
        try:
            fname=filedialog.asksaveasfilename(defaultextension=".png")
            image.save(screen.subsurface(canvasRect),fname)
        except:
            pass
            print("Error")
    if mb[0] and loadRect.collidepoint(mx,my): #Loading an image
        draw.rect(screen,GREEN,loadRect,2)
        try: #Try will see if the program can do the command because tkinter likes to crash on certain computers.
            fname=filedialog.askopenfilename(filetypes=[("images","*.png;*.jpg;*.jpeg")])#This will create a window so the user can choose what type of file they can pick and what file to load.
            loadpic=image.load(fname)                #This will load the image
            loadpicwidth = loadpic.get_width()  #getting width and height of image
            loadpicheight = loadpic.get_height()
            if loadpicwidth>canvasRect.width:
                if loadpicheight>canvasRect.height:    
                    loadpic=transform.scale(loadpic,(971,600))#scale it down to fit the canvas
                else:
                    loadpic=transform.scale(loadpic,(971,loadpicheight))
            else:
                if loadpicheight>canvasRect.height:    
                    loadpic=transform.scale(loadpic,(loadpicwidth,600))#scale it down to fit the canvas
            screen.blit(loadpic,(400,9))#Blits the load image
        except: #If it doesn't work it will simply let it go and not crash the program
            pass
    if mb[0] and restartRect.collidepoint(mx,my):
        draw.rect(screen,GREEN,restartRect,2)
        draw.rect(screen,WHITE,canvasRect) #draws a blank canvas

    #Displaying Text
    if canvasRect.collidepoint(mx,my):  #The canvas rect is at(400,9), so the coords have to subtracted to get the coords of the mouse inside the canvas
        cordt=font.render("X:%d  Y:%d"%(mx-400,my-9),True,(0,0,0))#While mouse is in the canvas
    else:
        cordt=font.render("X:---  Y:---",True,(0,0,0))#While mouse is not in the canvas
    size_text=font.render("Size:%d"%(size),True,(0,0,0)) #Displays the size on the screen
    screen.blit(ponytheme.subsurface((255,10,144,80)),(255,10))#This is so that the coords dont get overlapped by eachother when they change
    screen.blit(cordt,(255,10)) # Current Coords on the canavs
    screen.blit(size_text,(255,50))#Current Size

    omx,omy=mx,my#getting the previous mouse position
    myClock.tick(60)
    display.flip()
            
quit()
