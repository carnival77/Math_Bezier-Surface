make:
	@cp src/main.py .
	@mv main.py 309pollution
	@chmod +x 309pollution


clean:
	@rm -f 309pollution
	@rm -f *.py


fclean: clean
	@rm -rf __pycache__


re: fclean make

test: re
	#./309pollution ; echo "$$?" #No arguments
	#./309pollution 1 file.csv ; echo "$$?" #Need more arguments
	#./309pollution -1 file.csv 1 1 1; echo "$$?" #Too many arguments
	#./309pollution -1 file.csv 1 1; echo "$$?" #Negative size
	#./309pollution 0 file.csv 1 1; echo "$$?" #Negative size
	#./309pollution 3 file.csv 4 1; echo "$$?" #Out of range
	#./309pollution 3 file.csv 1 4; echo "$$?" #Out of range
	#./309pollution 0.1 file.csv 1 1; echo "$$?" #Float size
	#./309pollution -h 
	#./309pollution 3 none 0 2; echo "$$?" #File not existant
	#./309pollution 3 empty 0 2; echo "$$?" #File empty
	#./309pollution 3 error 0 2; echo "$$?" #File bad format
	./309pollution 3 file.csv 0 2 #Result: 0.00
	./309pollution 3 file.csv 0.6 2 #Result: 28.20
	./309pollution 3 file.csv 1.3 2 #Result: 56.55
	./309pollution 3 file.csv 1 1.5 #Result: 33.94
	./309pollution 3 file.csv 0.8 0.8 #Result 26.11