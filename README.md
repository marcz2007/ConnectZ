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

4. To run this command line program, simply put a text file into the project folder and run the application using the name of the text file without the '.txt' part of thee filename. The following printed codes are shown based on the game dynamics:

0 Draw This happens when every possible space in the frame was filled with
a counter, but neither player achieved a line of the required length.

1 Win for player 1 The first player achieved a line of the required length.
2 Win for player 2 The second player achieved a line of the required length.
3 Incomplete The file conforms to the format and contains only legal moves, but
the game is neither won nor drawn by either player and there are
remaining available moves in the frame. Note that a file with only a
dimensions line constitues an incomplete game.

4 Illegal continue All moves are valid in all other respects but the game has already
been won on a previous turn so continued play is considered an
illegal move.

5 Illegal row The file conforms to the format and all moves are for legal columns
but the move is for a column that is already full due to previous
moves.

6 Illegal column The file conforms to the format but contains a move for a column
that is out side the dimensions of the board. i.e. the column selected
is greater than X

7 Illegal game The file conforms to the format but the dimensions describe a game

that can never be won.

8 Invalid file The file is opened but does not conform the format.
9 File error The file can not be found, opened or read for some reason.

