# Add all your Python calls here:
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Contrary to popular belief and think carefully,"
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "In reality,"
python truthfulqa.py facebook/opt-1.3b --demos demo2.txt --system-prompt "Contrary to popular belief,"
python truthfulqa.py facebook/opt-1.3b --demos demo2.txt --system-prompt "Contrary to popular belief and think carefully,"
python truthfulqa.py facebook/opt-1.3b --demos demo2.txt --system-prompt "In reality,"
# python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Experts agree that,"
# python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Upon closer inspection,"
# ... etc.