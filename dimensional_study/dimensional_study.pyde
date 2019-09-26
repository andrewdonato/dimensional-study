numberOfLayers = 10
rgbColor=250
layers = []


def setup():
    ## "numberOfLayers" is not needed as a global for some reason
    global rgbColor #, numberOfLayers
    
    # size(700, 500, P3D)
    size(1000, 700, P3D)
    noFill()
    strokeWeight(5)
    background(0)
    
    # roughDraft()
    


def draw():
    global layers, rgbColor, numberOfLayers
    ## need generateLayers method that adds layers and then tells them to create themselves
    
    layers = generateLayers()
    populateLayers()
    print layers

def populateLayers() :
    global layers, rgbColor, numberOfLayers    
    for i in layers:
        layer = Layer(i)
        pushMatrix()        
        stroke(rgbColor,0,0, 125)
        rectMode(CENTER)
        rect (width/2,height/2,100,100)
        rgbColor += -10
        translate(-10, -10, -10)
        popMatrix()
    
    

def generateLayers():
    global layers, numberOfLayers, rgbColor    
    
    while len(layers) < numberOfLayers :
        for i in range(numberOfLayers) :
            layers.append([])
        # print layers
    return layers
    
def roughDraft():
    global rgbColor, numberOfLayers
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
    

class Layer():
    def __init__(self, layerIndex):
    # def __init__(self, layerIndex, layerX, layerY, layerZ, layerLevelDepth=0):        
        self.i = layerIndex
        # self.x = layerX
        # self.y = layerY
        # self.z = layerZ
        # self.depth = layerLevelDepth
        self.inventory = []

    def display(self):
        rect(self.x, self.y,  100,  100)
