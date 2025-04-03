# Add all your Python calls here:
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Contrary to popular belief and upon closer inspection,"
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Factually,"
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "In reality,"
# python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Experts agree that,"
# python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Upon closer inspection,"
python truthfulqa.py facebook/opt-125m --demos demonstrations.txt --system-prompt "Contrary to popular belief and upon closer inspection,"
# ... etc.