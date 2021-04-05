from psychopy import visual, core, event
#win.getMovieFrame(buffer='back') 
#create a window to draw in
myWin = visual.Window((600,600), allowGUI=False)

#INITIALISE SOME STIMULI
grating1 = visual.GratingStim(myWin, mask="circle",color=[1.0, 1.0, 1.0], opacity=1.0,size=(1.5, 1.5), sf=(7,0), ori=45)

grating2 = visual.GratingStim(myWin, mask="circle",color=[1.0, 1.0, 1.0],opacity=0.5,size=(1.5, 1.5), sf=(7,0), ori=135)

trialClock = core.Clock()
t = 0
while t < 20:  

    t = trialClock.getTime()

    grating1.setPhase(2*t)  
    grating1.draw()  #redraw it

    grating2.setPhase(2*t)  
    grating2.draw()  #redraw it

    myWin.flip()        
    #update the screen

    #handle key presses each frame
    for keys in event.getKeys():
        if keys in ['escape','q']:
            core.quit()
            #win.saveMovieFrames(fileName='some file.mp4')
