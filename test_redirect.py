import redirect
import os
import sys

print("[Python] Before redirection")

redirect.redirect("output.txt")

sys.stdout.flush()
sys.stdout = open(1, "a")

print("[Python] After redirection")
