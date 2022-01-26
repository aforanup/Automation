# This is automation programs practice from tech-with-tim's Video Resource on Youtube

### For Multi-Clipboard Program

For clipboard_program, Please run through terminal with set of commands i.e. save, load and list<br />
I will be explaining as my understanding in my own words as i have completed building the program

<b><i>Target</i></b>

<p>
The target is to save a data to the system's clipboard
or/and
to extract a data from the system's clipboard to create a json file which will store and can be used to load those data through a key item pair
</p>

<b><i>Process</i></b>

<p>
We have to use <i>sys.argv</i> to get the command from the terminal
which is then checked for the commands save, load or just simply list all the key-data pair
if save is the command then we run a function with arguments file and data to be saved in that file.
We open the file as write using open -'w' and dump json data in it.
Here json data is the data from clipboard.paste() ie data that is currently in the system's clipboard.

For storing a data in system clipboard we ask for a key and from the file data which we loaded with read we use clipboard.copy(data) which will load the key pair data to the system's clipboard.

data is loaded for both saving and loading the data whith load_data function.

</p>
