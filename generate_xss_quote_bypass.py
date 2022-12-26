import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--payload', type=str, help='javascript code to tranform into numbers', required=True)
args = parser.parse_args()

final_payload = ''
for c in args.payload:
    final_payload+= str(ord(c)) + ','
final_payload = final_payload[:-1]
result = 'String.fromCharCode(' + final_payload + ')'
print(result)