import pydirectinput
import pyttsx3
import threading
import keyboard
import time

# Initialize the pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 200)

# asfewsfe

# Test the engine with a simple text
text = '''To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream—ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause—there's the respect
That makes calamity of so long life.
For who would bear the whips and scorns of time,
Th'oppressor's wrong, the proud man's contumely,
The pangs of dispriz'd love, the law's delay,
The insolence of office, and the spurns
That patient merit of th'unworthy takes,
When he himself might his quietus make
With a bare bodkin? Who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscovere'd country, from whose bourn
No traveller returns, puzzles the will,
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience doth make cowards of us all,
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry
And lose the name of action.'''.split()

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
              'r', 's', 't', 'v', 'w', 'x', 'y', 'z', ]


def letter_check(letter_to_check):
    if letter_to_check.lower() in consonants:
        return consonants.index(letter_to_check.lower())
    else:
        return False


def pause():
    time.sleep(3)
    print("program paused")
    keyboard.wait('p')
    print("Program resumed!")


def run_inputs(target_word):
    for letter in target_word:
        if letter_check(letter):
            if letter_check(letter) % 4 == 0:
                pydirectinput.keyDown("right")
                pydirectinput.keyUp("right")
            elif letter_check(letter) % 4 == 1:
                pydirectinput.keyDown("down")
                pydirectinput.keyUp("down")
            elif letter_check(letter) % 4 == 2:
                pydirectinput.keyDown("left")
                pydirectinput.keyUp("left")
            elif letter_check(letter) % 4 == 3:
                pydirectinput.keyDown("up")
                pydirectinput.keyUp("up")
        else:
            pydirectinput.keyDown("up")
            pydirectinput.keyUp("up")


for word in text:
    input_thread = threading.Thread(target=run_inputs, args=(word,))
    input_thread.start()

    engine.say(word)
    engine.runAndWait()
    input_thread.join()
    if keyboard.is_pressed('p'):
        print("pausing program")
        pause()