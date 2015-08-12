#!/usr/bin/python
# -*- coding: utf-8 -*-

import random , numpy , argparse , sys , os
from PIL import Image , ImageDraw
from scipy.misc import comb


def banner() :
   screen = getTerminalSize()
   screen_height = screen[0]
   screen_width = screen[1]
   banner_ascii = [" __  .    _        _  ,            ,    ",
                   "/  ` |_  '_|  _   (  -+- * \  / * -+-   .",
                   "\__. [ ) (_] (_) _)   |  |  \/  |  |  \_|",
                   "                                      ._|",
                   "                                      ",
                   "Chaostivity/0.1",
                   "by geolado | g3ol4d0"]

   print("_"*screen_width)    
   for line in banner_ascii :
      print(line.center(screen_width))    
   print("_"*screen_width)

def getTerminalSize():

    line = os.popen('stty size', 'r').read().split()
    line = map(int , line)

    return line 

def progress( width , percent ) :
      screen = getTerminalSize()
      screen_height = screen[0]
      screen_width = screen[1]
      center_width = screen[1]
      actual_percent = percent
      width_percent = actual_percent*(screen_width-11)/100
      fill = (screen_width-11)*"."
      fill = fill.replace(".","#",width_percent)
      sys.stdout.write("\r[i] [{0}] {1}%".format( fill , actual_percent ))
      sys.stdout.flush()

def b3z13r_p( i , n , t ) :
	'''
	B3z13r p0lyn0m1um 'n sh1t
	'''
	return comb(n, i) * ( t**(n-i) ) * (1 - t) ** i

def b3z13r( p , nt = 10000) :
	'''
	http://incolumitas.com/2013/10/06/plotting-bezier-curves/
	'''
	np = len(p)
	xp = numpy.array( [ pl[0] for pl in p ] )
	yp = numpy.array( [ pl[1] for pl in p ] )

	t = numpy.linspace(0.0, 1.0, nt)

	p0ly_4rr4y = numpy.array([ b3z13r_p(i, np-1, t) for i in range(0, np) ])

	xs = numpy.dot(xp, p0ly_4rr4y)
	ys = numpy.dot(yp, p0ly_4rr4y)

	return xs, ys

def main(args) :
	c4l31d0 = Image.new("RGB" , (1240 , 1754) , "white" )
	draw = ImageDraw.Draw(c4l31d0)
	color = (255*int(args.alpha))/100
	print "[i] Color = "+str(color)
	screen_size = getTerminalSize()

	print "[i] Drawing lines ..."

	for q in xrange(int(args.density)) :
		x0,y0 = random.randint(1,1239),random.randint(1,1753)
		x1,y1 = random.randint(1,1239),random.randint(1,1753)

		draw.line( (x0,y0,x1,y1) , fill=(color,color,color) )

		c1_x,c1_y, = random.randint(1,1239),random.randint(1,1753)
		c2_x,c2_y = random.randint(1,1239),random.randint(1,1753)
		c3_x,c3_y = random.randint(1,1239),random.randint(1,1753)

		curv3_x , curv3_y = b3z13r([[c1_x,c1_y] , [c2_x ,c2_y] , [c3_x,c3_y] ])

		for i in xrange(10000) :
			c4l31d0.putpixel((int(curv3_x[i]) , int(curv3_y[i])) , (color,color,color) )

		progress(screen_size,(100*q)/500)	

	try :
		c4l31d0.save(args.filename+'.png')
		print "\n[i] "+args.filename+".png Saved (:"
		c4l31d0.show()
	except :
		print "[!] Error saving the image"

if __name__ == '__main__':

	banner()
	
	parser = argparse.ArgumentParser(description='Make random images.')
	parser.add_argument('--output' , '-o' , dest='filename' , default="pareidolia" , help='filename')
	parser.add_argument('--transparency' , '-t' , dest='alpha' , default="80" , help='percentage (0-100)')
	parser.add_argument('--density' , '-d' , dest='density' , default="100" , help='line\'s amount percentage (0-100)')
	args = parser.parse_args()

	main(args)