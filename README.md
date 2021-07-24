# Cryptanalysis-of-DryGASCON

The folder "Modes" consists of our cvc files to search for particular differential characteristics, which are used to construct collisions of DryGASCON128.

After installing STP solver, input the order: stp filename.cvc > resultname.txt.
And obtain results.
If there are many results, STP solver only returns one of them.
For obtaining all possible results, we need to adjust the model step by step and collect the result one by one.

Details about how to use STP, please refer to https://stp.github.io/.
