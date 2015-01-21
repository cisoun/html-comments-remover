import re
import sys

fin = sys.argv[1]
fout = sys.argv[2]

fileInput = open(fin, 'r')
text = fileInput.read()
fileInput.close()

text = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", text)
text = re.sub(re.compile("//.*?\n"), "\n", text)
text = re.sub(re.compile("<!--[^>]*-->"), "", text)

fileOutput = open(fout, 'w')
fileOutput.write(text)
fileOutput.close()
