# DUCTF
[Write Up Link](https://github.com/tbart27/DUCTF_Writeup/blob/master/DUCTF.md)<br>
### Team: 466 Crew
Taylor Bart<br>
Ryan Dunn<br>
John Tiffany<br>
Matt Evans<br>
By the end of the CTF we were able to solve 5 non-trivial challenges for 600 points, finishing at 505th.
### Reversing (Formatting)
To begin the CTF, John and I approached the reversing challenge of the CTF. We used binary ninja and at first glance we thought we found the flag in an almost trivial fashion.<br>
![](https://github.com/tbart27/DUCTF_Writeup/blob/master/Reversing3.PNG)<br>
However, after dereferencing the pointers, we obtained this string (which we still tried just on case, but it was still wrong).<br>
![](https://github.com/tbart27/DUCTF_Writeup/blob/master/Reversing4.PNG)<br>
Halfway through the CTF, our team regrouped and we approached reversing again. Once again we used binary ninja to inspect the binary and were able to find where the beginning of the flag was starting to be created.<br>
![](https://github.com/tbart27/DUCTF_Writeup/blob/master/Reversing1.PNG)<br>
We then followed the references until we were able to see their actual values.<br>
![](https://github.com/tbart27/DUCTF_Writeup/blob/master/Reversing2.PNG)<br>
At this point we noticed two things about the sprintf call:<br>
![](https://github.com/tbart27/DUCTF_Writeup/blob/master/Reversing5.PNG)<br>
1. It gave us a hint to ltrace the program.<br>
2. The sprintf call required formatting, just like the name of this challenge hints at.<br> 
A quick ltrace of the binary yielded:<br>
![](https://github.com/tbart27/DUCTF_Writeup/blob/master/Reversing6.PNG)<br>
ltrace didn't finish the whole string, however since we understand formatting and what the values were, we were able to recreate string like this: DUCTF{d1d_You_Just_ltrace_296faa2990acbc36}
### Crypto (Rot-i)
This was a Caesar cypher where the value for each letter's cypher was index % 26.<br>
I was able to start the python code and was able to fix minor issues with John's help, resulting in this [code](https://github.com/tbart27/DUCTF_Writeup/blob/master/decoder.py) and this output:<br>
Here's the flag! DUCTF{crypto_is_fun_kjqlptzy}
### Pwn (Shellthis)
Matt focused on Shellthis from the beginning, and was able to get all the framework needed to solve this once we came back together as a team. We approached this problem in the same way we approached Adam Doupe's Sug4rM4ma challenge by exploiting the buffer overflow vulnerability. A description of the entire process as it relates to sug4rM4ma can be found [here](https://www.youtube.com/watch?v=QGdwbum4O6U).<br>
However, the solution wasn't working because it was assuming python 2.x and not python 3.x! Fortunately, Ryan had python2 installed and was able to get the following:<br>
![](https://github.com/tbart27/DUCTF_Writeup/blob/master/pwn1.png)<br>
It was a very interesting tangent to figure out why only one of us was successful, and what the differences between python 2.x and 3.x was!<br>
### Misc (Welcome)
This was a simpler challenge solved by Ryan that involved putting the flag together from the image below:<br>
![](https://github.com/tbart27/DUCTF_Writeup/blob/master/misc1.PNG)<br>
### Misc (In a Pickle)
Ryan also figured out this challenge by using the name hint to know that the data was compressed by pickling. Simply using python's pickling libraries was enough to retrieve the flag from this challenge.
