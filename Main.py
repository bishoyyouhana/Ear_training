#Created by the one and only, Bishoy Baher Elkomos Youhana

import os 
import winsound
import random
import string

#os.chdir(r"Ear_training")
#error handling goes here (incase it's needed), first error is winError 2- has to do with relative paths being unrelative after one use.

NoteNames = os.listdir(r"notes")
ChordNames = os.listdir(r"chords")

notesTrials =0
chordTrials = 0
notesCorrect = 0
chordsCorrect = 0

print("Alright lads listen, you are about to play the ultimate guitar Ear training game.")
print("Rules are simple, have fun and practice")
print("when interacting with the inteface use capital letters R C N")
print("when writing chord names, write the actual chord in capital and its type in small letters, WITHOUT SPACES e.g. Aminor")
print("Now I will play a note and a chord for you reference")
input("press enter to continue")

os.chdir(r"notes")
relativeNote = random.randint(0,35)
winsound.PlaySound(NoteNames[relativeNote],1)
print(NoteNames[relativeNote].strip(".wav"))
relativeNoteInput = input("press R to replay -- or press enter to move on ")
while relativeNoteInput== "R":
		winsound.PlaySound(NoteNames[relativeNote],winsound.SND_FILENAME)
		relativeNoteInput = input("press R to replay -- or press enter to move on ")

os.chdir("..")
os.chdir(r"chords")
relativeChord = random.randint(0,9)
winsound.PlaySound(ChordNames[relativeChord],winsound.SND_FILENAME)
print(ChordNames[relativeChord].strip(".wav"))
relativeChordInput = input("press R to replay -- or press enter to move on ")
while relativeChordInput== "R":
	winsound.PlaySound(ChordNames[relativeChord],winsound.SND_FILENAME)
	relativeChordInput = input("press R to replay -- or press enter to move on ")
os.chdir("..")

print("					LET'S DANCE  ")

choice = input("what do you want to practice chords (C) or notes (N)? Or are you too weak to practice (W)")

def playNotes():
	global notesTrials
	global notesCorrect
	integer = random.randint(0,35)
	winsound.PlaySound(NoteNames[integer],winsound.SND_FILENAME)
	x = input("press R to replay -- or enter your answer and press enter ")
	while x== "R":
		winsound.PlaySound(NoteNames[integer],winsound.SND_FILENAME)
		x = input("press R to replay -- or enter your answer and press enter ")
	if(x ==NoteNames[integer].strip(".wav")):
		notesTrials+=1
		notesCorrect+=1
		print("YOU GOT IT RIGHT!!")
	else:
		notesTrials+=1
		print("better luck next time, the answer was {}".format(NoteNames[integer].strip(".wav")))

def playChords():
	global chordsCorrect
	global chordTrials
	integer = random.randint(0,9)
	winsound.PlaySound(ChordNames[integer],winsound.SND_FILENAME)
	x = input("press R to replay -- or enter your answer and press enter ")
	while x== "R":
		winsound.PlaySound(ChordNames[integer],winsound.SND_FILENAME)
		x = input("press R to replay -- or enter your answer and press enter ")
	if(x ==ChordNames[integer].strip(".wav")):
		chordTrials+=1
		chordsCorrect+=1
		print("YOU GOT IT RIGHT!!")
	else:
		chordTrials+=1
		print("better luck next time, the answer was {}".format(ChordNames[integer].strip(".wav")))

while(choice != "W"):
	if(choice == "N"):
		os.chdir(r"notes")
		playNotes()
		choice = input("what do you want to practice chords (C) or notes (N)? Or are you too weak to practice (W)")
		os.chdir("..")

	elif(choice == "C"):
		os.chdir(r"chords")		
		playChords()
		choice = input("what do you want to practice chords (C) or notes (N)? Or are you too weak to practice (W)")
		os.chdir("..")

	else:
		print("Invalid Input - program will restart")
		choice = input("what do you want to practice chords (C) or notes (N)? Or are you too weak to practice (W)")


print("			You got {} out of {} chords correct".format(chordsCorrect, chordTrials))
print("			You got {} out of {} notes correct".format(notesCorrect, notesTrials))
print("                               HOPE YOU HAD FUN !!!!")		
