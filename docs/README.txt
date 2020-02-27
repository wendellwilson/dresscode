Ever want to order somebody to don clothing and watch them struggle? This is the project for you.
Run dress_for_work.py and input a space separated list of numbers to indicate article of clothing to don.
This project is not compatible with python 2.

1 = hat
2 = pants
3 = shirt
4 = shoes
5 = socks

The worker you are ordering around will follow these Rules:

1. They must put your socks on before your shoes.
2. They must put your pants on before your shoes.
3. They must put your shirt on before your hat.
4. A hat is optional but all other articles of clothing are required.
5. They must leave the house when receiving the number 6. They must leave the house after getting dressed.
6. Any violation will output "fail" and stop immediately.

The 5th rule  has been interpreted to mean that there is a implied leave command at the end of every dressing sequence.

Example:
> python3 dresscode/dress_for_work.py
Please input a space separated list of numbers to indicate articles of clothing or actions. 1='hat', 2='pants', 3='shirt', 4='shoes', 5='socks', 6='leave'
> 6
fail
