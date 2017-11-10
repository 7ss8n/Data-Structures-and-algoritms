class GrayScaleImage:
    def __init__(self, nrows,ncols):
        self._width=nrows
        self._height=ncols
        self._matrix=[[0 for x in range(self._width)] \
            for y in range(self._height)]
    def width(self):
        return self._width
    def height(self):
        return self._height
    def clear(self,value):
        assert(value>=0 and value<=255),"value exceed the size[0-255]" 
        for i in range(self._width):
            for j in range(self._height):
                self._matrix[i][j]=value         
    def getitem(self,row,col):
        assert ((row< self._width) and (col<self.height)),"wrong width and height"
        return self._matrix[row][col]
    def setitem(self,row,col,value):
        assert ((row< self._width) and (col<self._height)),"wrong width and height"
        self._matrix[row][col]=value
matix=GrayScaleImage(4,4)
#print(matix.height())
#print(matix._matrix)
#matix.clear(3)
#print(matix._matrix)
matix.setitem(1,0,5)
matix.setitem(0,0,5)
matix.setitem(0,1,5)
matix.setitem(3,0,5)
print(matix._matrix)
