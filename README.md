# Simple_Evolutionary_Algorithm
<p>The code provided is used to build a simple Evolutionary Algorithm.</p>

<h3>Files:</h3>
<p>There are 3 Python files:<br>
<ul>
<li>Evolutionary_Algorithm.py that works as the main file</li>
<li>EA_Functions.py where you find all the functions and the steps needed</li>
<li>EA_Hyperparameters.py where you can change and play with numbers you like</li>
</ul></p>

<h3>Goal:</h3>
<p>The algorithm aims to generate arrays (called worms) of a given length containing in each position the length of the array itself. The number within the array are randomly generated within a given range. The algorithm tries to reduce the error - measured in terms of RMSE - between each number and the length of the worm. The algorithm has been built entirely from scratch to understand better how EAs are built and how they work.</p>

<h3>Examples:</h3>
<p>Let's suppose you want to create an array with length 5. The algorithm starts off creating a bunch of randomly generated arrays of length 5 (Initialization step). The numbers within the randomly generated arrays are in the range LOWEST_NUMBER - HIGHEST_NUMBER. The algorithm will then perform the typical EA steps in the following order: Selection, Recombination, Mutation, Termination. The algorithm ends when the error falls below a given threshold called TOLERANCE. As the example, <code>[5, 5, 5, 5, 5]</code> It is also possible to store and retrieve the best population found at that point in time. This allows us to start a new cycle with an already trained model.</p>
