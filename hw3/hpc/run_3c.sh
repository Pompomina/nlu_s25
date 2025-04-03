# Add all your Python calls here:
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Contrary to popular belief,"
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Careful reasoning suggests,"
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "To be precise,"
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Experts agree that,"
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Upon closer inspection,"
python truthfulqa.py facebook/opt-125m --demos demonstrations.txt --system-prompt "Contrary to popular belief,"
# ... etc.