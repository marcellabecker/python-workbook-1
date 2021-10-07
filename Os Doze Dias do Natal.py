#! /usr/bin/env python3
def displayVerse(m):
	print("One the ",m, "day of christmas")
	print("my true love sent to me:")
	if(m>=12):
		print("Twelve drummers drumming,")
	if(m>=11):
		print("eleve pipers piping,")
	if(m>=10):
		print("ten lods a leaping",)
	if(m>=9):
		print("nine laids dancing,")
	if(m>=8):
		print("eight maids a milking,")
	if(m>=7):
		print("seven swans a swimming,")
	if(m>=6):
		print("six geese a laying,")
	if(m>=5):
		print("five golden rings,")
	if(m>=4):
		print("four calling birds,")
	if(m>=3):
		print("three french hens,")
	if(m>=2):
		print("two turtle doves,")
	if(m==1):
		print("A", end=" ")
	else:
		print("and a", end=" ")
	print("partridge in a pear tree.")
	print()
def main():
	for verse in range(1, 13):
		displayVerse(verse)
main()