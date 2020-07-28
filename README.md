# ConnectZ

This application plays out a Connect 4 style game by reading in a text file full of numbers, the first line of which
detailing the game's dimenions: i.e how tall the board is, how wide the ball is and, since it is Connect Z rather than Connect 4,
how many consecutive player turns are needed to win the game.

1. Summary of My Solution:

The program has a main method which pulls in the arguments used in the command line running of the game. In this case,
the arguments neededd to run the game is the name of a textfile which detail the dimensions and turns of a game.
The read_file method reads the text file and checks it for validity and legality, using the simiilarly named methods to 
do so. Once it has passed these methods, the game is played out using the run_game method. This takes the arrray of the
game's outcome and places it into a new 2Dimensional arrray, denoting the board depicted as a 2D board. While adding each 
turn of the gamme to the board, the program checks for winners repeatedly - whether vertical, horizontal or diagoonal. If a
winner is not found then either a draw or an incomplete game is returned. If a winner is found but the game still has turns
left to be added to the board, the program returns this too.

2. My Approach:

I used 2D arrayss to create the board and then made methods that count the consecutive player turns by looping through
the array multiplee times as aand when there have been enough turns for a winner to be possible i.e the same numberr of turns
as the winning tarrget foor the game.

3. What I found Challenging:

- This is the first Python script I have created so I did not have a great deal of time to get up to speed with
the Python conventions (I only had a couple of evenings due to working full time and being sick on two of the five allotted days). This includes classes which I did not feel was necessary for this app but was necessary in order 
to create a test class. So unfortunately, not test class exists but iin a real world application I would have written unit tests
for eevery method. Instead of this, I tested the program throughout by editing the inputted text file to ensure mmultiple
different games would play out and the correct response was outputed by the application.  
- The Diagonal Method was becomming an extremely complicated set of nested loops - I therefore went for using an iterator 
instead. Given more time II would like to improve this method without using an iterator.
- The multiple nested loops in the program also add to the time taken to run the application. Since the games would usually be 
short, this speedd would not usualy maatter. However, for larger games the application would take a lot longerr due to the
On^2 complexity of the program.
