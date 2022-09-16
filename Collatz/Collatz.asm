	IN
	BRZ	big	#if input is zero, print zero and halt
	STO	a	
chk1	SUB	one	#checks if a is 1 yet
	BRZ	done
	LDA	a	#if a has not reached 1
print	OUT		#no other output instruction in code until 'done' bit
	STO	c	#c is a dummy variable used for next loop, 'a' can't be used as it is required to find 3a+1 if needed
	LDA	zero	
	STO	Q	#resets value of quotient to zero
sub	LDA	Q	#this loop checks if the number is even AND divides by two
	ADD	one
	STO	Q
	LDA	c
	SUB	two
	STO	c	
	BRZ	even
	BRP	sub	#if it goes negative, it must be odd
	LDA	a	#procedure if a is odd
	SUB	lim	#if a is bigger than 332, (3a+1) will be bigger than 999
	BRP	big
	LDA	a
	ADD	a
	ADD	a
	ADD	one
	STO	a
	BR	print	#3a+1 is never 1, so directly go to output it
even	LDA	Q
	STO	a
	BR	chk1
done	LDA	a	#when a has reached 1
	OUT	
	HLT
big	LDA	zero	#when overflow has occured
	OUT
	HLT
a	DAT	000
c	DAT	000
zero	DAT	000
one	DAT	001
two	DAT	002
Q	DAT	000
lim	DAT	332