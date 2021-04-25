
run: main.py display.py draw.py matrix.py parser.py
	python main.py

test: main.py display.py draw.py matrix.py parser.py
	python3 main.py
	
fly: main.py display.py draw.py matrix.py parser.py
	python3 main.py
	rm new_script
	touch new_script
clean:
	rm *.pyc
	rm *~
