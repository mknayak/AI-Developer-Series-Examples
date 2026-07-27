import os
from dotenv import load_dotenv
load_dotenv()

print(os.environ["VERSION"])
#print(os.environ["VERSION_NEW"])

print(os.getenv("VERSION_NEW","DEFAULT"))