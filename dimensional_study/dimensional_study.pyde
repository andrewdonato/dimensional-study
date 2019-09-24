numberOfLayers = 10
rgbColor=250

def setup():
    # size(700, 500, P3D)
    size(1000, 700, P3D)
    # translate(58, 48, 0)
    # translate(290, 240, 0)


   
# def draw():
    ## "numberOfLayers" is not needed as a global for some reason
    global rgbColor #, numberOfLayers
    
    # rotateY(0.5)
    noFill()
    strokeWeight(5)
    # box(40, 20, 50)
    
    # translate(100, 100, 0)
    # stroke(255,0,0)
    # rect (0,0,100,100)
    
    # translate(100, 100, 0)
    # stroke(0,255,0)
    # rect (0,0,100,100)
    
    rgbDelta = rgbColor/numberOfLayers
    if width <= height:
        positionDelta = (width*0.8)/numberOfLayers
    else:
        positionDelta = (height*0.8)/numberOfLayers
    
    print numberOfLayers  ## why dont I need to call this as a global?
    print rgbColor
    print rgbDelta
    
    
    ## need to merge these below on refactor
    ## lets create a layer class
    pushMatrix()
    for i in range(numberOfLayers):         
        stroke(rgbColor,0,0, 125)
        rectMode(CENTER)
        rect (width/2,height/2,100,100)
        rgbColor += -rgbDelta
        translate(-positionDelta, -positionDelta, -positionDelta)
    popMatrix()
    
    pushMatrix()
    rgbColor = 250
    for i in range(numberOfLayers):
        stroke(0,rgbColor,0, 125)
        rectMode(CENTER)
        rect (width/2,height/2,100,100)
        rgbColor += -rgbDelta
        translate(positionDelta, -positionDelta, -positionDelta) 
    popMatrix()
    
    pushMatrix()
    rgbColor = 250
    for i in range(numberOfLayers):
        stroke(0,0,rgbColor, 125)
        rectMode(CENTER)
        rect (width/2,height/2,100,100)
        rgbColor += -rgbDelta
        translate(-positionDelta, positionDelta, -positionDelta) 
    popMatrix()
    
    pushMatrix()
    rgbColor = 250
    for i in range(numberOfLayers):
        stroke(rgbColor, 125)
        rectMode(CENTER)
        rect (width/2,height/2,100,100)
        rgbColor += -rgbDelta
        translate(positionDelta, positionDelta, -positionDelta) 


def keyReleased():
    global numberOfLayers

    if key == "=" or key == "+" :      
        numberOfLayers += 1
    elif key == "-" or key == "_" :
        if numberOfLayers > 1 :       
            numberOfLayers -= 1
    else:
        pass
    print "Key is " + str(key)

def draw():
    ## need generateLayers method that adds layers and then tells them to create themselves
    pass
