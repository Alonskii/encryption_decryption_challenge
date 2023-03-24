# encryption_decryption_challenge
This is a task about writing the decryption function of the 101compute.net challenge. 


The actual code started from line 35, as line 1 to 32 which comprises mostly of the encryption part was provided on the website. 

First, I used the timer to slow down the execution of the program for 5 seconds, as it had just finished encrypting. 

Then I created a variable 'ciphertext' which takes an a text that has to be decrypted as an input. 
I also created the 'key' variable  which takes integer as an input, and then key must tally with the text to be decryped, as the text to be decrypted all came with a key. 

I wrote a function called decrypt which takes two arguments, and then set 'plaintext' to empty string as it has not been assigned any decrypted text yet. 

I used a for loop to loop through the lenght of the ciphertext one at a time, and also used a while loop to set the conditionals to make sure that the key input must be between 1 and 10, and everything else outside that will reject and ask user to enter a valid key. 

