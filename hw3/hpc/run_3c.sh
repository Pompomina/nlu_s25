# Add all your Python calls here:
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Think critically and carefully and avoid bias,"
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "Respond as an expert in that field,"
python truthfulqa.py facebook/opt-1.3b --demos demonstrations.txt --system-prompt "A wrong answer might cause disaster,"
# ... etc.