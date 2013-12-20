Note: All the scripts are in a single repository and extensionless so you can just clone the repo, and put the direcotry in your global $PATH variable for ease of use.


# hexof  

hexadecimal strings manipulation tool

usage: hexof &lt;string&gt; &lt;options&gt;
	
	options:
	
	-d <delimiter>	: put the <delimiter> string inbetween each returned character
	
	-r 				: reversed order
	
	-x <xor key>	: xor (EXPERIMENTAL)
	
	-g <nb>			: group characters (default 1)
	
	--asm			: alias for: hexof -d "push $0x" -g 4 -r

fun example:
	
	echo -e $(hexof hello -d "\\x")

# brutegen  
Generate every possible strings based on a custom charset, and a custom length

usage: bruteGen AB 3

AAA BAA ABA BBA AAB BAB ABB BBB


# cheat 
easy file creation

usage: cheat &lt;filename&gt;

creates/edits a file &lt;filename&gt; in your $HOME/.cheat/ directory
can be used to take notes about commands.

# urld  

easy url decode from the command line

usage: urld url%20encoded%20string

# urle

easy url encode from the command line

usage: urle "enc()de [me]"
