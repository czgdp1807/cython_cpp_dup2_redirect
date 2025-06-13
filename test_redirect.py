import redirect
import os
import sys

print("[Python] Before redirection")

redirect.redirect("output.txt")

sys.stdout.flush()
sys.stdout = open(1, "w")

print("[Python] After redirection")
os.fdopen(1, "w").write("[Python] Written using fdopen\n")
