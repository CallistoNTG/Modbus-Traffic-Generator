from ModLib import *

connection = connectToTarget();
results = getSupportedFunctionCodes(connection);
print("#", flush=True)
closeConnectionToTarget();
