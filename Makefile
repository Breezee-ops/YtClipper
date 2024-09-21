PYTHON=python3
REQUIREMENTS=requirements.txt
TARGET=src.py

.PHONY: all install run clean

install:
	$(PYTHON) -m pip install -r $(REQUIREMENTS)

run:
	$(PYTHON) $(TARGET) $(TIMESTAMPS)

clean:
	@echo "removing pyc and cached files"
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	find . -name "*.mp4" -delete