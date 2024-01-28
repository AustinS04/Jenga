This is code I made for a solution to https://dmoj.ca/problem/cco04p5
The best I could do with it was solve 9/10 test cases, I am looking to figure out what I am missing from the 10th

This program includes a calculator for:
Center of gravity of a single layer
Center of gravity of the structure from layer n upwards
Convex hull of a layer

along with functions to remove a block and add a block at any position.

with these functions working together, a game or sequence of Jenga moves can be played, and each time a block is moved (taken out and placed on top), a calculation is made to see if the tower will stand.
